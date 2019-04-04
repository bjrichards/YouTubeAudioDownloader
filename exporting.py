from __future__ import unicode_literals
import youtube_dl

class ExportMgr():
    def __init__(self, engine):
        self.engine = engine
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        }
        return

    def Run(self, ydl_opts, requested_url):
        self.engine.GfxMgr.Update_User("Downloading")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([requested_url])
        self.engine.GfxMgr.Update_User("Finished!")
        return
