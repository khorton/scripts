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
        MainWindow.resize(1280, 800)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuSlide_Show = QtWidgets.QMenu(self.menubar)
        self.menuSlide_Show.setObjectName("menuSlide_Show")
        MainWindow.setMenuBar(self.menubar)
        self.actionDir = QtWidgets.QAction(MainWindow)
        self.actionDir.setShortcutVisibleInContextMenu(True)
        self.actionDir.setObjectName("actionDir")
        self.actionStart_Slide_Show = QtWidgets.QAction(MainWindow)
        self.actionStart_Slide_Show.setShortcutVisibleInContextMenu(True)
        self.actionStart_Slide_Show.setObjectName("actionStart_Slide_Show")
        self.actionRandom_Slide_Show = QtWidgets.QAction(MainWindow)
        self.actionRandom_Slide_Show.setShortcutVisibleInContextMenu(True)
        self.actionRandom_Slide_Show.setObjectName("actionRandom_Slide_Show")
        self.actionHelp_H = QtWidgets.QAction(MainWindow)
        self.actionHelp_H.setShortcutVisibleInContextMenu(True)
        self.actionHelp_H.setObjectName("actionHelp_H")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcutVisibleInContextMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionNext_Alpha = QtWidgets.QAction(MainWindow)
        self.actionNext_Alpha.setObjectName("actionNext_Alpha")
        self.actionPrev_Alpha = QtWidgets.QAction(MainWindow)
        self.actionPrev_Alpha.setObjectName("actionPrev_Alpha")
        self.actionNext_Random = QtWidgets.QAction(MainWindow)
        self.actionNext_Random.setObjectName("actionNext_Random")
        self.actionPrev_Random = QtWidgets.QAction(MainWindow)
        self.actionPrev_Random.setObjectName("actionPrev_Random")
        self.menuSlide_Show.addAction(self.actionDir)
        self.menuSlide_Show.addAction(self.actionStart_Slide_Show)
        self.menuSlide_Show.addAction(self.actionRandom_Slide_Show)
        self.menuSlide_Show.addSeparator()
        self.menuSlide_Show.addAction(self.actionNext_Alpha)
        self.menuSlide_Show.addAction(self.actionPrev_Alpha)
        self.menuSlide_Show.addSeparator()
        self.menuSlide_Show.addAction(self.actionNext_Random)
        self.menuSlide_Show.addAction(self.actionPrev_Random)
        self.menuSlide_Show.addSeparator()
        self.menuSlide_Show.addAction(self.actionQuit)
        self.menubar.addAction(self.menuSlide_Show.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuSlide_Show.setTitle(_translate("MainWindow", "Slide Show"))
        self.actionDir.setText(_translate("MainWindow", "Dir ..."))
        self.actionDir.setToolTip(_translate("MainWindow", "Select Image Directory"))
        self.actionDir.setShortcut(_translate("MainWindow", "D"))
        self.actionStart_Slide_Show.setText(_translate("MainWindow", "Start Slide Show"))
        self.actionStart_Slide_Show.setShortcut(_translate("MainWindow", "S"))
        self.actionRandom_Slide_Show.setText(_translate("MainWindow", "Random Slide Show"))
        self.actionRandom_Slide_Show.setShortcut(_translate("MainWindow", "R"))
        self.actionHelp_H.setText(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit Slide Show"))
        self.actionNext_Alpha.setText(_translate("MainWindow", "Next Alpha"))
        self.actionNext_Alpha.setShortcut(_translate("MainWindow", ">"))
        self.actionPrev_Alpha.setText(_translate("MainWindow", "Prev Alpha"))
        self.actionPrev_Alpha.setShortcut(_translate("MainWindow", "<"))
        self.actionNext_Random.setText(_translate("MainWindow", "Next Random"))
        self.actionNext_Random.setShortcut(_translate("MainWindow", "Shift+N"))
        self.actionPrev_Random.setText(_translate("MainWindow", "Prev Random"))
        self.actionPrev_Random.setShortcut(_translate("MainWindow", "Shift+P"))

