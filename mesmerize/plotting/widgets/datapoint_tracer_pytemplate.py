# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './datapoint_tracer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DatapointTracer(object):
    def setupUi(self, DatapointTracer):
        DatapointTracer.setObjectName("DatapointTracer")
        DatapointTracer.resize(1043, 697)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DatapointTracer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(DatapointTracer)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEditUUID = QtWidgets.QLineEdit(DatapointTracer)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUUID.setFont(font)
        self.lineEditUUID.setReadOnly(True)
        self.lineEditUUID.setObjectName("lineEditUUID")
        self.horizontalLayout_3.addWidget(self.lineEditUUID)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.splitterMain = QtWidgets.QSplitter(DatapointTracer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitterMain.sizePolicy().hasHeightForWidth())
        self.splitterMain.setSizePolicy(sizePolicy)
        self.splitterMain.setOrientation(QtCore.Qt.Horizontal)
        self.splitterMain.setObjectName("splitterMain")
        self.groupBoxInfo = QtWidgets.QGroupBox(self.splitterMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxInfo.sizePolicy().hasHeightForWidth())
        self.groupBoxInfo.setSizePolicy(sizePolicy)
        self.groupBoxInfo.setObjectName("groupBoxInfo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonOpenInViewer = QtWidgets.QPushButton(self.groupBoxInfo)
        self.pushButtonOpenInViewer.setObjectName("pushButtonOpenInViewer")
        self.verticalLayout.addWidget(self.pushButtonOpenInViewer)
        self.pushButtonOpenAnalysisGraph = QtWidgets.QPushButton(self.groupBoxInfo)
        self.pushButtonOpenAnalysisGraph.setObjectName("pushButtonOpenAnalysisGraph")
        self.verticalLayout.addWidget(self.pushButtonOpenAnalysisGraph)
        self.groupBoxImageViewAndCurve = QtWidgets.QGroupBox(self.splitterMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxImageViewAndCurve.sizePolicy().hasHeightForWidth())
        self.groupBoxImageViewAndCurve.setSizePolicy(sizePolicy)
        self.groupBoxImageViewAndCurve.setObjectName("groupBoxImageViewAndCurve")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxImageViewAndCurve)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonMaxProjection = QtWidgets.QRadioButton(self.groupBoxImageViewAndCurve)
        self.radioButtonMaxProjection.setChecked(True)
        self.radioButtonMaxProjection.setObjectName("radioButtonMaxProjection")
        self.horizontalLayout_2.addWidget(self.radioButtonMaxProjection)
        self.radioButtonSTDProjection = QtWidgets.QRadioButton(self.groupBoxImageViewAndCurve)
        self.radioButtonSTDProjection.setObjectName("radioButtonSTDProjection")
        self.horizontalLayout_2.addWidget(self.radioButtonSTDProjection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.splitterImageViewAndCurve = QtWidgets.QSplitter(self.groupBoxImageViewAndCurve)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitterImageViewAndCurve.sizePolicy().hasHeightForWidth())
        self.splitterImageViewAndCurve.setSizePolicy(sizePolicy)
        self.splitterImageViewAndCurve.setOrientation(QtCore.Qt.Vertical)
        self.splitterImageViewAndCurve.setObjectName("splitterImageViewAndCurve")
        self.graphicsViewImage = GraphicsLayoutWidget(self.splitterImageViewAndCurve)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.graphicsViewImage.sizePolicy().hasHeightForWidth())
        self.graphicsViewImage.setSizePolicy(sizePolicy)
        self.graphicsViewImage.setObjectName("graphicsViewImage")
        self.graphicsViewPlot = PlotWidget(self.splitterImageViewAndCurve)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.graphicsViewPlot.sizePolicy().hasHeightForWidth())
        self.graphicsViewPlot.setSizePolicy(sizePolicy)
        self.graphicsViewPlot.setObjectName("graphicsViewPlot")
        self.verticalLayout_2.addWidget(self.splitterImageViewAndCurve)
        self.verticalLayout_3.addWidget(self.splitterMain)

        self.retranslateUi(DatapointTracer)
        QtCore.QMetaObject.connectSlotsByName(DatapointTracer)

    def retranslateUi(self, DatapointTracer):
        _translate = QtCore.QCoreApplication.translate
        DatapointTracer.setWindowTitle(_translate("DatapointTracer", "Form"))
        self.label.setText(_translate("DatapointTracer", "UUID:"))
        self.groupBoxInfo.setTitle(_translate("DatapointTracer", "Info"))
        self.pushButtonOpenInViewer.setText(_translate("DatapointTracer", "Open in viewer"))
        self.pushButtonOpenAnalysisGraph.setText(_translate("DatapointTracer", "Open Analysis Graph"))
        self.groupBoxImageViewAndCurve.setTitle(_translate("DatapointTracer", "Image"))
        self.radioButtonMaxProjection.setText(_translate("DatapointTracer", "&Max Projection"))
        self.radioButtonSTDProjection.setText(_translate("DatapointTracer", "Standard De&viation Projection"))

from ...pyqtgraphCore import GraphicsLayoutWidget, PlotWidget
