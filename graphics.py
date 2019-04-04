import window as Wn
from tkinter import X, W, LEFT, BOTH, RAISED, RIGHT, Radiobutton
from tkinter.ttk import Frame, Button, Style, Label, Entry

class GfxMgr():
    def __init__(self, engine):
        self.width = None
        self.height = None
        self.name = None
        self.window = None
        self.engine = engine
        self.url_entry = None
        self.close_button = None
        return

    def Initialize(self, name, width, height):
        self.width = width
        self.height = height
        self.name = name
        self.window = Wn.Window(self.engine)
        self.window.Initialize(self.width, self.height, self.name)

        return

    def Run(self):

        return

    def Init_UI(self):
        self.export_types = [
        ("mp3"),
        ]
        # Adding Text Boxes
        self.frame1 = Frame(self.window.Root)
        self.frame1.pack(fill=X)
        self.label1 = Label(self.frame1, text="Save as: ", width = 6)
        self.label1.pack(side=LEFT, padx=5, pady=5)
        self.save_name = Entry(self.frame1)
        self.save_name.pack(fill=X, padx=5, expand=True)

        self.frame2 = Frame(self.window.Root)
        self.frame2.pack(fill=X)
        self.label2 = Label(self.frame2, text="Url: ", width = 6)
        self.label2.pack(side=LEFT, padx=5, pady=5)
        self.url_entry = Entry(self.frame2)
        self.url_entry.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self.window.Root)
        frame3.pack(fill=X)
        self.directory_button = Button(frame3,
                                        command=self.engine.InputMgr.Get_Dir,
                                        text="Save to")
        self.directory_button.pack(side=LEFT)

        self.frame3 = Frame(self.window.Root)
        self.frame3.pack(fill=X)
        self.label3 = Label(self.frame3, text="Output file type:", width=6)
        self.label3.pack(fill=X, padx=5, pady=5)
        for val, file in enumerate(self.export_types):
            Radiobutton(self.frame3,
                            text=file,
                            padx = 20,
                            variable=self.engine.InputMgr.export_type,
                            command=self.engine.InputMgr.Export_Choice,
                            value=file).pack(anchor=W)

        frameFinal = Frame(self.window.Root, relief=RAISED, borderwidth=1)
        frameFinal.pack(fill=BOTH, expand=True)

        self.frame4 = Frame(self.window.Root)
        self.frame4.pack(fill=X)

        self.retrieve_button = Button(self.window.Root,
                                    command=self.engine.InputMgr.Retrieve,
                                    text="Retrieve")
        self.retrieve_button.pack(side=RIGHT)
        self.close_button = Button(self.window.Root, text="Quit",
                                command=self.engine.InputMgr.Quit_Button)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)

        return

    def Update_User(self, string):
        for widget in self.frame4.winfo_children():
            widget.pack_forget()
        if string == "Downloading":
            self.label_update = Label(self.frame4, text=string, width=X, foreground="firebrick2")
        elif string == "Finished!":
            self.label_update = Label(self.frame4, text=string, width=X, foreground="medium sea green")
        elif string == "Choose where to save the file Noelle!":
            self.label_update = Label(self.frame4, text=string, width=X, foreground="firebrick2")
        elif string == "Noelle ya didn't put a name for the file!":
            self.label_update = Label(self.frame4, text=string, width=X, foreground="firebrick2")
        else:
            return
        self.label_update.pack(side=LEFT, padx=5, pady=5)
        return
