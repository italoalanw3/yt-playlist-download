# YouTube Playlist Downloader
YT-playlist-downloader is a command-line tool that downloads every video in a YouTube playlist as an MP3-file and automatically adds id3 tags to them. Those tags allow MP3 players to display information about a song such as the author or title.
It also detects new videos in the playlist and downloads only those.

This project uses [youtube-dl](https://github.com/rg3/youtube-dl) by [Ricardo Garcia](https://github.com/rg3) to download YouTube videos.


## Installation
#### Download
Either download the files as a zip and unpack them or clone the repository by running:

```git clone https://github.com/nicolasraube/yt-playlist-downloader.git```

#### Install [Python](https://www.python.org/downloads/)
Note: Please use Python 3.

#### Install Python modules
Run this command that installs required Python modules with pip (pip should come with Python):

```pip install colorama requests lxml mutagen beautifulsoup4 youtube_dl```

#### Install FFmpeg
[Download FFmpeg here](https://ffmpeg.org/download.html)

[How to install FFmpeg](https://www.google.com/search?q=how+to+install+ffmpeg)

You are now ready to use yt-playlist-downloader.

## Usage
#### Downloading
To download videos in a playlist, run this command:
```python ytdl.py "[url]" "[directory]"```
Please include the quotation marks.
##### [url]
URL to a video in the playlist (**not** to the playlist itself)

This means that the url should include /watch?v= and &list= like this:

https://www.youtube.com/watch?v=XCV34VJX&index=1&list=lskfjgPOIJSd63ksfgd345f43hjkl

and not /playlist?list= like this:

https://www.youtube.com/playlist?list=lskfjgPOIJSd63ksfgd345f43hjkl

Also keep in mind that it will download only the first 200 videos in a playlist. If you have more than 200 videos, please create multiple playlists. Downloading only new videos will still work.

##### [directory]
Local path to a directory where you want to download all videos to / where you already keep your downloaded files.

#### Examples
```python ytdl.py "https://www.youtube.com/watch?v=XCV34VJX&index=1&list=lskfjgPOIJSd63ksfgd345f43hjkl" "/home/nicolas/music/"```

```python ytdl.py "https://www.youtube.com/watch?v=XCV34VJX&index=1&list=lskfjgPOIJSd63ksfgd345f43hjkl" "D:\Music\"```

## Automatic tag setting
yt-playlist-downloader automatically sets the following MP3 tags (ID3):
#### Artist
Usually the first part of the YT-title
#### Title (of the song)
Usually the second part of the YT-title
#### Website
The YouTube-URL of the video which is used for comparing local MP3-files to the videos in a playlist.

For auto tag-setting to work flawlessly, the YT-title of the video must follow the following pattern:
<br><b>Artist - Title (additional information)</b><br>
If the YT-title contains exactly one dash ('-'), the left part of it will be used as the artist tag and the right part will be used as the title tag. Otherwise, the user will be prompted to enter the artist and song title after the whole download process finished.
Square brackets ('[ ]') and everything inside them will be removed from the title, as well as these characters: ' \ / " . _ :

## Edit tags of MP3s
The command to edit the tags is:
```python ytdl.py edit "[MP3]"```
Please include the quotation marks.

##### [MP3]
Local path to the MP3 file that you want to edit.

The program will now output the tags artist, title and URL with their current values.
To exit editing mode, enter

```exit```

To edit tags, enter a command like this:

```[tag]=[value]```

##### [tag]
Tag name, e.g. artist

##### [value]
Value for the tag, e.g. Adele

#### Examples
```python ytdl.py edit "D:\Music\Adele - Rolling In The Deep.mp3"```

Output:
```
Artist=Adel
Title=Rolling In The
URL=https://www.youtube.com/watch?v=rYEDA3JcQqw
```
You can now enter e.g.:
```
artist=Adele
title=Rolling In The Deep
exit
```
You have now changed the tags.
