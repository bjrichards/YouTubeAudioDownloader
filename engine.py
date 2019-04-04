#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Engine for this application. Contains all the other managers.               #
#                                                                             #
# Created April 3rd, 2019                                                     #
# Written by:                                                                 #
#   Braeden Richards                                                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                 Imports                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import graphics as Graphics     # GraphicsManager
import input as Input           # InputManager
import exporting as Export      # ExportManager
import data as Data             # Data structure for whole app


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# @Def: Engine for whole application                                          #
# @Inherits: None                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Engine():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: __init__ of Object                                                #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__(self):
        self.GfxMgr = None          # Graphics Manager
        self.InputMgr = None        # Input Manager
        self.ExportMgr = None       # Export Manager
        self.Data = None            # Data Structure

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Initializes variables of the Engine                               #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Initialize(self):
        # Create Objects
        self.GfxMgr = Graphics.GfxMgr(self)
        self.InputMgr = Input.InputMgr(self)
        self.Data = Data.Data(self)

        # Initialize the managers
        # The GfxMgr MUST be initialized before InputMgr or ExportMgr
        # The InputMgr MUST be initialized before the ExportMgr
        self.GfxMgr.Initialize("YouTube Audio Downloader", 600, 300)
        self.InputMgr.Initialize()
        self.ExportMgr = Export.ExportMgr(self)

        # Create/Initialize the UI to be packed on the tkinter main window
        self.GfxMgr.Init_UI()
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # @Def: Calls Tkinter's main loop to run the application                  #
    # @Param: None                                                            #
    # @Return: None                                                           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Run(self):
        # Call tkinter's internal loop
        self.GfxMgr.window.Root.mainloop()
        return
