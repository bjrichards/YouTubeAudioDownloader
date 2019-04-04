#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Input Manager for application. Deals with button presses and inputs         #
#                                                                             #
# Created April 3rd, 2019                                                     #
# Written by:                                                                 #
#   Braeden Richards                                                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                 Imports                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import tkinter as tk                # For StringVar
from tkinter import filedialog      # For opening file managers
import _thread                      # To multithread while downloading

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# @Def: Input Manager for whole application                                   #
# @Inherits: None                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class InputMgr():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: __init__ of Object                                                #
    # @Param: <Engine> engine: Engine containing all the managers             #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__(self, engine):
        self.engine = engine        # Engine containing this and all managers
        self.folder_selected = None # Folder path to save to
        return


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Initializes variables of the InputMgr                             #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Initialize(self):
        self.export_type = '.'              # What file extension to save as
        self.output_file = tk.StringVar()   # File name
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Retrieves information from tkinter buttons and text boxes,        #
    #       updates applications data structure to proper files for grabbing  #
    #       and saving of requested data                                      #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Retrieve(self):
        # Get the name of the file to be saved
        self.engine.Data.output_file_name = self.engine.GfxMgr.save_name.get()
        # Get the string of what the
        self.engine.Data.export_type = 'mp3'
        # Get the full string of the output file
        self.engine.Data.output_file = (self.engine.Data.output_file_name + '.'
                + self.engine.Data.export_type)
        # Get the url to read from
        self.engine.Data.requested_url = self.engine.GfxMgr.url_entry.get()
        if self.engine.Data.directory_path == None:
            self.engine.GfxMgr.Update_User("Choose where to save the file!")
            return
        # Save file to correct filepath and as the correct file name
        if self.engine.Data.output_file_name != '':
            self.engine.ExportMgr.ydl_opts['outtmpl'] = self.engine.Data.directory_path + '/' + self.engine.Data.output_file_name + ".%(ext)s"
        elif self.engine.Data.output_file_name == None or self.engine.Data.output_file_name == '':
            self.engine.GfxMgr.Update_User("Add a name for the file!")
            return
        # Retrieve the data from the url, save the data
        _thread.start_new_thread(self.engine.ExportMgr.Run,(
                        self.engine.Data.requested_url,))
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Quits tkinter an closes application when quit button pressed      #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Quit_Button(self):
        self.engine.GfxMgr.window.Root.quit()
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Opens file/directory manager to choose file path to save to       #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Get_Dir(self):
        self.engine.Data.directory_path = filedialog.askdirectory()
        return
