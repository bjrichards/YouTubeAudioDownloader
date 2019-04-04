#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Graphics Manager for application. Creates the window and controls tkinter's #
#       canvas and packs                                                      #
#                                                                             #
# Created April 3rd, 2019                                                     #
# Written by:                                                                 #
#   Braeden Richards                                                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                 Imports                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import window as Wn     # To create a window

# Specific imports from tkinter
from tkinter import X, W, LEFT, BOTH, RAISED, RIGHT, Radiobutton
from tkinter.ttk import Frame, Button, Style, Label, Entry

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# @Def: Graphics Manager for whole application                                #
# @Inherits: None                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class GfxMgr():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: __init__ of Object                                                #
    # @Param: <Engine> engine: Engine containing all the managers             #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__(self, engine):
        self.width = None           # Width of window to be created
        self.height = None          # Height of window to be created
        self.name = None            # Title of window to be created
        self.window = None          # Window object
        self.engine = engine        # Engine that this mgr is part of
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Initializes variables of the GfxMgr                               #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Initialize(self, name, width, height):
        self.width = width
        self.height = height
        self.name = name
        self.window = Wn.Window(self.engine)
        self.window.Initialize(self.width, self.height, self.name)

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Creates the UI of the main window of application                  #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Init_UI(self):
        # Radio button options
        self.export_types = [
        ("mp3"),
        ]

        # Text box for save file name
        self.frame1 = Frame(self.window.Root)
        self.frame1.pack(fill=X)
        self.label1 = Label(self.frame1, text="Save as: ", width = 6)
        self.label1.pack(side=LEFT, padx=5, pady=5)
        self.save_name = Entry(self.frame1)
        self.save_name.pack(fill=X, padx=5, expand=True)

        # Text box for url to grab from
        self.frame2 = Frame(self.window.Root)
        self.frame2.pack(fill=X)
        self.label2 = Label(self.frame2, text="Url: ", width = 6)
        self.label2.pack(side=LEFT, padx=5, pady=5)
        self.url_entry = Entry(self.frame2)
        self.url_entry.pack(fill=X, padx=5, expand=True)

        # Button to open file manager to choose where to save the file
        frame3 = Frame(self.window.Root)
        frame3.pack(fill=X)
        self.directory_button = Button(frame3,
                                        command=self.engine.InputMgr.Get_Dir,
                                        text="Save to")
        self.directory_button.pack(side=LEFT)

        # Radio buttons for choosing file extension to save as
        self.frame3 = Frame(self.window.Root)
        self.frame3.pack(fill=X)
        self.label3 = Label(self.frame3, text="Output file type:", width=6)
        self.label3.pack(fill=X, padx=5, pady=5)
        for val, file in enumerate(self.export_types):
            Radiobutton(self.frame3,
                            text=file,
                            padx = 20,
                            variable=self.engine.InputMgr.export_type,
                            command=None,
                            value=file).pack(anchor=W)

        # For any warning/update messages while running
        self.frame4 = Frame(self.window.Root)
        self.frame4.pack(fill=X)

        # To separate the bottom buttons of application from main application
        frameFinal = Frame(self.window.Root, relief=RAISED, borderwidth=1)
        frameFinal.pack(fill=BOTH, expand=True)

        # Quit and Retrieve buttons
        self.retrieve_button = Button(self.window.Root,
                                    command=self.engine.InputMgr.Retrieve,
                                    text="Retrieve")
        self.retrieve_button.pack(side=RIGHT)
        self.close_button = Button(self.window.Root, text="Quit",
                                command=self.engine.InputMgr.Quit_Button)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Packs any updates or warnings to the user through frame4          #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Update_User(self, string):
        # Forget any already printed warnings or updates before printing current
        for widget in self.frame4.winfo_children():
            widget.pack_forget()
        # Update while downloading and saving file
        if string == "Downloading":
            self.label_update = Label(self.frame4, text=string, width=X,
                                        foreground="firebrick2")
        # Update that the file has been downloaded and saved
        elif string == "Finished!":
            self.label_update = Label(self.frame4, text=string, width=X,
                                        foreground="medium sea green")
        # Update that the user must choose where to save file before retrieving
        elif string == "Choose where to save the file!":
            self.label_update = Label(self.frame4, text=string, width=X,
                                        foreground="firebrick2")
        # Update that the user must name the file before retrieving
        elif string == "Add a name for the file!":
            self.label_update = Label(self.frame4, text=string, width=X,
                                        foreground="firebrick2")
        # Return since there is nothing to pack
        else:
            return
        # Pack the warning/update label
        self.label_update.pack(side=LEFT, padx=5, pady=5)

        return
