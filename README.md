# Youtube Downloader & Converter

This script automates some of the process needed to download video from youtube videos.  The raw download from youtube-dl does not play on iPods, so this script converts them to mp3 files.

Feel free to use and add to this however you need.  I made it to speed up the process of putting media on my iPod.  There are a lot of ways it can be improved on.
## Dependencies

 - [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)
 - [ffmpeg](https://ffmpeg.org/download.html)


This script is just a wrapper around these two tools.  As long as they're both in your path variables they should work no matter how they are installed.

It looks like they're both in pip so you might be able to do:

    pip install ffmpeg
    pip install youtube-dl

## Installation
Navigate to the folder you would like to work in.

    git clone https://github.com/DeGrandis/youtube-downloader-converter.git
    cd youtube-downloader-converter

## Using

Since this is a wrapper around youtube-dl, you can do anything you can do with it.  I.E Download single videos or entire playlists.  This script converts them when done.



Windows

    python.exe .\process.py [VIDEO URL]
    python.exe .\process.py [PLAYLIST URL]

Linux/Mac 
*(if you're using these you know what to do)*

    python ./process.py [VIDEO URL]
    python ./process.py [PLAYLIST URL]
