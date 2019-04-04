import graphics as Graphics
import input as Input
import exporting as Export
import data as Data
class Engine():
    def __init__(self):
        self.GfxMgr = None
        self.InputMgr = None
        self.ExportMgr = None
        self.Data = None

        return

    def Initialize(self):
        self.GfxMgr = Graphics.GfxMgr(self)
        self.InputMgr = Input.InputMgr(self)
        self.Data = Data.Data(self)
        self.GfxMgr.Initialize("Noelle's Youtube Helper", 600, 300)
        self.InputMgr.Initialize()
        self.ExportMgr = Export.ExportMgr(self)
        self.GfxMgr.Init_UI()
        return

    def Run(self):
        self.GfxMgr.window.Root.mainloop()
        return

    def Stop(self):

        return
