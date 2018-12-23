#!/opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from demoGraphicsView import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.i = 0
        self.files = ['/Users/kwh/Pictures/kwh_pics/KWH01_KP.jpg', '/Users/kwh/Pictures/kwh_pics/KWH01_KP_copy2.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_100.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_100_2.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_125.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_150.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_650.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_80.jpg', '/Users/kwh/Pictures/kwh_pics/KWH_80_2.jpg', '/Users/kwh/Pictures/kwh_pics/X.png']
        self.scene = QGraphicsScene(self)
        

   
    def slide(self, i):
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load(self.files[i])
        try:
            self.scene.removeItem(self.item)
        except:
            print("failed to remove item")
        self.item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
    
    def inc_slide(self, i):
        print("in inc_slide")
        i = i + 1
        if i > 9:
            i = 0
        print("i =", i)

        self.slide(i)   
        return i 
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.Quit()
        if e.key() == Qt.Key_Space:
            print("increment")
            self.i = self.inc_slide(self.i)
            
    def Quit(self):
        sys.exit(app.exec_())
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())