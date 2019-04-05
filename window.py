#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Window object, creates a tkinter window and stores it as self.Root          #
#                                                                             #
# Created April 3rd, 2019                                                     #
# Written by:                                                                 #
#   Braeden Richards                                                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                 Imports                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import tkinter as tk        # For window creation
from os import system       # For bringing window to front if on MacOs
from sys import platform    # For finding what os is running to bring window to
                            #    front


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# @Def: Window object for tkinter window creation and manipulation            #
# @Inherits: None                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Window():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: __init__ of Object                                                #
    # @Param: <Engine> engine: Engine containing all the managers             #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__(self, engine):
        self.Root = None        # Tkinter window root for this object
        self.width = None       # Width of window
        self.height = None      # Height of window
        self.name = None        # Name of this window (title)
        self.engine = engine    # Engine that this window is part of
        return

    def Initialize(self, w, h, name):
        self.width = w
        self.height = h
        self.name = name
        # Set size of window and set root
        self.Root = tk.Tk()
        self.Root.title(self.name)
        self.Root.geometry(str(self.width) + 'x' + str(self.height))
        # Position window in center of screen on open
        self.positionRight = int(self.Root.winfo_screenwidth()/2 - self.width/2)
        self.positionDown = int(self.Root.winfo_screenheight()/2 - self.height/2)
        self.Root.geometry("+{}+{}".format(self.positionRight, self .positionDown))
        # Don't let the window be resized
        self.Root.resizable(0, 0)

        # Bring the window to the front on open
        # If on Mac
        if platform == "darwin":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        # If on anything else
        else:
            self.Root.lift()
            self.Root.attributes('-topmost',True)
            self.Root.after_idle(self.Root.attributes,'-topmost',False)
        return
