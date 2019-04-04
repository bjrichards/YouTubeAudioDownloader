#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Export Manager for application. Deals with downloading and exporting        #
#       of the requested information (url and extension mostly)               #
#                                                                             #
# Created April 3rd, 2019                                                     #
# Written by:                                                                 #
#   Braeden Richards                                                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                             Data Structures                                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Data():
    def __init__(self, engine):
        self.engine = engine

        # Extension type, aka mp3, mp4, etc
        self.export_type = None
        # Name of the file to be exported
        self.output_file_name = None
        # Full output file name with the extension
        self.output_file = None
        # Path to the directory to save the exported file
        self.directory_path = None
        # URL to get the data from
        self.requested_url = None

        return
