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
from tkinter import *
from tkinter import X, W, LEFT, BOTH, RAISED, RIGHT, Radiobutton
# from tkinter import Frame, Button, Style, Label, Entry
# from tkinter import tk

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
        self.window = None          # Window object
        self.engine = engine        # Engine that this mgr is part of
        self.style = None
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Initializes Window of the GfxMgr                                  #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Initialize(self, name, width, height):
        self.window = Wn.Window(self.engine)
        self.window.Initialize(width, height, name)
        self.engine.Data.export_type = StringVar(master=self.window.Root)
        self.engine.Data.export_type.set("aac")

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Creates the UI of the main window of application                  #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Init_UI(self):

        # Creating main containers
        self.top_frame = Frame(self.window.Root, width=540, height=250, pady=3, bg="#f4c242")
        self.bottom_frame = Frame(self.window.Root, width=540, height=50, bg="#f4c242")
        self.bottom_left = Frame(self.bottom_frame, width=420, bg="#f4c242")
        self.bottom_right = Frame(self.bottom_frame, width=120, bg="#f4c242")

        # Layout main containers
        self.window.Root.grid_rowconfigure(0, weight=1)
        self.window.Root.grid_rowconfigure(1, weight=1)
        self.window.Root.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.bottom_frame.grid(row=1, sticky="ew")
        self.bottom_left.grid(row=0, column=0, sticky="e")
        self.bottom_right.grid(row=0, column=1, sticky="w")

        # Create widgets for top frame
        self.save_label = Label(self.top_frame, text="Save as: ", bg="#f4c242")
        self.save_entry = Entry(self.top_frame, width=60, bg="#ef8f09", highlightbackground="#f4c242")
        self.url_label = Label(self.top_frame, text="Url: ", bg="#f4c242")
        self.url_entry = Entry(self.top_frame, width=60, bg="#ef8f09", highlightbackground="#f4c242")
        self.dir_button = Button(self.top_frame, command=self.engine.InputMgr.Get_Dir, text="Save to", bg="#ef8f09", activebackground="#ef7409", highlightbackground="#f4c242")
        self.radio_label = Label(self.top_frame, text="File type: ", bg="#f4c242")
        self.radio_1 = Radiobutton(self.top_frame, text="aac", variable=self.engine.Data.export_type, value="aac", width=8, bg="#f4c242", activebackground="#f4c242", selectcolor="#ef7409")
        self.radio_2 = Radiobutton(self.top_frame, text="mp3", variable=self.engine.Data.export_type, value="mp3", width=8, bg="#f4c242", activebackground="#f4c242", selectcolor="#ef7409")
        self.radio_3 = Radiobutton(self.top_frame, text="wav", variable=self.engine.Data.export_type, value="wav", width=8, bg="#f4c242", activebackground="#f4c242", selectcolor="#ef7409")

        # Layout widgets for top frame
        self.save_label.grid(row=0, column=0)
        self.save_entry.grid(row=0, column=1)
        self.url_label.grid(row=1, column=0)
        self.url_entry.grid(row=1, column=1)
        self.dir_button.grid(row=2, column=0)
        self.radio_label.grid(row=3, column=0)
        self.radio_1.grid(row=4, column=0)
        self.radio_2.grid(row=5, column=0)
        self.radio_3.grid(row=6, column=0)

        # Create Widgets for bottom frame
        self.close_button = Button(self.bottom_right, text="Quit", command=self.engine.InputMgr.Quit_Button, bg="#ef8f09", activebackground="#ef7409", highlightbackground="#f4c242")
        self.retrieve_button = Button(self.bottom_right, command=self.engine.InputMgr.Retrieve, text="Retrieve", bg="#ef8f09", activebackground="#ef7409", highlightbackground="#f4c242")

        # Layout Widgets for bottom frame
        self.close_button.grid(row=0, column=0)
        self.retrieve_button.grid(row=0, column=1)

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Packs any updates or warnings to the user through frame4          #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Update_User(self, string):
        # Update while downloading and saving file
        if string == "Downloading":
            self.label_update = Label(self.bottom_left, text=string,
                                        foreground="firebrick2")
        # Update that the file has been downloaded and saved
        elif string == "Finished!":
            self.label_update = Label(self.bottom_left, text=string,
                                        foreground="medium sea green")
        # Update that the user must choose where to save file before retrieving
        elif string == "Choose where to save the file!":
            self.label_update = Label(self.bottom_left, text=string,
                                        foreground="firebrick2")
        # Update that the user must name the file before retrieving
        elif string == "Add a name for the file!":
            self.label_update = Label(self.bottom_left, text=string,
                                        foreground="firebrick2")
        # Return since there is nothing to pack
        else:
            return
        # Pack the warning/update label
        self.label_update.grid(row=0, column=0)

        return
