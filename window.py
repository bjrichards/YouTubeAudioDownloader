import tkinter as tk
# from tkinter import tk as tk
from os import system
from sys import platform

class Window():
    def __init__(self, engine):
        self.Root = None
        self.width = None
        self.height = None
        self.name = None
        self.engine = engine
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
        self.Root.geometry("+{}+{}".format(self.positionRight, self.positionDown))
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
