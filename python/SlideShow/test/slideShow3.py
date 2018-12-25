# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slideShow3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1280, 750))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuSlide_Show = QtWidgets.QMenu(self.menubar)
        self.menuSlide_Show.setObjectName("menuSlide_Show")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDir_D = QtWidgets.QAction(MainWindow)
        self.actionDir_D.setShortcutVisibleInContextMenu(True)
        self.actionDir_D.setObjectName("actionDir_D")
        self.actionStart_Slide_Show = QtWidgets.QAction(MainWindow)
        self.actionStart_Slide_Show.setShortcutVisibleInContextMenu(True)
        self.actionStart_Slide_Show.setObjectName("actionStart_Slide_Show")
        self.actionRandom_Slide_Show_R = QtWidgets.QAction(MainWindow)
        self.actionRandom_Slide_Show_R.setShortcutVisibleInContextMenu(True)
        self.actionRandom_Slide_Show_R.setObjectName("actionRandom_Slide_Show_R")
        self.actionHelp_H = QtWidgets.QAction(MainWindow)
        self.actionHelp_H.setShortcutVisibleInContextMenu(True)
        self.actionHelp_H.setObjectName("actionHelp_H")
        self.actionQuit_Q = QtWidgets.QAction(MainWindow)
        self.actionQuit_Q.setShortcutVisibleInContextMenu(True)
        self.actionQuit_Q.setObjectName("actionQuit_Q")
        self.menuSlide_Show.addAction(self.actionHelp_H)
        self.menuSlide_Show.addAction(self.actionDir_D)
        self.menuSlide_Show.addAction(self.actionStart_Slide_Show)
        self.menuSlide_Show.addAction(self.actionRandom_Slide_Show_R)
        self.menuSlide_Show.addAction(self.actionQuit_Q)
        self.menubar.addAction(self.menuSlide_Show.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSlide_Show.setTitle(_translate("MainWindow", "Slide Show"))
        self.actionDir_D.setText(_translate("MainWindow", "&Dir ..."))
        self.actionDir_D.setToolTip(_translate("MainWindow", "Select Image Directory"))
        self.actionStart_Slide_Show.setText(_translate("MainWindow", "&Start Slide Show"))
        self.actionRandom_Slide_Show_R.setText(_translate("MainWindow", "&Random Slide Show"))
        self.actionRandom_Slide_Show_R.setShortcut(_translate("MainWindow", "R"))
        self.actionHelp_H.setText(_translate("MainWindow", "&Help"))
        self.actionQuit_Q.setText(_translate("MainWindow", "&Quit Slide Show"))

