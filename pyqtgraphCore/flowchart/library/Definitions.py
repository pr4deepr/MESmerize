# -*- coding: utf-8 -*-
import numpy as np
from ...Qt import QtCore, QtGui
from ..Node import Node
from . import functions
from ... import functions as pgfn
from .common import *
from ...python2_3 import xrange
from ... import PolyLineROI
from ... import Point
from ... import metaarray as metaarray
from analyser.DataTypes import *
from MesmerizeCore.misc_funcs import empty_df
from MesmerizeCore import configuration
from functools import partial
from analyser import PeakEditor

configuration.configpath = '/home/kushal/Sars_stuff/github-repos/testprojects/feb6-test-10/config.cfg'
configuration.openConfig()

class AlignStims(CtrlNode):
    """Align Stimulus Definitions"""
    nodeName = 'AlignStims'
    uiTemplate = [('Stim_Type', 'combo', {'values': []}),
                  ('Stimulus', 'lineEdit', {'placeHolder': 'Stimulus and/or Substim', 'text': ''}),
                  ('start_offset', 'doubleSpin', {'min': 0, 'max': 999999.99, 'value': 0, 'step': 1}),
                  ('end_offset', 'doubleSpin', {'min': 0, 'max': 999999.99, 'value': 0, 'step': 1}),
                  ('zero_pos', 'combo', {'values': ['start_offset', 'stim_end', 'stim_center']}),
                  ('Apply', 'check', {'checked': False, 'applyBox': True})
                  ]

    def setAutoCompleter(self, stim_def):
        stims = list(set([a for b in self.transmission.df[stim_def].tolist() for a in b]))
        autocompleter = QtGui.QCompleter(stims, self.ctrls['Stimulus'])
        self.ctrls['Stimulus'].setCompleter(autocompleter)

    # def connected(self, localTerm, remoteTerm):
    #     pass

    def processData(self, transmission):
        self.transmission = transmission.copy()
        assert isinstance(self.transmission, Transmission)
        # Very messy work-around because the usual widget clear() and removeItem() result in
        # stack overflow from recursion over here. Something to do with Node.__get__attr I think.
        # Results in a really stupid bug where stuff in the comboBox is duplicated.
        all_stims = []
        for i in range(self.ctrls['Stim_Type'].count()):
            all_stims.append(self.ctrls['Stim_Type'].itemText(i))
        for item in self.transmission.STIM_DEFS:
            if item in all_stims:
                continue
            else:
                self.ctrls['Stim_Type'].addItem(item)

        self.ctrls['Stim_Type'].currentTextChanged.connect(self.setAutoCompleter)
        if self.ctrls['Apply'].isChecked() is False:
            return

        stim_def = self.ctrls['Stim_Type'].currentText()
        stim_tag = self.ctrls['Stimulus'].text()
        start_offset = self.ctrls['start_offset'].value()
        end_offset = self.ctrls['end_offset'].value()
        zero_pos = self.ctrls['zero_pos'].currentText()

        params = {'stim_def': stim_def,
                  'stim_tag': stim_tag,
                  'start_offset': start_offset,
                  'end_offset': end_offset,
                  'zero_pos': zero_pos
                  }

        t = Transmission(empty_df(), self.transmission.src, self.transmission.data_column['curve'], dst=self.transmission.dst)
        for ix, r in self.transmission.df.iterrows():
            ## TODO: Should use an if-continue block, just not critical at the moment
            try:
                smap = r['stimMaps'].flatten()[0][stim_def]
                # print(smap)
            except KeyError:
                continue
            # print(r)
            curve = r[self.transmission.data_column['curve']]
            for stim in smap:
                if stim_tag in stim[0][0]:
                    continue
                if curve is None:
                    continue
                stim_start = stim[-1][0]
                stim_end = stim[-1][1]

                if zero_pos == 'start_offset':

                    tstart = max(stim_start + start_offset, 0)
                    tend = min(stim_end + end_offset, np.size(curve))

                elif zero_pos == 'stim_end':
                    tstart = stim_end
                    tend = tstart + end_offset

                elif zero_pos == 'stim_center':
                    tstart = int(((stim_start + stim_end) / 2)) + start_offset
                    tend = min(stim_end + end_offset, np.size(curve))

                rn = r.copy()

                tstart = int(tstart)
                tend = int(tend)

                sliced_curve = np.take(curve, np.arange(tstart, tend), axis=0)

                rn[self.transmission.data_column['curve']] = sliced_curve / np.min(sliced_curve)
                rn[stim_def] = stim[0][0]

                t.df = t.df.append(rn, ignore_index=True)
        # print(t.df)

        t.src.append({'AlignStims': params})
        print('ALIGN_STIMS APPENDED')
        print(t.src)
        t.data_column['curve'] = self.transmission.data_column['curve']
        t.plot_this = t.data_column['curve']

        return t


class DF_IDX(CtrlNode):
    """Pass only one or multiple DataFrame Indices"""
    nodeName = 'DF_IDX'
    uiTemplate = [('Index', 'intSpin', {'min': 0, 'step': 1, 'value': 0}),
                  ('Indices', 'lineEdit', {'text': '0', 'toolTip': 'Index numbers separated by commas'})
                  ]

    def processData(self, transmission):
        self.ctrls['Index'].setMaximum(len(transmission.df.index)-1)
        self.ctrls['Index'].valueChanged.connect(partial(self.ctrls['Indices'].setText, str(self.ctrls['Index'].value())))

        indices = [int(ix.strip()) for ix in self.ctrls['Indices'].text().split(',')]
        t = transmission.copy()
        t.df = t.df.iloc[indices, :]
        t.src.append({'DF_IDX': {'indices': indices}})
        return t


class ROI_Selection(CtrlNode):
    """Pass-through DataFrame rows if they have the chosen tags"""
    nodeName = 'ROI_Selection'
    uiTemplate = [('ROI_Type', 'combo', {'values': []}),
                  ('availTags', 'label', {'toolTip': 'All tags found under this ROI_Def'}),
                  ('ROI_Tags', 'lineEdit', {'toolTip': 'Enter one or many tags separated by commas (,)\n' +\
                                                       'Spaces before or after commas do not matter'}),
                  ('Include', 'radioBtn', {'checked': True}),
                  ('Exclude', 'radioBtn', {'checked': False}),
                  ('Apply', 'check', {'checked': False, 'applyBox': True})
                  ]

    def _setAvailTags(self, roi_def):
        tags = list(set(self.transmission.df[roi_def]))
        self.ctrls['availTags'].setText(', '.join(tags))
        self.ctrls['availTags'].setToolTip('\n'.join(tags))

    def processData(self, transmission):
        assert isinstance(transmission, Transmission)
        self.transmission = transmission.copy()

        # Very messy work-around because the usual widget clear() and removeItem() result in
        # stack overflow from recursion over here. Something to do with Node.__get__attr I think.
        # Results in a really stupid bug where stuff in the comboBox is duplicated.
        all_roi_defs = []
        for i in range(self.ctrls['ROI_Type'].count()):
            all_roi_defs.append(self.ctrls['ROI_Type'].itemText(i))

        for item in self.transmission.ROI_DEFS:  # transmission.ROI_DEFS comes from MesmerizeCore.configuration
            if item in all_roi_defs:             # during the creation of the Transmission class object
                continue
            else:
                self.ctrls['ROI_Type'].addItem(item)

        self.ctrls['ROI_Type'].currentTextChanged.connect(self._setAvailTags)

        if self.ctrls['Apply'].isChecked() is False:
            return

        chosen_tags = [tag.strip() for tag in self.ctrls['ROI_Tags'].text().split(',')]

        t = self.transmission.copy()
        '''***************************************************************************'''
        ## TODO: CHECK IF THIS IS ACTUALLY DOING THE RIGHT THING!!!!
        t.df = t.df[t.df[self.ctrls['ROI_Type'].currentText()].isin(chosen_tags)]
        '''***************************************************************************'''

        params = {'ROI_DEF': self.ctrls['ROI_Type'].currentText(),
                  'tags': chosen_tags}

        t.src.append({'ROI_Include': params})

        return t


class PeakFeaturesExtract(CtrlNode):
    """Extract peak features. Use this after the Peak_Detect node."""
    nodeName = 'Peak_Features_Extract'
    uiTemplate = [('Apply', 'check', {'checked': True, 'applyBox': True}),

                  ('Amplitude', 'check', {'checked': True}),
                  ('Peak_Area', 'check', {'checked': True}),

                  ('Rising_Slope_avg', 'check', {'checked': True}),
                  ('Falling_Slope_avg', 'check', {'checked': True}),

                  ('Peak_Duration_Base', 'check', {'checked': True}),
                  ('Peak_Duration_Mid', 'check', {'checked': True}),
                  ('Inter_Peak_Interval', 'check', {'checked': True}),
                  ]

    def __init__(self, name):
        # super(Save, self).__init__(name, terminals={'data': {'io': 'in'}})
        CtrlNode.__init__(self, name, terminals={'In': {'io': 'in', 'multi': True}, 'Out': {'io': 'out'}})
        self.ctrls['Apply'].clicked.connect(self._fileDialog)

    def process(self, In, display=True):
        self._update_stats(In)

    def _update_stats(self, In):

        print(In)
        pass


class Universal_Statistics_Of_Type_ANOVA_For_Example(CtrlNode):
    """Takes in a transmission that comes from certain types of nodes that output data
    which can be used by this node to do the final stats and draw plots."""
    uiTemplate = [('Apply', 'check', {'checked': True, 'applyBox': True})]

    def processData(self, **kwargs):
        pass


# class StatsPlots(CtrlNode):
#     """Perform statistics and draw plots"""

# TODO: BASED ON PARAMETERS DESCRIBED BY THAT UNI OF MARYLAND PROF. SUCH AS MINIMUM SLOPE AND AMPLITUDE ETC.
class PeakDetect(CtrlNode):
    """Detect peaks & bases by finding local maxima & minima. Use this after the Derivative Filter"""
    nodeName = 'Peak_Detect'
    uiTemplate = [('Apply', 'check', {'checked': True, 'applyBox': True}),
                  ('Edit', 'button', {'text': 'Open Editor'}),
                  ('SlopeThr', 'label', {'text': ''}),
                  ('AmpThr', 'label', {'text': ''})
                  ]

    def __init__(self, name, **kwargs):
        CtrlNode.__init__(self, name, terminals={'Derivative': {'io': 'in'},
                                                 'Curve': {'io': 'in'},
                                                 'Out': {'io': 'out', 'bypass': 'In'}}, **kwargs)
        self.data_modified = False
        self.editor_output = False
        self.ctrls['Edit'].clicked.connect(self._peak_editor)
        self.t = None

    @staticmethod
    def _get_zero_crossings(dsig):
        """
        Determine the peaks and bases of the signal by finding zero crossing in the first derivative of the signal
        :param dsig: The first derivative of the signal
        :type dsig: np.array
        :return: DataFrame, all zero crossing events in one column, another column denotes it as a peak or base.
        :rtype: pd.DataFrame
        """
        sc = np.diff(np.sign(dsig))

        peaks = np.where(sc < 0)[0]
        bases = np.where(sc > 0)[0]

        peaks_df = pd.DataFrame()
        peaks_df['event'] = peaks
        peaks_df['label'] = 'peak'

        bases_df = pd.DataFrame()
        bases_df['event'] = bases
        bases_df['label'] = 'base'

        peaks_bases_df = pd.concat([peaks_df, bases_df])
        assert isinstance(peaks_bases_df, pd.DataFrame)
        peaks_bases_df = peaks_bases_df.sort_values('event')
        peaks_bases_df = peaks_bases_df.reset_index(drop=True)

        peaks_bases_df['peak'] = peaks_bases_df['label'] == 'peak'
        peaks_bases_df['base'] = peaks_bases_df['label'] == 'base'

        # print(peaks_bases_df)

        return peaks_bases_df

    def process(self, display=True, **kwargs):
        out = self.processData(**kwargs)
        return {'Out': out}

    def processData(self, **inputs):
        if self.editor_output:
            return self.t

        if self.data_modified is True:
            if QtGui.QMessageBox.question(None, 'Discard peak edits?',
                                          'You have made modifications to peak data passing '
                                          'through this node! Would you like to discard all '
                                          'changes and load the newly transmitted data?',
                                          QtGui.QMessageBox.Yes,
                                          QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
                return self.t
        self.data_modified = False

        if inputs['Derivative'] is None:
            raise Exception('No incoming Derivative transmission. '
                            'You must input both a curve and its derivative')

        if inputs['Curve'] is None:
            raise Exception('No incoming Curve transmission.'
                            ' You must input both a curve and its derivative')

        if inputs['Derivative'].df.index.size != inputs['Curve'].df.index.size:
            QtGui.QMessageBox.warning(None, 'ValueError!', 'Input diemensions of Derivative and Curve transmissions'
                                                           ' MUST match!')
            raise ValueError('Input diemensions of Derivative and Curve transmissions MUST match!')

        self.t = inputs['Derivative'].copy()
        self.t_curve = inputs['Curve']

        assert isinstance(self.t, Transmission)
        assert isinstance(self.t_curve, Transmission)

        self.t.data_column['peaks_bases'] = 'peaks_bases'
        self.t.df[self.t.data_column['peaks_bases']] = self.t.df[self.t.data_column['curve']].apply(lambda s: PeakDetect._get_zero_crossings(s))

        self.t.df[self.t.data_column['curve']] = deepcopy(self.t_curve.df[self.t_curve.data_column['curve']])


        if hasattr(self, 'pbw'):
            self.pbw.update_transmission(self.t_curve, self.t)

        return self.t

    def _set_editor_output(self):
        self.pbw.close()
        self.editor_output = True
        self.t = self.pbw.getData()
        self.pbw = None
        self.data_modified = True
        self.update()

    def _peak_editor(self):
        self.pbw = PeakEditor.PBWindow(self.t_curve, self.t)
        self.pbw.show()
        self.pbw.btnDone.clicked.connect(self._set_editor_output)
