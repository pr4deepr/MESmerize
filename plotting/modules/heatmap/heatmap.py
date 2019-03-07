#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraphCore.widgets.MatplotlibWidget import MatplotlibWidget
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle as RectangularPatch
from matplotlib.lines import Line2D
from matplotlib import cm


class Heatmap(MatplotlibWidget):
    signal_row_selection_changed = QtCore.pyqtSignal(int)

    def __init__(self, highlight_mode='row'):
        MatplotlibWidget.__init__(self)
        sns.set()
        self.ax_heatmap = self.fig.add_subplot(111)
        self.fig.subplots_adjust(right=0.8)
        self.cbar_ax = self.fig.add_axes([0.85, 0.15, 0.05, 0.7])
        self.data = None
        self._highlight = None
        self.highlighted_index = None

        self.stimulus_indicators = []

        if highlight_mode == 'row':
            self.canvas.mpl_connect('button_press_event', self.highlight_row)
        elif highlight_mode == 'item':
            pass

        self.labelSort = QtWidgets.QLabel(self)
        self.labelSort.setText('Sort heatmap according to column:')
        self.labelSort.setMinimumHeight(30)
        self.labelSort.setMaximumHeight(30)
        self.comboBoxSortColumn = QtWidgets.QComboBox(self)
        #
        self.layout().addWidget(self.labelSort)
        self.layout().addWidget(self.comboBoxSortColumn)

        self.labelSort.hide()
        self.comboBoxSortColumn.hide()

    def unhide_sort_gui(self):
        self.labelSort.show()
        self.comboBoxSortColumn.show()

    def set(self, data: np.ndarray, *args, **kwargs):
        """
        :param data:    2D numpy array
        :param args:    Additional args that are passed to sns.heatmap()
        :param kwargs:  Additional kwargs that are passed to sns.heatmap()
        """
        self.ax_heatmap.cla()
        self._highlight = None
        self.cbar_ax.cla()
        self.data = data

        self.plot = sns.heatmap(data, *args, ax=self.ax_heatmap, cbar_ax=self.cbar_ax, **kwargs)

        self.draw()

    def highlight_row(self, ev):
        if type(ev) is int:
            ix = ev
        else:
            ix = ev.ydata
            ix = int(ix)
            if ix is None:
                return
        self.highlighted_index = ix
        self.signal_row_selection_changed.emit(ix)
        if self._highlight is not None:
            self._highlight.remove()
        self._highlight = self.plot.add_patch(RectangularPatch((0, ix), self.data.shape[1], 1, facecolor='w', edgecolor='k', lw=3, alpha=0.5))
        self.draw()

    def add_stimulus_indicator(self, start: int, end: int, color: str):
        for t in [start, end]:
            x = np.array([t, t])
            y = np.array([0, self.data.shape[0]])
            line = Line2D(x, y, lw=3, color=color)
            self.stimulus_indicators.append(line)
            self.plot.add_line(line)


class Clustermap(Heatmap):
    def __init__(self):
        Heatmap.__init__(self)

    def set(self, data: np.ndarray, *args, **kwargs):
        """
        :param data:    2D numpy array
        :param args:    Additional args that are passed to sns.heatmap()
        :param kwargs:  Additional kwargs that are passed to sns.heatmap()
        """
        self.ax_heatmap.cla()
        self.cbar_ax.cla()
        self.data = data
        self.plot = sns.clustermap(data, *args, ax=self.ax_heatmap, cbar_ax=self.cbar_ax, **kwargs)
        self.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = Heatmap()
    w.show()
    data = np.load('/home/kushal/Sars_stuff/palp_project_mesmerize/zst_data.npy')
    w.set(data, cmap='jet')
    w.add_stimulus_indicator(144, 288, 'k')
    app.exec()
