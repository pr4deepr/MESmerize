# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './control_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControlsDock(object):
    def setupUi(self, ControlsDock):
        ControlsDock.setObjectName("ControlsDock")
        ControlsDock.resize(296, 672)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_data_column = ComboBox(self.dockWidgetContents)
        self.comboBox_data_column.setObjectName("comboBox_data_column")
        self.horizontalLayout.addWidget(self.comboBox_data_column)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.checkBoxIncludeUnlabelled = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBoxIncludeUnlabelled.setObjectName("checkBoxIncludeUnlabelled")
        self.verticalLayout_3.addWidget(self.checkBoxIncludeUnlabelled)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_method = ComboBox(self.dockWidgetContents)
        self.comboBox_method.setObjectName("comboBox_method")
        self.horizontalLayout_2.addWidget(self.comboBox_method)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_start_offset = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox_start_offset.setMinimum(-1000)
        self.spinBox_start_offset.setMaximum(1000)
        self.spinBox_start_offset.setObjectName("spinBox_start_offset")
        self.horizontalLayout_3.addWidget(self.spinBox_start_offset)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_end_offset = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox_end_offset.setMinimum(-1000)
        self.spinBox_end_offset.setMaximum(1000)
        self.spinBox_end_offset.setObjectName("spinBox_end_offset")
        self.horizontalLayout_4.addWidget(self.spinBox_end_offset)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_DPT_column = ComboBox(self.dockWidgetContents)
        self.comboBox_DPT_column.setObjectName("comboBox_DPT_column")
        self.horizontalLayout_5.addWidget(self.comboBox_DPT_column)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.pushButton_set = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_set.setObjectName("pushButton_set")
        self.verticalLayout_3.addWidget(self.pushButton_set)
        self.pushButton_save = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_3.addWidget(self.pushButton_save)
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.listWidget_samples = ListWidget(self.dockWidgetContents)
        self.listWidget_samples.setObjectName("listWidget_samples")
        self.verticalLayout_2.addWidget(self.listWidget_samples)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.listWidget_rois = ListWidget(self.dockWidgetContents)
        self.listWidget_rois.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listWidget_rois.setObjectName("listWidget_rois")
        self.verticalLayout.addWidget(self.listWidget_rois)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        ControlsDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(ControlsDock)
        QtCore.QMetaObject.connectSlotsByName(ControlsDock)
        ControlsDock.setTabOrder(self.comboBox_data_column, self.checkBoxIncludeUnlabelled)
        ControlsDock.setTabOrder(self.checkBoxIncludeUnlabelled, self.comboBox_method)
        ControlsDock.setTabOrder(self.comboBox_method, self.spinBox_start_offset)
        ControlsDock.setTabOrder(self.spinBox_start_offset, self.spinBox_end_offset)
        ControlsDock.setTabOrder(self.spinBox_end_offset, self.comboBox_DPT_column)
        ControlsDock.setTabOrder(self.comboBox_DPT_column, self.pushButton_set)
        ControlsDock.setTabOrder(self.pushButton_set, self.pushButton_save)
        ControlsDock.setTabOrder(self.pushButton_save, self.listWidget_samples)
        ControlsDock.setTabOrder(self.listWidget_samples, self.listWidget_rois)

    def retranslateUi(self, ControlsDock):
        _translate = QtCore.QCoreApplication.translate
        ControlsDock.setWindowTitle(_translate("ControlsDock", "Co&ntrols"))
        self.label.setText(_translate("ControlsDock", "data_column: "))
        self.comboBox_data_column.setToolTip(_translate("ControlsDock", "data column from which stimulus periods will be extracted"))
        self.checkBoxIncludeUnlabelled.setToolTip(_translate("ControlsDock", "If checked, any time periods that are not labelled with a stimulus will be considered as \"None\".\n"
"If unchecked, these unlabelled regions are ignored."))
        self.checkBoxIncludeUnlabelled.setText(_translate("ControlsDock", "Include unlabelled regions as \"None\""))
        self.label_2.setText(_translate("ControlsDock", "method: "))
        self.comboBox_method.setToolTip(_translate("ControlsDock", "method for creating the tuning curve"))
        self.label_3.setText(_translate("ControlsDock", "start offset:"))
        self.spinBox_start_offset.setToolTip(_translate("ControlsDock", "start offset"))
        self.label_4.setText(_translate("ControlsDock", "end offset:"))
        self.spinBox_end_offset.setToolTip(_translate("ControlsDock", "end offset"))
        self.label_5.setText(_translate("ControlsDock", "DPT column: "))
        self.comboBox_DPT_column.setToolTip(_translate("ControlsDock", "data to show in the datapoint tracer"))
        self.pushButton_set.setText(_translate("ControlsDock", "Set"))
        self.pushButton_save.setText(_translate("ControlsDock", "Save"))
        self.label_6.setText(_translate("ControlsDock", "Select Sample:"))
        self.label_7.setText(_translate("ControlsDock", "Select ROI:"))

from ....pyqtgraphCore.widgets.ComboBox import ComboBox
from ....pyqtgraphCore.widgets.ListWidget import ListWidget
