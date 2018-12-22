#!/opt/local/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QFileDialog, QLabel)
from PyQt5.QtGui import QPixmap

#QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
#if hasattr(Qt, 'AA_EnableHighDpiScaling'):
#    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
# 
#if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
#    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class Example(QWidget):
    
    def __init__(self, w, h, r):
        super().__init__()
        #print('Available screen size: %d x %d @ pixel ratio %f' % (w,h,d))
        self.width = w
        self.height = h
        self.pixel_ratio = r
        
        self.initUI()
        
        
    def initUI(self):
        
        #w,h,r = self.GetScreenSize()
        #self.GetScreenSize()
        #print('Available: %d x %d @ %f' % (w, h, r))
 
        # self.statusBar().showMessage('Ready')
        SlideShowButton = QPushButton("Slide Show")
        RandomSlideShowButton = QPushButton("Random Slide Show")
        DirButton = QPushButton("Dir")
        QuitButton = QPushButton("Quit")

        RandomSlideShowButton.clicked.connect(self.SlideShow)
        DirButton.clicked.connect(self.openFileNameDialog)
        QuitButton.clicked.connect(self.Quit)

        vbox = QVBoxLayout()
        vbox.addWidget(SlideShowButton)
        vbox.addWidget(RandomSlideShowButton)
        vbox.addWidget(DirButton)
        vbox.addWidget(QuitButton)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        
        self.setLayout(hbox)    
        
        self.setGeometry(10, 10, 200, 120)
        #self.setWindowTitle('Statusbar') 
        self.setWindowTitle('Control Panel')
                
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        
    def SlideShow(self):
        self.next=Example2(self.width,self.height,self.pixel_ratio)

    def Quit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.Quit()
        if e.key() == Qt.Key_Q:
            self.Quit()

#    def GetScreenSize(self):
        
        # Get screen size
        # https://stackoverflow.com/questions/35887237/current-screen-size-in-python3-with-pyqt5
        #app = QApplication(sys.argv)
        #app = QApplication(self)
        #screen = app.primaryScreen()
        #print('Screen: %s' % screen.name())
        #size = screen.size()
        #print('Size: %d x %d' % (size.width(), size.height()))
        #rect = screen.availableGeometry()
        #pix_ratio = screen.devicePixelRatio()
        # return(rect.width(), rect.height(), pix_ratio)

class Example2(QWidget):
    
    def __init__(self, width, height, pixel_ratio):
        super().__init__()
        # print('Available screen size: %d x %d @ pixel ratio %f' % (width,height,pixel_ratio))
        self.width = width
        self.height = height
        self.pixel_ratio = pixel_ratio
        
        self.ImageWindow()
        
    def ImageWindow(self):
        # self.statusBar().showMessage('Ready')
        # SlideShowButton2 = QPushButton("Slide Show 2")
        # RandomSlideShowButton2 = QPushButton("Random Slide Show")
        # DirButton2 = QPushButton("Dir")
        # QuitButton2 = QPushButton("Quit")
        # 
        # vbox2 = QVBoxLayout()
        # vbox2.addWidget(SlideShowButton2)
        # vbox2.addWidget(RandomSlideShowButton2)
        # vbox2.addWidget(DirButton2)
        # vbox2.addWidget(QuitButton2)
        # vbox2.addStretch(1)
        # 
        # hbox2 = QHBoxLayout()
        # hbox2.addLayout(vbox2)
        # hbox2.addStretch(1)
        # 
        # self.setLayout(hbox2)    
        
        window = QLabel(self)
        image_path = '/Users/kwh/Pictures/CGNHK/IMG_0379.jpg'
        pixmap = QPixmap(image_path)
        pixmap.setDevicePixelRatio(self.pixel_ratio) # https://stackoverflow.com/questions/50127246/pyqt-5-10-enabling-high-dpi-support-for-macos-poor-pixmap-quality
        pixmap4 = pixmap.scaled(self.width * self.pixel_ratio, self.height * self.pixel_ratio, Qt.KeepAspectRatio)
        window.setPixmap(pixmap4)
        
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Image')    
        self.show()

    def Quit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Q:
            self.Quit()

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

    def getImageNames2(self,path):
        "get the names of all images on disc or from the web (which are cached locally)"
        if not path:
            path = os.getcwd()
        imagefiles = []
        if path[-1] != '/': 
            path += '/'
        # print "Path is:", path, "\n"
        try:
            listdir(path)
        except:
            #tkMessageBox.showerror('error','error in path: '+path)
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Error in path' +path) # https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5
            return [], path
        # print "path is:", path
        # for i in listdir(path):
        #     p = os.path.normpath(os.path.join(path, i))
        #     # print p
        #     if os.path.isfile(p):
        #         # print "is file"
        #         # if self.checkImageType(p): imagefiles.append(p)
        #         if self.checkImageType(i): imagefiles.append(i)
        # print "in getImageNames().  Image files are:", imagefiles
        # print "Path is:", path, "\n"
        for i in GlobDirectoryWalker(path, "*.*"):
            # print i
            if os.path.isfile(i):
                # print "is file"
                # if self.checkImageType(p): imagefiles.append(p)
                if self.checkImageType(i): imagefiles.append(i)
            
        max_index = len(imagefiles) - 1
        # print "max_index = ", max_index

        imagefiles.sort()

        random_index = range(max_index + 1)
        # print "random_index = ", random_index
        random.shuffle(random_index)
        # print "imagefiles are:\n"
        # print imagefiles
        return imagefiles, random_index, path, max_index





if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    pix_ratio = screen.devicePixelRatio()
    # print('Available: %d x %d @ %f' % (rect.width(), rect.height(), pix_ratio))
    
    ex = Example(rect.width(), rect.height(), pix_ratio)
    sys.exit(app.exec_())