#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:14:51 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from pyqtgraphCore.Qt import QtCore, QtGui, USE_PYSIDE
from MesmerizeCore import ProjBrowser
from pyqtgraphCore.graphicsItems.InfiniteLine import *
import pyqtgraphCore
import numpy as np
import pickle
import sys
import ast
from MesmerizeCore import packager
from shutil import copyfile
import time
import pandas as pd
from MesmerizeCore.startWindow import startGUI
import os
from functools import partial

'''
Main file to be called. The intent is that if no arguments are passed the standard desktop application loads.
I intend to create a headless mode for doing certain things on a cluster/supercomputer

The instance of desktopApp is useful for communicating between the Viewer & Project Browser
'''

class main():
    def __init__(self, args=None):
        if args is None:
            self.app = QtGui.QApplication([])
            self.initStartWindow()
            
            self.viewer = None
            self.projName = None
            
            #self.openProj('/home/kushal/Sars_stuff/github-repos/testprojects/testnew/testnew_index.mzp')
            
            if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtGui.QApplication.instance().exec_()

    def initStartWindow(self):
        self.startWin = QtGui.QMainWindow()
        self.startWin.resize(448,88)
        self.startgui = startGUI()
        self.startWin.setCentralWidget(self.startgui)
        self.startWin.show()
        self.startgui.ui.openViewerBtn.clicked.connect(self.initViewer)
        self.startgui.ui.newProjBtn.clicked.connect(self.newProj)
        self.startgui.ui.openProjBtn.clicked.connect(self.openProjFileDialog)
        
    def newProj(self):
        parentPath = QtGui.QFileDialog.getExistingDirectory(None,'Choose location for new project')
        if parentPath == '':
            return
        print('parentPath is: ' + parentPath)
        projName, start = QtGui.QInputDialog.getText(None, '', 'Project Name:', QtGui.QLineEdit.Normal, '')
        if start and projName != '':
            self.projName = projName
            self.projPath = parentPath + '/' + self.projName
            os.mkdir(self.projPath)
            self.projDataFrame = packager.empty_df()
            self.projDataFrameFilePath = self.projPath + '/' + self.projName + '_index.mzp'
#            self.projDataFrame.to_csv(self.projDataFrameFilePath, index=False)
            self.projDataFrame.to_pickle(self.projDataFrameFilePath, protocol=4)
            # Start the Project Browser loaded with the dataframe columns in the listwidget
            self.initProjBrowser()
    
    def openProjFileDialog(self):
        mzpPath = QtGui.QFileDialog.getOpenFileName(None, 'Select Project Index File', 
                                                      '.', '(*.mzp)')[0]
        self.openProj(mzpPath)
        
    def openProj(self, mzpPath):
        self.projDataFrameFilePath = mzpPath
        if self.projDataFrameFilePath == '':
            return
        self.projPath = os.path.dirname(self.projDataFrameFilePath)
        self.projDataFrame = pd.read_pickle(self.projDataFrameFilePath) 
        self.projName = self.projPath.split('/')[-1][:-4]
        # Start the Project Browser loaded with the dataframe columns in the listwidget
        self.initProjBrowser()
        
    def initProjBrowser(self):
        try:
            self.startWin.hide()
        except:
            pass
        special = {'Timings': 'StimSet'}
        self.projBrowser = ProjBrowser.Window(self.projDataFrame, special=special)
        self.projBrowser.resize(1000,840)
        self.projBrowser.show()
        
        ## Create window with Project Explorer widget
#        self.projectWindow = QtGui.QMainWindow()
#        self.projectWindow.resize(1000,800)
#        self.projectWindow.setWindowTitle('Mesmerize - Project Browser')
#        self.projBrowser = ProjBrowser()
#        self.projectWindow.setCentralWidget(self.projBrowser)
#        exclude = ['ImgPath', 'ROIhandles', 'ImgInfoPath', 'CurvePath']
#        
#        special = {'Timings': 'StimSet'}
#        self.projBrowser.setupGUI(projDataFrame, exclude, special)
#        self.projectWindow.show()
        if self.viewer is None:
            self.initViewer()
        #self.projBrowser.ui.openViewerBtn.clicked.connect(self.viewerWindow.show())
        self.viewer.projPath = self.projPath
        n = 0
        for col in self.projDataFrame.columns:
            if col.startswith('ROI_DEF:'):
                n+=1
                s = 'self.viewer.ui.labelROIDef_'+str(n)+".setText('"+col[8:]+"')"
                eval(s)
            
    def initViewer(self):
        try:
            self.startWin.hide()
        except:
            pass
        # Interpret image data as row-major instead of col-major
        pyqtgraphCore.setConfigOptions(imageAxisOrder='row-major')
    
        ## Create window with ImageView widget
        self.viewerWindow = QtGui.QMainWindow()
        self.viewerWindow.resize(1458,931)
        self.viewer = pyqtgraphCore.ImageView()
        self.viewerWindow.setCentralWidget(self.viewer)
#        self.projBrowser.ui.openViewerBtn.clicked.connect(self.showViewer)
        self.viewerWindow.setWindowTitle('Mesmerize - viewer')
        
        ## Set a custom color map
        colors = [
            (0, 0, 0),
            (45, 5, 61),
            (84, 42, 55),
            (150, 87, 60),
            (208, 171, 141),
            (255, 255, 255)
        ]
        cmap = pyqtgraphCore.ColorMap(pos=np.linspace(0.0, 1.0, 6), color=colors)
        self.viewer.setColorMap(cmap)
        
        self.viewer.ui.btnAddCurrEnvToProj.clicked.connect(self.addWorkEnvToProj)        
        self.viewer.ui.btnAddToBatch.clicked.connect(self.viewerAddToBatch)
        self.viewer.ui.btnOpenBatch.clicked.connect(self.viewerOpenBatch)
        self.viewerWindow.show()
        
    def isProjLoaded(self):
        if self.projName is None:
            answer = QtGui.QMessageBox.question(self.viewer, 'Message', 
                        'You don''t have any project open! ' +\
                        'Would you like to start a new project (Yes) or Open a project?', 
                        QtGui.QMessageBox.Yes, QtGui.QMessageBox.Open)
            if answer == QtGui.QMessageBox.Yes:
                self.newProj()
            elif answer == QtGui.QMessageBox.Open:
                self.openProj()
                
            return False
        
        else:
            return True
    
    def viewerAddToBatch(self):
        if self.isProjLoaded():
            self.viewer.addToBatch()
    
    def viewerOpenBatch(self):
        if self.isProjLoaded():
            self.viewer.openBatch()
    
    def addWorkEnvToProj(self):
        if self.isProjLoaded():
            df = packager.workEnv2pandas(self.projDataFrame,
                                self.projPath,
                                self.viewer.currImgDataObj, 
                                self.viewer.ROIlist,
                                self.viewer.ROItags,
                                self.viewer.Curveslist)
            print(df)
            # Create backup of index
            copyfile(self.projDataFrameFilePath, 
                     self.projDataFrameFilePath + '.BACKUP_' + str(time.time()))
            
            self.projDataFrame = df
            # Save index
#            self.projDataFrame.to_csv(self.projDataFrameFilePath, index=False)
            self.projDataFrame.to_pickle(self.projDataFrameFilePath, protocol=4)
            self.projBrowser.tabs.widget(0).df = df
            self.projBrowser.tabs.widget(0).updateDf()
            
            
if __name__ == '__main__':
    gui = main()