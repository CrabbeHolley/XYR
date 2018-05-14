# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiji.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 462)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.mapWidget = QtWebEngineWidgets.QWebEngineView(Form)
        self.mapWidget.setObjectName("mapWidget")
        url = 'http://localhost:8000/'  # 修改
        self.mapWidget.setUrl(QtCore.QUrl(url))
        self.verticalLayout.addWidget(self.mapWidget)
        self.information = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMaximumSize(QtCore.QSize(16777215, 70))
        self.information.setReadOnly(True)
        self.information.setObjectName("information")
        self.verticalLayout.addWidget(self.information)
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)

        self.retranslateUi(Form)
        self.backButton.clicked.connect(self.back)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "嫌疑人轨迹查询"))
        self.label_5.setText(_translate("Form", "嫌疑人轨迹查询"))
        self.backButton.setText(_translate("Form", "确定并返回"))

