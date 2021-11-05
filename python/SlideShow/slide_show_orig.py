#! /opt/local/bin/python2.7

# MAX_SIZE = (1024, 768)
from Tkinter import *
import tkFileDialog, tkMessageBox
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter, ImageStat
# import urllib
import os
from os import mkdir, listdir
from math import sqrt


class PyImp(object):
    "A python image processing class using PIL"
    # def __init__(self, W=640, H=480, path='/Users/kwh/Pictures/'):
    def __init__(self, W=640, H=480, path=''):
        "intialise three panels - control, image window and info panel"
        self.W, self.H = W, H           # initial width & height of image window
        self.imagefiles, self.path = self.getImageNames(path)       # image filenames in current path
        self.filename = ''
        self.slideflag = False
        self.slideindex = 0
        self.thumbsize = (100,75)                   # thumbnail size
        self.thbuttons = []                         # thumbnail buttons
        self.thimages = []                          # thumbnail images
        self.control = Tk()                         # control panel for main buttons
        self.control.title('Control panel')
        self.imageWindow = Toplevel()               # image window to display the image
        self.imageWindow.protocol('WM_DELETE_WINDOW', self.userDelWin)  # can't delete the image window
        self.imageLabel = Label(self.imageWindow,anchor='nw')
        self.infoPanel = Toplevel(self.control)
        self.infoPanel.title('Information panel')
        self.infoPanel.protocol('WM_DELETE_WINDOW', self.userDelWin)    # can't delete the info panel
        self.thumbFrame = Frame(self.infoPanel,width=W, height=H)       # use this to hold thumbnails
        self.thumbFrame.pack() #grid(row=0)
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
        cachepath = './pyimpcache/'
        try:
            listdir(cachepath)
        except:                 # make sure we have a cache directory
            try:
                mkdir(cachepath)
            except: pass
        if not path: 
            path = cachepath
        elif path[:4] == 'http':
            if self.checkImageType(path):       # only download a single image file
                fn = self.downloadImageUrl(path,cachepath)
                if not fn: return []
                self.loadFile(cachepath+fn)
                return [fn]
            else:
                tkMessageBox.showerror('error','url is not an image')
                return [], path
        else:
            if path[-1] != '/': path += '/'
            try:
                listdir(path)
            except:
                tkMessageBox.showerror('error','error in path: '+path)
                return [], path
        imagefiles = []
        # print "path is:", path
        for i in listdir(path):
            p = os.path.normpath(os.path.join(path, i))
            # print p
            if os.path.isfile(p):
                # print "is file"
                # if self.checkImageType(p): imagefiles.append(p)
                if self.checkImageType(i): imagefiles.append(i)
        # print "in getImageNames().  Image files are:", imagefiles
        return imagefiles, path

    # initialisation, utility and termination functions 
    def checkImageType(self, f):
        "check to see if we have an file with an image extension"
        ext = self.extension(f)
        chk = [i for i in ['jpg','gif','ppm', 'tif'] if i==ext]
        if chk == []: return False
        return True
    
    def downloadImageUrl(self,url,cache):
        "download a file of type http://www.abc.com/xyz/image.jpg and save it into the local cache"
        cachedfiles = listdir(cache)
        fname = url.split('/').pop()
        if not [i for i in cachedfiles if i==fname]:    # check to see if its already in the cache
            try:
                image = urllib.urlopen(url).read()
            except:
                tkMessageBox.showerror('error','error in downloading '+url)
                return ''
            f = open(cache+fname,'wb')
            f.write(image)
            f.close()
        return fname
    
    def getWebImages(url,cache):
        pass

    def addWidgets(self):
        """add a series of widgets like buttons and checkboxes to the control panel
           widgets are described as tuples with a name and a callback function """
        i = 0
        # main buttons 
        buttons = [ ('quit',self.bye), ('load',self.load), ('thumbs',self.thumbs), 
                    ('next',self.next), ('slideshow',self.slideshow), ('dir/url',self.dirUrl)]
        for b, i in zip(buttons,range(1,len(buttons)+1)):
            Button(self.control, text=b[0], command= lambda x=b[1]:self.buttonHandler(x)).grid(row=i, sticky=W)
        self.entry = Entry(self.control, width=40)
        i += 1
        self.entry.grid(row=i,columnspan=3, sticky=W)
        self.entry.insert(0,self.path)

        # some popular image processing functions from the PIL implemented as checkbuttons      
        # imageops = [ ('autocontrast',ImageOps.autocontrast), ('resize -50%',self.resize),
        #            ('equalize',ImageOps.equalize), ('flip',ImageOps.flip),
        #            ('grayscale',ImageOps.grayscale), ('invert',ImageOps.invert), ('mirror',ImageOps.mirror), 
        #            ('solarize',ImageOps.solarize), ('posterize',lambda im: ImageOps.posterize(im,3)),
        #            ('sharpen',self.sharpen), 
        #            ('edge enhance',lambda im: im.filter(ImageFilter.EDGE_ENHANCE)), 
        #            ('edge enhance+',lambda im: im.filter(ImageFilter.EDGE_ENHANCE_MORE)), 
        #            ('find edges',lambda im: im.filter(ImageFilter.FIND_EDGES)) ]
        # checkbuttons = {} # dictionary lists containing nameKey:[checkValue #checkbuttonWidget functionReference]
        # for ops in imageops:
        #   k = ops[0] 
        #   checkbuttons[k] = [IntVar()]    # first 
        #   checkbuttons[k].append(Checkbutton(self.control, text=k, command=self.displayImage, 
        #                                      anchor='w',justify='left', variable=checkbuttons[k][0]))
        #   checkbuttons[k][1].var = checkbuttons[k][0]
        #   checkbuttons[k].append(ops[1])              # image processing function reference
        #   i += 1
        #   checkbuttons[k][1].grid(row=i, column=0, sticky=W)
        # self.checkbuttons = checkbuttons  

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
    def displayImage(self): 
        "display the current or processed image in the image window"
        # im = self.processImage(self.im)               # do the image processing 
        im = self.im                # no image processing 
        self.imagedata = ImageTk.PhotoImage(im)     # use PIL's PhotoImage to convert the image to Tk format
        self.imageLabel.destroy()
        self.imageLabel = Label(self.imageWindow,anchor='nw',image=self.imagedata)
        self.imageLabel.pack()
        self.imageLabel.focus_set()
        self.imageWindow.title(self.filename)

    #put button-related functions here e.g. for button callbacks
    
    def buttonHandler(self,cbfunc):
        "main handler for callback functions associated with buttons"
        if self.loopId is not None:                 # stop any background activity
            self.control.after_cancel(self.loopId)
        cbfunc()                                    # invoke callback
        
    def bye(self): 
        # self.infoPanel.destroy()     
        # self.imageWindow.destroy()
        # self.thumbFrame.destroy()
        self.control.destroy()    
        
    
    def thumbClick(self,filename):
        "open the selected thumbnail file"
        self.loadFile(self.path+filename)

    def load(self):
        "get a filename using a dialog box"
        dlg = Tk()
        dlg.withdraw()
        filename = tkFileDialog.askopenfilename(parent=self.control,title='Choose a file')
        if filename:
            try:
                self.loadFile(filename)
            except: pass    

    def loadFile(self,filename):
        "load an image file and display it"
        self.im = Image.open(filename)
        self.filename = filename.split('/').pop()
        self.displayImage()
    
    def thumbs(self):
        "load all image files as thumbnails in buttons which open the image when clicked"
        if not self.imagefiles: 
            print "no image files in thumbs()"
            print "path = ", self.path
            return
        if self.thbuttons: 
            for i in self.thbuttons: i.destroy()        # get rid of any previously defined thumbnail buttons
            self.thbuttons = []
            self.thimages = []
        tmpimg = Image.new('RGB',self.thumbsize)
        self.blankimg = ImageTk.PhotoImage(tmpimg)
        gridW, x, y = int(sqrt(len(self.imagefiles))) + 1, 0 , 0    
        for f in self.imagefiles:
            if len(f)>16: txt = f.split('.')[0][:14]+'...'+self.extension(f)
            else: txt=f     
            self.thbuttons.append(Button(self.thumbFrame, text=txt, image=self.blankimg, 
                                         compound=BOTTOM, command=lambda x=f: self.thumbClick(x)))
            self.thbuttons[-1].grid(row=x,column=y)
            y = (y+1)% gridW
            if y==0: x+=1   
        self.slideindex = 0
        self.startloop(1,self.loadThumbImage)

    def loadThumbImage(self):                       # timed looping function
        "load the thumbnail image in the background and show them as we go"
        i, f = self.slideindex, self.imagefiles[self.slideindex]
        if len(self.thimages) != len(self.imagefiles):
            thumb = Image.open(self.path+f).resize(self.thumbsize)
            # thumb = Image.open(f).resize(self.thumbsize)
            self.thimages.append(ImageTk.PhotoImage(thumb))
        x = self.thbuttons[i].grid_info()['row']
        y = self.thbuttons[i].grid_info()['column']         # remember button position
        self.thbuttons[i].destroy()
        if len(f)>16: txt = f.split('.')[0][:14]+'...'+self.extension(f)
        else: txt=f
        self.thbuttons[i] = Button(self.thumbFrame, text=txt, image=self.thimages[i],
                                   compound=BOTTOM, command=lambda x=f: self.thumbClick(x))
        self.thbuttons[i].image = self.thimages[-1]     
        self.thbuttons[i].grid(row=x,column=y)
        self.slideindex = (self.slideindex+1) % len(self.imagefiles)
        return self.slideindex == 0

    def next(self):
        "load and display the next image file in the sequence"
        if not self.imagefiles: return
        if not self.filename: self.filename = self.imagefiles[0]
        try:
            self.slideindex = self.imagefiles.index(self.filename)
        except:
            self.slideindex = 0
        self.slideindex = (self.slideindex+1) % len(self.imagefiles)        
        self.loadFile(self.path+self.imagefiles[self.slideindex])

    def slideshow(self):
        "setup the slideshow for all found images"
        if not self.imagefiles: return          # make sure we have some images to play with
        if not self.filename: self.filename = self.imagefiles[0]
        self.slideflag = not self.slideflag     # toggle the slideshow
        if self.slideflag: 
            try: 
                self.slideindex = self.imagefiles.index(self.filename)
            except:
                self.slideindex = 0 
            self.slidecount = len(self.imagefiles)
            self.startloop(1200,self.runslideshow) # self.runslideshow()

    def runslideshow(self):
        "run the slideshow continuously"        # timed looping function
        self.loadFile(self.path+self.imagefiles[self.slideindex])
        self.slideindex = (self.slideindex+1) % len(self.imagefiles)
        self.slidecount -= 1
        if self.slidecount == 0:
            self.slideflag = not self.slideflag
            return True
        return False

    def dirUrl(self):
        "load a new directory or a url that points to an image"
        # print "in dirURL"
        # path = self.entry.get()
        # if path == self.path: return 
        # self.imagefiles, self.path = self.getImageNames(path)
        # if not path: self.entry.insert(0,self.path)
        # if self.thbuttons: self.thumbs()  

        "get a directory name using a dialog box"
        dlg = Tk()
        dlg.withdraw()
        dirname = tkFileDialog.askdirectory(parent=self.control,title='Choose a directory')
        if dirname:
            # try:
            # print dirname
            path = dirname
            self.imagefiles, self.path = self.getImageNames(path)
            # print "image files are:", self.imagefiles
            return
                # self.loadFile(filename)
            # except: 
            #     print "failed try in dirUrl()"    
            
        else:
            print "no dirname"
            

        
    # do the predefined image processing functions
    # def processImage(self,img):
    #   "main image processing loop where the functions associated with checked boxes are performed"
    #   checkbuttons = self.checkbuttons
    #   for k in checkbuttons.keys():
    #       if checkbuttons[k][0].get():
    #           try:
    #               img = checkbuttons[k][2](img)   # invoke image processing function if selected
    #           except: pass                        # function requires more params - ignore these for now
    #   return img  

    # put our own image processing functions here ...
    # each function should input an image and output a processed image   
    def resize(self,im):
        imresize = (im.size[0]>>1, im.size[1]>>1)   # resize by  half
        return im.resize(imresize)

    def sharpen(self,im):
        sharpen = ImageEnhance.Sharpness(im)
        img = sharpen.enhance(4.0)
        return img


        
        
pyimpApp = PyImp() #(path='/Users/Jav/Pictures/nasa/')