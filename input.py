import tkinter as tk
from tkinter import filedialog
import _thread

class InputMgr():
    def __init__(self, engine):
        self.engine = engine
        self.folder_selected = None
        return

    def Initialize(self):
        self.export_type = '.'
        self.output_file = tk.StringVar()
        return

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
            self.engine.GfxMgr.Update_User("Choose where to save the file Noelle!")
            return
        # Save file to correct filepath and as the correct file name
        if self.engine.Data.output_file_name != '':
            self.engine.ExportMgr.ydl_opts['outtmpl'] = self.engine.Data.directory_path + '/' + self.engine.Data.output_file_name + ".%(ext)s"
        elif self.engine.Data.output_file_name == None or self.engine.Data.output_file_name == '':
            self.engine.GfxMgr.Update_User("Noelle ya didn't put a name for the file!")
            return
        # Retrieve the data from the url, save the data
        _thread.start_new_thread(self.engine.ExportMgr.Run,(
                        self.engine.ExportMgr.ydl_opts,
                        self.engine.Data.requested_url))
        return

    def Export_Choice(self):
        return

    def Quit_Button(self):
        self.engine.GfxMgr.window.Root.quit()
        return

    def Get_Dir(self):
        self.engine.Data.directory_path = filedialog.askdirectory()
        return
