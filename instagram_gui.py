# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instagram.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('InstaDown')
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 140))
        MainWindow.setMaximumSize(QtCore.QSize(400, 140))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 100))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 100))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 0, 171, 96))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setContentsMargins(0, 10, 0, 0)
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtPass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPass.setObjectName("txtPass")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.txtPass, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtUser = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtUser.setObjectName("txtUser")
        self.gridLayout.addWidget(self.txtUser, 0, 1, 1, 1)
        self.btnDownload = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDownload.setObjectName("btnDownload")
        self.gridLayout.addWidget(self.btnDownload, 3, 0, 1, 2)
        self.lblProgress = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblProgress.setText("")
        self.lblProgress.setObjectName("lblProgress")
        self.gridLayout.addWidget(self.lblProgress, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHola_mundo = QtWidgets.QAction(MainWindow)
        self.actionHola_mundo.setObjectName("actionHola_mundo")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("InstaDown", "InstaDown"))
        self.label.setText(_translate("MainWindow", "User"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.btnDownload.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

