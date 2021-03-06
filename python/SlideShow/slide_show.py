#! /sw/bin/python2.7

from Tkinter import *
import tkFileDialog, tkMessageBox
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter, ImageStat
# import urllib
import os
from os import mkdir, listdir
from math import sqrt
import sys
import random
import platform
import fnmatch

# if platform.system() == 'Darwin':
#     import Carbon.File as CF
#     PLATFORM = 'OSX'

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



class PyImp(object):
    "A python image processing class using PIL"
    # def __init__(self, W=640, H=480, path='/Users/kwh/Pictures/'):
    def __init__(self, W=640, H=480, path=''):
        "intialise three panels - control, image window and info panel"
        self.W, self.H = W, H           # initial width & height of image window
        # if sys.platform == 'linux2':
        #     self.max_w, self.max_h = 1000, 565
        # else:
        #     self.max_w, self.max_h = 1000, 720
        self.imagefiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)       # image filenames in current path
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
        self.thumbsize = (100,75)                   # thumbnail size
        self.thbuttons = []                         # thumbnail buttons
        self.thimages = []                          # thumbnail images
        self.control = Tk()                         # control panel for main buttons
        self.max_w = self.control.winfo_screenwidth() - 6
        self.max_h = self.control.winfo_screenheight() - 38
        print "screen size = %i x %i" % (self.max_w, self.max_h)
        self.control.title('Control panel')
        self.imageWindow = Toplevel()               # image window to display the image
        self.imageWindow.protocol('WM_DELETE_WINDOW', self.userDelWin)  # can't delete the image window
        self.imageLabel = Label(self.imageWindow,anchor='nw')
#        self.infoPanel = Toplevel(self.control)
#        self.infoPanel.title('Information panel')
#        self.infoPanel.protocol('WM_DELETE_WINDOW', self.userDelWin)    # can't delete the info panel
#        self.thumbFrame = Frame(self.infoPanel,width=W, height=H)       # use this to hold thumbnails
#        self.thumbFrame.pack() #grid(row=0)
        #self.infoFrame = Frame(self.infoPanel)     # use this to hold info about the current image
        self.im = Image.new('RGB',(W,H)) # create a blank image
        self.addWidgets()       # add widgets: buttons &  checkboxes    
        self.displayImage()   
        self.loopId = None
        self.control.mainloop()


    extension = staticmethod(lambda f: f.split('.').pop().lower())
    filename  = staticmethod(lambda f: f.split('/').pop())

    def getImageNames(self,path):
        "get the names of all images on disc or from the web (which are cached locally)"
        if not path:
            path = os.getcwd()
        imagefiles = []
        if path[-1] != '/': 
            path += '/'
        try:
            listdir(path)
        except:
            tkMessageBox.showerror('error','error in path: '+path)
            return [], path
        # print "path is:", path
        for i in listdir(path):
            p = os.path.normpath(os.path.join(path, i))
            # print p
            if os.path.isfile(p):
                # print "is file"
                # if self.checkImageType(p): imagefiles.append(p)
                if self.checkImageType(i): imagefiles.append(i)
        # print "in getImageNames().  Image files are:", imagefiles

        
        max_index = len(imagefiles) - 1
        # print "max_index = ", max_index
        
        imagefiles.sort()
        
        random_index = range(max_index + 1)
        # print "random_index = ", random_index
        random.shuffle(random_index)
        return imagefiles, random_index, path, max_index

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
            tkMessageBox.showerror('error','error in path: '+path)
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


    # initialisation, utility and termination functions 
    def checkImageType(self, f):
        "check to see if we have an file with an image extension"
        ext = self.extension(f)
        chk = [i for i in ['jpg','gif','ppm', 'tif'] if i==ext]
        if chk == []: return False
        return True
    
    def addWidgets(self):
        """add a series of widgets like buttons and checkboxes to the control panel
           widgets are described as tuples with a name and a callback function """
        i = 0
        # main buttons 
        #buttons = [ ('quit',self.bye), ('slideshow',self.slideshow), ('dir/url',self.dirUrl)]
        buttons = [ ('Slideshow',self.slideshow), ('Random Slideshow',self.random), ('Dir/URL',self.dirUrl), ('Quit',self.bye)]
        for b, i in zip(buttons,range(1,len(buttons)+1)):
            Button(self.control, text=b[0], command= lambda x=b[1]:self.buttonHandler(x)).grid(row=i, sticky=W)
        self.entry = Entry(self.control, width=40)
        i += 1
        self.entry.grid(row=i,columnspan=3, sticky=W)
        self.entry.insert(0,self.path)
        self.control.bind('<q>', self.press_q)
        self.control.bind('<s>', self.press_s)
#         self.control.bind('<Button-1>', self.press_mouse)

    def userDelWin(self): pass                  # don't allow user to delete the image window

    # helper functions to manage periodic looping. The loopng function has to return a True when is has finished, otherwise False
    def startloop(self,delay,loopfunction):
        "periodic looping function for loading things in the background or a slideshow"
        self.delay, self.loopfunction = delay, loopfunction
        if self.loopId is not None:                 # stop any other loops that are running
            self.control.after_cancel(self.loopId)
        if self.loopfunction() == False:
            self.control.after(self.delay,self.runloop)

    def runloop(self):
        "the the looping function, terminates when the looping function returns a True"
        if self.loopfunction() == False:
            self.loopId = self.control.after(self.delay,self.runloop)

    # main image display
    def displayImage(self, filename=""): 
        "display the current or processed image in the image window"
        # im = self.processImage(self.im)               # do the image processing 
        im = self.im                # no image processing 
        try:
            self.imagedata = ImageTk.PhotoImage(im)     # use PIL's PhotoImage to convert the image to Tk format
        except:
            print "unable to convert image:", filename
        self.imageLabel.destroy()
        self.imageLabel = Label(self.imageWindow,anchor='nw',image=self.imagedata)
        self.imageLabel.pack()
        self.imageLabel.focus_set()
        try:
            filename = os.path.basename(filename)
        except:
            pass
        self.imageWindow.title(filename)
        self.imageWindow.bind('<q>', self.press_q)
        self.imageWindow.bind('<Escape>', self.press_q)
        self.imageWindow.bind('<n>', self.press_n)
        self.imageWindow.bind('<p>', self.press_p)
        self.imageWindow.bind('<m>', self.press_m)
        self.imageWindow.bind('<space>', self.press_space)
        self.imageWindow.bind('<Right>', self.press_right_arrow)
        self.imageWindow.bind('<Left>', self.press_left_arrow)

        self.imageWindow.bind('<Button-1>', self.press_mouse)

    #put button-related functions here e.g. for button callbacks
    
    def buttonHandler(self,cbfunc):
        "main handler for callback functions associated with buttons"
        if self.loopId is not None:                 # stop any background activity
            self.control.after_cancel(self.loopId)
        cbfunc()                                    # invoke callback
        
    def bye(self): 
        self.control.quit()
    
    def load(self):
        "get a filename using a dialog box"
        dlg = Tk()
        dlg.withdraw()
        filename = tkFileDialog.askopenfilename(parent=self.control,title='Choose a file', filetypes=[("allfiles","*"),("jpegs","*.jpg")])
        if filename:
            try:
                self.loadFile(filename)
            except: pass    
    
    def loadFile(self, filename):
        "load an image file and display it"
        print "In loadFile, and filename is:", filename, "\n"
        try:
            self.im = Image.open(filename)
        except:
            # need to resolve alias
            if PLATFORM == 'OSX':
                fss = CF.FSSpec(filename)
                try:
                    fss, isFolder, aliased = CF.ResolveAliasFile(fss,0)
                except:
                    print "File not found: ", filename
                    return
                fsr = CF.FSRef(fss)
                filename = fsr.FSRefMakePath()
                self.im = Image.open(filename)
        if self.im.size[0] > self.max_w:
            self.im = self.resize(self.im)
        if self.im.size[1] > self.max_h:
            self.im = self.resize(self.im)
        print filename
        self.displayImage(filename)
    
    def slideshow(self, r=False):
        "setup the slideshow for all found images"
        print "in slideshow, r=", r
        if not self.imagefiles: 
            return          # make sure we have some images to play with
#         if not self.filename: 
#              self.filename = self.imagefiles[random.randrange(self.max_index)]
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
        self.loadFile(self.imagefiles[self.slideindex])
        return False

    def random_next(self):
        "display the next random slide"
        self.random_index_number += 1
        try:
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imagefiles[self.slideindex])
        except IndexError:
            self.random_index_number = 0
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imagefiles[self.slideindex])
        return False

    def random_prev(self):
        "display the previous random slide"
        self.random_index_number -= 1
        try:
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imagefiles[self.slideindex])
        except IndexError:
            self.random_index_number = self.max_index
            self.slideindex = self.random_index[self.random_index_number]
            self.loadFile(self.imagefiles[self.slideindex])
        return False

    def increment_slide(self):
        "display a higher slide"  
        #print "in increment_slide"      
        self.slideindex += 1
        if self.slideindex > self.max_index:
            self.slideindex = 0
        self.loadFile(self.imagefiles[self.slideindex])
        return False

    def decrement_slide(self):
        "display a lower slide"        
        self.slideindex -= 1
        if self.slideindex < 0:
            self.slideindex = self.max_index
        self.loadFile(self.imagefiles[self.slideindex])
        return False

    def dirUrl(self):
        "get a directory name using a dialog box.  Return the directory + the list of images in it."
        dlg = Tk()
        dlg.withdraw()
        dirname = tkFileDialog.askdirectory(parent=self.control,title='Choose a directory')
        if dirname:
            # try:
            # print dirname
            path = dirname
            self.imagefiles, self.random_index, self.path, self.max_index = self.getImageNames2(path)
            random.seed()
            # print "image files are:", self.imagefiles
            self.entry.delete(0, END)
            
            self.entry.insert(0,self.path)
            
            return
        else:
            print "no dirname"
            

        
    # put our own image processing functions here ...
    # each function should input an image and output a processed image   
    def resize(self,im):
        new_w = im.size[0] * self.max_h / im.size[1]
#         print "new width =", new_w
        new_h = self.max_h
#         print "initial height =", new_h
        
        if new_w > self.max_w:
            new_w = self.max_w
            new_h = im.size[1] * self.max_w / im.size[0]
#         print "resizing image to size (%i, %i)" % (new_w, new_h)
        return im.resize((new_w, new_h))

    def mark_pic(self):
#         self.mark_file.write(self.imagefiles[self.slideindex])
        self.mark_file.write(self.imagefiles[self.slideindex])
        self.mark_file.write('\n')
    
    def press_q(self, event):
        self.bye()

    def press_s(self, event):
        self.slideshow(r=True)

    def press_space(self, event):
        if self.r == True:
            self.random_next()
        else:
            self.increment_slide()

    def press_right_arrow(self, event):
        self.increment_slide()

    def press_left_arrow(self, event):
        self.decrement_slide()
    
    def press_n(self, event):
        if self.r == True:
            self.random_next()
        else:
            self.increment_slide()

    def press_p(self, event):
        if self.r == True:
            self.random_prev()
        else:
            self.decrement_slide()
    
    def press_m(self, event):
        self.mark_pic()
    
    def press_mouse(self, event):
        self.press_space(event)
        
        
pyimpApp = PyImp() #(path='/Users/Jav/Pictures/nasa/')
