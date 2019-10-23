# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './control_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CrossCorrelationControls(object):
    def setupUi(self, CrossCorrelationControls):
        CrossCorrelationControls.setObjectName("CrossCorrelationControls")
        CrossCorrelationControls.resize(904, 706)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(CrossCorrelationControls)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.splitter = QtWidgets.QSplitter(CrossCorrelationControls)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayoutLeftMain = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayoutLeftMain.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutLeftMain.setObjectName("verticalLayoutLeftMain")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.comboBoxDataColumn = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxDataColumn.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBoxDataColumn.setObjectName("comboBoxDataColumn")
        self.verticalLayout_6.addWidget(self.comboBoxDataColumn)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.comboBoxLabelsColumn = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxLabelsColumn.setObjectName("comboBoxLabelsColumn")
        self.verticalLayout_6.addWidget(self.comboBoxLabelsColumn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.radioButtonLag = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButtonLag.setChecked(True)
        self.radioButtonLag.setObjectName("radioButtonLag")
        self.verticalLayout_2.addWidget(self.radioButtonLag)
        self.radioButtonMaxima = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButtonMaxima.setObjectName("radioButtonMaxima")
        self.verticalLayout_2.addWidget(self.radioButtonMaxima)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.checkBoxAbsoluteValue = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxAbsoluteValue.setChecked(True)
        self.checkBoxAbsoluteValue.setObjectName("checkBoxAbsoluteValue")
        self.verticalLayout_3.addWidget(self.checkBoxAbsoluteValue)
        self.doubleSpinBoxLagThreshold = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxLagThreshold.setMinimum(-999.0)
        self.doubleSpinBoxLagThreshold.setMaximum(999.0)
        self.doubleSpinBoxLagThreshold.setSingleStep(0.5)
        self.doubleSpinBoxLagThreshold.setProperty("value", 1.0)
        self.doubleSpinBoxLagThreshold.setObjectName("doubleSpinBoxLagThreshold")
        self.verticalLayout_3.addWidget(self.doubleSpinBoxLagThreshold)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.doubleSpinBoxMaximaThreshold = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMaximaThreshold.setMinimum(-1.0)
        self.doubleSpinBoxMaximaThreshold.setMaximum(1.0)
        self.doubleSpinBoxMaximaThreshold.setSingleStep(0.01)
        self.doubleSpinBoxMaximaThreshold.setProperty("value", 0.5)
        self.doubleSpinBoxMaximaThreshold.setObjectName("doubleSpinBoxMaximaThreshold")
        self.verticalLayout_4.addWidget(self.doubleSpinBoxMaximaThreshold)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayoutLeftMain.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonComputeAllData = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonComputeAllData.setFont(font)
        self.pushButtonComputeAllData.setObjectName("pushButtonComputeAllData")
        self.horizontalLayout_6.addWidget(self.pushButtonComputeAllData)
        self.pushButtonExportAllData = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonExportAllData.setFont(font)
        self.pushButtonExportAllData.setObjectName("pushButtonExportAllData")
        self.horizontalLayout_6.addWidget(self.pushButtonExportAllData)
        self.verticalLayoutLeftMain.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEditCurve1UUID = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditCurve1UUID.setFont(font)
        self.lineEditCurve1UUID.setReadOnly(True)
        self.lineEditCurve1UUID.setObjectName("lineEditCurve1UUID")
        self.horizontalLayout_5.addWidget(self.lineEditCurve1UUID)
        self.verticalLayoutLeftMain.addLayout(self.horizontalLayout_5)
        self.graphicsViewCurve1 = PlotWidget(self.layoutWidget)
        self.graphicsViewCurve1.setObjectName("graphicsViewCurve1")
        self.verticalLayoutLeftMain.addWidget(self.graphicsViewCurve1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEditCurve2UUID = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditCurve2UUID.setFont(font)
        self.lineEditCurve2UUID.setReadOnly(True)
        self.lineEditCurve2UUID.setObjectName("lineEditCurve2UUID")
        self.horizontalLayout_4.addWidget(self.lineEditCurve2UUID)
        self.verticalLayoutLeftMain.addLayout(self.horizontalLayout_4)
        self.graphicsViewCurve2 = PlotWidget(self.layoutWidget)
        self.graphicsViewCurve2.setObjectName("graphicsViewCurve2")
        self.verticalLayoutLeftMain.addWidget(self.graphicsViewCurve2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutLeftMain.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.listWidgetSampleID = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidgetSampleID.setObjectName("listWidgetSampleID")
        self.verticalLayout_5.addWidget(self.listWidgetSampleID)
        self.verticalLayout_9.addWidget(self.splitter)

        self.retranslateUi(CrossCorrelationControls)
        QtCore.QMetaObject.connectSlotsByName(CrossCorrelationControls)

    def retranslateUi(self, CrossCorrelationControls):
        _translate = QtCore.QCoreApplication.translate
        CrossCorrelationControls.setWindowTitle(_translate("CrossCorrelationControls", "Form"))
        self.label_5.setText(_translate("CrossCorrelationControls", "Parameters"))
        self.label_10.setText(_translate("CrossCorrelationControls", "Data column:"))
        self.label_12.setText(_translate("CrossCorrelationControls", "Labels column:"))
        self.label_2.setText(_translate("CrossCorrelationControls", "Visualization:"))
        self.radioButtonLag.setText(_translate("CrossCorrelationControls", "&lag"))
        self.radioButtonMaxima.setText(_translate("CrossCorrelationControls", "&maxima"))
        self.label_11.setText(_translate("CrossCorrelationControls", "Thresholds"))
        self.label_3.setText(_translate("CrossCorrelationControls", "lag"))
        self.checkBoxAbsoluteValue.setText(_translate("CrossCorrelationControls", "absolute value"))
        self.label_4.setText(_translate("CrossCorrelationControls", "maxima"))
        self.pushButtonComputeAllData.setText(_translate("CrossCorrelationControls", "Compute all data"))
        self.pushButtonExportAllData.setText(_translate("CrossCorrelationControls", "Export all data"))
        self.label_6.setText(_translate("CrossCorrelationControls", "Curve 1"))
        self.label_7.setText(_translate("CrossCorrelationControls", "Curve 2"))
        self.label_8.setText(_translate("CrossCorrelationControls", "Cross-correlation function"))
        self.label_9.setText(_translate("CrossCorrelationControls", "SampleID"))

from ....pyqtgraphCore import PlotWidget
