#!/opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys, os, random, fnmatch
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QGraphicsPixmapItem, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from slideShow3 import *
#from helpBox import *

#import ipdb; ipdb.set_trace()

helpText = """
Slide Show 

Dir = File Browser
"""
class MyForm(QMainWindow):
    def __init__(self, width, height, pixel_ratio, path):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.width = width
        self.height = height
        self.pixel_ratio = pixel_ratio
        self.path = path
        self.imageFiles = []
        self.slideIndex = -1
        self.random_index_number = 0
        self.random = ""
        self.imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2() 
        #self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)

        self.scene = QGraphicsScene(self)
        self.ui.actionDir.triggered.connect(self.openFileNameDialog)
        self.ui.actionStart_Slide_Show.triggered.connect(self.slide_show)
        self.ui.actionRandom_Slide_Show.triggered.connect(self.random_slide_show)
        #self.actionQuit_Q.triggered.connect(self.Quit())
        self.show()

    def openFileNameDialog(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.path = os.path.dirname(fileName)
            # print(dirName)
            # return(dirName)
            self.imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2()
            print(self.imageFiles)
    
        
    #def getImageNames2(self, path):
    def getImageNames2(self):
        "get the names of all images on disc or from the web (which are cached locally)"
        
        if not self.path:
            self.path = os.getcwd()
        if self.path[-1] != '/': 
            self.path += '/'
        # print "Path is:", path, "\n"
        try:
            os.listdir(self.path)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Error in path' +self.path) # https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5
            return [], self.path

        for i in GlobDirectoryWalker(self.path, "*.*"):
            # print i
            if os.path.isfile(i):
                # print "is file"
                # if self.checkImageType(p): imageFiles.append(p)
                if self.checkImageType(i): self.imageFiles.append(i)
            
        max_index = len(self.imageFiles) - 1
        # print "max_index = ", max_index

        self.imageFiles.sort()

        random_index = list(range(max_index + 1))
        # print "random_index = ", random_index
        random.shuffle(random_index)
        # print "imageFiles are:\n"
        # print imageFiles
        return self.imageFiles, random_index, self.path, max_index



    def slide(self, i):
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load(self.imageFiles[i])
        self.pixmap.setDevicePixelRatio(self.pixel_ratio) # https://stackoverflow.com/questions/50127246/pyqt-5-10-enabling-high-dpi-support-for-macos-poor-pixmap-quality
        self.pixmap4 = self.pixmap.scaled(self.width * self.pixel_ratio, (self.height * self.pixel_ratio)-60, Qt.KeepAspectRatio)
        try:
            self.scene.removeItem(self.item)
        except:
            print("failed to remove item")
        self.item = QGraphicsPixmapItem(self.pixmap4)
        self.scene.addItem(self.item)
        myapp.setWindowTitle(os.path.basename(self.imageFiles[i]))
        self.ui.graphicsView.setScene(self.scene)
        
    def slide_show(self):
        self.random = 0
        self.next_slide()
        
    def random_slide_show(self):
        self.random = 1
        self.next_slide()
    

    def next_slide(self):
        if self.random == 0:
            self.increment_slide()
        else:
            self.random_next()
            
    def prev_slide(self):
        if self.random == 0:
            self.decrement_slide()
        else:
            self.random_prev()
        
    def random_next(self):
        "display the next random slide"
        self.random_index_number += 1
        try:
            self.slideIndex = self.random_index[self.random_index_number]
            self.slide(self.slideIndex)
        except IndexError:
            self.random_index_number = 0
            self.slideIndex = self.random_index[self.random_index_number]
            self.slide(self.slideIndex)
        return False

    def random_prev(self):
        "display the previous random slide"
        self.random_index_number -= 1
        #self.ImageWindow.clear()
        try:
            self.slideIndex = self.random_index[self.random_index_number]
            self.slide(self.slideIndex)
        except IndexError:
            self.random_index_number = self.max_index
            self.slideIndex = self.random_index[self.random_index_number]
            self.slide(self.slideIndex)
        return False

    def increment_slide(self):
        "display a higher slide"  
        print("in increment_slide")   
        self.slideIndex += 1
        if self.slideIndex > self.max_index:
            self.slideIndex = 0
            print('Max index hit')
        self.slide(self.slideIndex)
        return False

    def decrement_slide(self):
        "display a lower slide"        
        self.slideIndex -= 1
        if self.slideIndex < 0:
            self.slideIndex = self.max_index
        self.slide(self.slideIndex)
        return False




    
    def checkImageType(self, f):
        "check to see if we have an file with an image extension"
        ext = self.extension(f)
        chk = [i for i in ['jpg','gif','ppm', 'tif', 'png', 'jpeg'] if i==ext]
        if chk == []: return False
        return True

    extension = staticmethod(lambda f: f.split('.').pop().lower())
    filename  = staticmethod(lambda f: f.split('/').pop())
    
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.Quit()
        if e.key() == Qt.Key_Q:
            self.Quit()
        if e.key() == Qt.Key_Space:
            self.i = self.next_slide()
        if e.key() == Qt.Key_N:
            self.i = self.random_next()
        if e.key() == Qt.Key_P:
            self.i = self.random_prev()
        if e.key() == Qt.Key_Comma:
            self.decrement_slide()
        if e.key() == Qt.Key_Period:
            self.increment_slide()
        if e.key() == Qt.Key_H:
            self.helpWindow = HelpText(helpText)
            #ipdb.pm()
        
        
        if e.key() == Qt.Key_BracketLeft:
            self.slideIndex = self.decrement_slide()
            
    def Quit(self):
        sys.exit(app.exec_())
    
class GlobDirectoryWalker:
    # a forward iterator that traverses a directory tree

    def __init__(self, directory, pattern="*"):
        self.stack = [directory]
        self.pattern = pattern
        self.files = []
        self.index = 0

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                if fnmatch.fnmatch(file, self.pattern):
                    return fullname

class HelpText(QDialog):
    def __init__(self, helpText):
        super().__init__()
        self.ui = Ui_Dialog(helpText)
        self.ui.setupUi(self)
        print(helpText)
        #self.setPlaceholderText(helpText)
        self.show()
        
    def Close(self):
        self.close()
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    pix_ratio = screen.devicePixelRatio()
    currentPath = os.getcwd()
    
    myapp = MyForm(rect.width(), rect.height(), pix_ratio, currentPath)
    myapp.show()
    sys.exit(app.exec_())