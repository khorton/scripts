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
import os
import platform
import fnmatch
import random


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QFileDialog, QLabel)
from PyQt5.QtGui import QPixmap

class ControlPanel(QWidget):
    
    def __init__(self, w, h, r):
        super().__init__()
        self.width = w
        self.height = h
        self.pixel_ratio = r
        
        self.initUI()
        
    def initUI(self):
        global imageFiles
        imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)       # image filenames in current path
        try:
            self.mark_file = open('/home/kwh/temp/mark_file.txt', 'w')
        except IOError:
            try:
                self.mark_file = open('/Users/test3/mark_file.txt', 'w')
            except IOError:
                self.mark_file = open('/Users/kwh/temp/mark_file.txt', 'w')
        self.filename = ''
        self.slideflag = False
        self.slideindex = 0
        self.max_w = self.width - 6
        self.max_h = self.height - 38
 
        # self.statusBar().showMessage('Ready')
        SlideShowButton = QPushButton("Slide Show")
        RandomSlideShowButton = QPushButton("Random Slide Show")
        DirButton = QPushButton("Dir")
        QuitButton = QPushButton("Quit")

        RandomSlideShowButton.clicked.connect(self.SlideShow)
        dirName = DirButton.clicked.connect(self.openFileNameDialog)
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
        global imageFiles
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.dirName = os.path.dirname(fileName)
            # print(dirName)
            # return(dirName)
            imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2(self.dirName)
            print(imageFiles)
        
    def SlideShow(self):
        print(imageFiles)
        self.next=SlideShowWindow(self.width,self.height,self.pixel_ratio,imageFiles)

    def Quit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.Quit()
        if e.key() == Qt.Key_Q:
            self.Quit()

        imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)       # image filenames in current path
        try:
            self.mark_file = open('/home/kwh/temp/mark_file.txt', 'w')
        except IOError:
            try:
                self.mark_file = open('/Users/test3/mark_file.txt', 'w')
            except IOError:
                self.mark_file = open('/Users/kwh/temp/mark_file.txt', 'w')
        app = QApplication(sys.argv)
        screen = app.primaryScreen()
        size = screen.size()
        rect = screen.availableGeometry()
        pix_ratio = screen.devicePixelRatio()
        
        cp = ControlPanel(rect.width(), rect.height(), pix_ratio)
        
    extension = staticmethod(lambda f: f.split('.').pop().lower())
    filename  = staticmethod(lambda f: f.split('/').pop())

    def getImageNames2(self,path):
        "get the names of all images on disc or from the web (which are cached locally)"
        global imageFiles
        
        if not path:
            path = os.getcwd()
        imageFiles = []
        if path[-1] != '/': 
            path += '/'
        # print "Path is:", path, "\n"
        try:
            os.listdir(path)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Error in path' +path) # https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5
            return [], path

        for i in GlobDirectoryWalker(path, "*.*"):
            # print i
            if os.path.isfile(i):
                # print "is file"
                # if self.checkImageType(p): imageFiles.append(p)
                if self.checkImageType(i): imageFiles.append(i)
            
        max_index = len(imageFiles) - 1
        # print "max_index = ", max_index

        imageFiles.sort()

        random_index = list(range(max_index + 1))
        # print "random_index = ", random_index
        random.shuffle(random_index)
        # print "imageFiles are:\n"
        # print imageFiles
        return imageFiles, random_index, path, max_index

    def dirUrl(self):
        "get a directory name using a dialog box.  Return the directory + the list of images in it."
        dlg = Tk()
        dlg.withdraw()
        dirname = tkFileDialog.askdirectory(parent=self.control,title='Choose a directory')
        if dirname:
            # try:
            # print dirname
            path = dirname
            self.imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)
            random.seed()
            # print "image files are:", self.imageFiles
            self.entry.delete(0, END)
            
            self.entry.insert(0,self.path)
            
            return
        else:
            print("no dirname")

    def checkImageType(self, f):
        "check to see if we have an file with an image extension"
        ext = self.extension(f)
        chk = [i for i in ['jpg','gif','ppm', 'tif'] if i==ext]
        if chk == []: return False
        return True

    def slideshow(self, r=False):
        "setup the slideshow for all found images"
        print("in slideshow, r=", r)
        if not self.imageFiles: 
            return          # make sure we have some images to play with
#         if not self.filename: 
#              self.filename = self.imageFiles[random.randrange(self.max_index)]
        if r == True:
            self.r = True
            self.random_index_number = 0
            self.slideindex = self.random_index[self.random_index_number]
            self.random_slide()
        else:
            self.r = False
            self.slideindex = -1
            #self.random_index_number = 0
            self.increment_slide()

    def random(self):
        self.slideshow(r=True)

    def random_slide(self):
        "display a random slide"
        self.random_index_number += 1
        self.slideindex = self.random_index[self.random_index_number]
#         self.slideindex = random.randrange(self.max_index)
        self.loadFile(self.imageFiles[self.slideindex])
        return False

    def random_next(self):
        "display the next random slide"
        self.random_index_number += 1
        try:
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imageFiles[self.slideindex])
        except IndexError:
            self.random_index_number = 0
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imageFiles[self.slideindex])
        return False

    def random_prev(self):
        "display the previous random slide"
        self.random_index_number -= 1
        try:
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imageFiles[self.slideindex])
        except IndexError:
            self.random_index_number = self.max_index
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imageFiles[self.slideindex])
        return False

    def increment_slide(self):
        "display a higher slide"  
        #print "in increment_slide"      
        self.slideindex += 1
        if self.slideindex > self.max_index:
            self.slideindex = 0
        self.loadFile(self.imageFiles[self.slideindex])
        return False

    def decrement_slide(self):
        "display a lower slide"        
        self.slideindex -= 1
        if self.slideindex < 0:
            self.slideindex = self.max_index
        self.loadFile(self.imageFiles[self.slideindex])
        return False


class SlideShowWindow(QWidget):
    
    def __init__(self, width, height, pixel_ratio, imageFiles):
        super().__init__()
        # print('Available screen size: %d x %d @ pixel ratio %f' % (width,height,pixel_ratio))
        self.width = width
        self.height = height
        self.pixel_ratio = pixel_ratio
        print("Image File = ", imageFiles[0])
        self.ImageWindow(imageFiles[0])
        
    def ImageWindow(self, image_path):
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
        #image_path = '/Users/kwh/Pictures/CGNHK/IMG_0379.jpg'
        pixmap = QPixmap(image_path)
        pixmap.setDevicePixelRatio(self.pixel_ratio) # https://stackoverflow.com/questions/50127246/pyqt-5-10-enabling-high-dpi-support-for-macos-poor-pixmap-quality
        pixmap4 = pixmap.scaled(self.width * self.pixel_ratio, self.height * self.pixel_ratio, Qt.KeepAspectRatio)
        window.setPixmap(pixmap4)
        
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle(os.path.basename(image_path))    
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


#class PyImp(QApplication):
#    "A python image processing class using PIL"
#    # def __init__(self, W=640, H=480, path='/Users/kwh/Pictures/'):
#    def __init__(self, W=640, H=480, path='/Users/kwh/Pictures/'):
#        super().__init__()
#        
#        "intialise three panels - control, image window and info panel"
#        #self.W, self.H = W, H           # initial width & height of image window
#        self.imageFiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)       # image filenames in current path
#        try:
#            self.mark_file = open('/home/kwh/temp/mark_file.txt', 'w')
#        except IOError:
#            try:
#                self.mark_file = open('/Users/test3/mark_file.txt', 'w')
#            except IOError:
#                self.mark_file = open('/Users/kwh/temp/mark_file.txt', 'w')
#        app = QApplication(sys.argv)
#        screen = app.primaryScreen()
#        size = screen.size()
#        rect = screen.availableGeometry()
#        pix_ratio = screen.devicePixelRatio()
#        
#        ex = ControlPanel(rect.width(), rect.height(), pix_ratio)
#        
#    extension = staticmethod(lambda f: f.split('.').pop().lower())
#    filename  = staticmethod(lambda f: f.split('/').pop())
#
#    def getImageNames2(self,path):
#        "get the names of all images on disc or from the web (which are cached locally)"
#        if not path:
#            path = os.getcwd()
#        imageFiles = []
#        if path[-1] != '/': 
#            path += '/'
#        # print "Path is:", path, "\n"
#        try:
#            os.listdir(path)
#        except:
#            #tkMessageBox.showerror('error','error in path: '+path)
#            error_dialog = QtWidgets.QErrorMessage()
#            error_dialog.showMessage('Error in path' +path) # https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5
#            return [], path
#        # print "path is:", path
#        # for i in listdir(path):
#        #     p = os.path.normpath(os.path.join(path, i))
#        #     # print p
#        #     if os.path.isfile(p):
#        #         # print "is file"
#        #         # if self.checkImageType(p): imageFiles.append(p)
#        #         if self.checkImageType(i): imageFiles.append(i)
#        # print "in getImageNames().  Image files are:", imageFiles
#        # print "Path is:", path, "\n"
#        for i in GlobDirectoryWalker(path, "*.*"):
#            # print i
#            if os.path.isfile(i):
#                # print "is file"
#                # if self.checkImageType(p): imageFiles.append(p)
#                if self.checkImageType(i): imageFiles.append(i)
#            
#        max_index = len(imageFiles) - 1
#        # print "max_index = ", max_index
#
#        imageFiles.sort()
#
#        random_index = list(range(max_index + 1))
#        # print "random_index = ", random_index
#        random.shuffle(random_index)
#        # print "imageFiles are:\n"
#        # print imageFiles
#        return imageFiles, random_index, path, max_index
#
#    def checkImageType(self, f):
#        "check to see if we have an file with an image extension"
#        ext = self.extension(f)
#        chk = [i for i in ['jpg','gif','ppm', 'tif'] if i==ext]
#        if chk == []: return False
#        return True
#
#    def slideshow(self, r=False):
#        "setup the slideshow for all found images"
#        print("in slideshow, r=", r)
#        if not self.imageFiles: 
#            return          # make sure we have some images to play with
##         if not self.filename: 
##              self.filename = self.imageFiles[random.randrange(self.max_index)]
#        if r == True:
#            self.r = True
#            self.random_index_number = 0
#            self.slideindex = self.random_index[self.random_index_number]
#            self.random_slide()
#        else:
#            self.r = False
#            self.slideindex = -1
#            #self.random_index_number = 0
#            self.increment_slide()
#
#    def random(self):
#        self.slideshow(r=True)
#
#    def random_slide(self):
#        "display a random slide"
#        self.random_index_number += 1
#        self.slideindex = self.random_index[self.random_index_number]
##         self.slideindex = random.randrange(self.max_index)
#        self.loadFile(self.imageFiles[self.slideindex])
#        return False
#
#    def random_next(self):
#        "display the next random slide"
#        self.random_index_number += 1
#        try:
#            self.slideindex = self.random_index[self.random_index_number]
#            self.loadFile(self.imageFiles[self.slideindex])
#        except IndexError:
#            self.random_index_number = 0
#            self.slideindex = self.random_index[self.random_index_number]
#            self.loadFile(self.imageFiles[self.slideindex])
#        return False
#
#    def random_prev(self):
#        "display the previous random slide"
#        self.random_index_number -= 1
#        try:
#            self.slideindex = self.random_index[self.random_index_number]
#            self.loadFile(self.imageFiles[self.slideindex])
#        except IndexError:
#            self.random_index_number = self.max_index
#            self.slideindex = self.random_index[self.random_index_number]
#            self.loadFile(self.imageFiles[self.slideindex])
#        return False
#
#    def increment_slide(self):
#        "display a higher slide"  
#        #print "in increment_slide"      
#        self.slideindex += 1
#        if self.slideindex > self.max_index:
#            self.slideindex = 0
#        self.loadFile(self.imageFiles[self.slideindex])
#        return False
#
#    def decrement_slide(self):
#        "display a lower slide"        
#        self.slideindex -= 1
#        if self.slideindex < 0:
#            self.slideindex = self.max_index
#        self.loadFile(self.imageFiles[self.slideindex])
#        return False


if __name__ == '__main__':
    
    path='/Users/kwh/Pictures/CGNHK'
    imageFiles = ['/Users/kwh/Pictures/CGNHK/IMG_0379.jpg']
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    pix_ratio = screen.devicePixelRatio()
    # print('Available: %d x %d @ %f' % (rect.width(), rect.height(), pix_ratio))
    
    
    panel = ControlPanel(rect.width(), rect.height(), pix_ratio)
    sys.exit(app.exec_())
