# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/samu/PyPicMover/view_log.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 631)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setGeometry(QtCore.QRect(650, 0, 75, 23))
        self.btnClose.setObjectName("btnClose")
        self.img_view = QtWidgets.QLabel(Form)
        self.img_view.setGeometry(QtCore.QRect(20, 90, 681, 501))
        self.img_view.setText("")
        self.img_view.setObjectName("img_view")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 41, 16))
        self.label_2.setObjectName("label_2")
        self.select_src = QtWidgets.QPushButton(Form)
        self.select_src.setGeometry(QtCore.QRect(450, 20, 51, 21))
        self.select_src.setObjectName("select_src")
        self.img_source = QtWidgets.QPlainTextEdit(Form)
        self.img_source.setGeometry(QtCore.QRect(320, 20, 131, 21))
        self.img_source.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_source.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_source.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.img_source.setObjectName("img_source")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Stuff here..."))
        self.btnClose.setText(_translate("Form", "Close"))
        self.label_2.setText(_translate("Form", "Image:"))
        self.select_src.setText(_translate("Form", "Select"))
