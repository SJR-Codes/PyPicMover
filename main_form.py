# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 603)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.source_folder = QtWidgets.QPlainTextEdit(Form)
        self.source_folder.setGeometry(QtCore.QRect(130, 50, 131, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_folder.sizePolicy().hasHeightForWidth())
        self.source_folder.setSizePolicy(sizePolicy)
        self.source_folder.setObjectName("source_folder")
        self.dest_folder = QtWidgets.QPlainTextEdit(Form)
        self.dest_folder.setGeometry(QtCore.QRect(420, 50, 131, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dest_folder.sizePolicy().hasHeightForWidth())
        self.dest_folder.setSizePolicy(sizePolicy)
        self.dest_folder.setObjectName("dest_folder")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 31, 16))
        self.label_3.setObjectName("label_3")
        self.select_src = QtWidgets.QPushButton(Form)
        self.select_src.setGeometry(QtCore.QRect(260, 50, 51, 28))
        self.select_src.setObjectName("select_src")
        self.select_dst = QtWidgets.QPushButton(Form)
        self.select_dst.setGeometry(QtCore.QRect(550, 50, 51, 28))
        self.select_dst.setObjectName("select_dst")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(337, 50, 31, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PyPicMover"))
        self.label_2.setText(_translate("Form", "Source"))
        self.label_3.setText(_translate("Form", "Dest"))
        self.select_src.setText(_translate("Form", "Select"))
        self.select_dst.setText(_translate("Form", "Select"))
        self.label_4.setText(_translate("Form", "--->"))
