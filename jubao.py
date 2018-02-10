# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jubao.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Rname = QtWidgets.QLineEdit(Dialog)
        self.Rname.setObjectName("Rname")
        self.gridLayout.addWidget(self.Rname, 0, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.content = QtWidgets.QTextEdit(Dialog)
        self.content.setObjectName("content")
        self.gridLayout.addWidget(self.content, 2, 1, 1, 3)
        self.sureButton = QtWidgets.QPushButton(Dialog)
        self.sureButton.setObjectName("sureButton")
        self.gridLayout.addWidget(self.sureButton, 3, 1, 1, 1)
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 3, 2, 1, 2)
        self.suspect = QtWidgets.QComboBox(Dialog)
        self.suspect.setObjectName("suspect")
        self.gridLayout.addWidget(self.suspect, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.backButton.clicked.connect(self.back)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "举报人："))
        self.radioButton.setText(_translate("Dialog", "匿名举报"))
        self.label_2.setText(_translate("Dialog", "嫌疑人："))
        self.label_3.setText(_translate("Dialog", "笔录："))
        self.sureButton.setText(_translate("Dialog", "确定"))
        self.backButton.setText(_translate("Dialog", "取消"))

