# YouTube Audio Downloader - UNDER DEVELOPMENT

## Description
YoutubeAudioDownloader is a simple GUI written in Python3 that makes downloading YouTube videos and converting them to aac, mp3, or wav file formats much easier and more user-friendly.

This application has only been tested and developed with MacOS in mind. It <should> run on Windows and Linux as long as Tkinter, FFmpeg, and Youtube-dl are all installed libraries, however this has not been tested. Also, the GUI has only been designed to look nice with MacOS's window properties so any other OS it most likely will not be correctly formatted/positioned.

## Dependency Instructions
This project uses Python3.6. Newer versions should work, but nothing is guaranteed. <br>
In addition to Python3.6, this project requires installation of the following libaries:
 * [Tkinter](https://docs.python.org/3/library/tkinter.html)
 * [FFmpeg](https://ffmpeg.org/)
 * [Youtube-dl](http://ytdl-org.github.io/youtube-dl/)

### MacOS
####Installing of libraries
Assumption made that the user has access to pip3.
```bash
  pip3 install ffmpeg youtube-dl

```
####Run Application
```bash
  python main.py
```
