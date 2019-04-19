import subprocess, os
from modules import scraper, terminal
from modules.directory import Directory
from modules.mp3 import MP3

class Downloader:
    def __init__(self, path):
        self.directory = Directory(path)

    def find_new_videos(self, url):
        videos_in_playlist = scraper.find_videos_in_playlist(url, self.directory.path)

        downloaded_files = self.directory.get_downloaded_files()
        terminal.print_green(str(len(downloaded_files)) + " files found in directory")

        terminal.print_green(str(len(videos_in_playlist)) + " videos found in playlist")

        new_videos = self.directory.find_new_videos(videos_in_playlist, downloaded_files)
        self.count_new_videos = str(len(new_videos))

        return new_videos

    def download_videos(self, videos):
        for video in videos:
            terminal.print_green("\n" + str(videos.index(video)+1) + "/" + self.count_new_videos)
            terminal.print_green(video.title)

            self.download_video(video)
            try:
                mp3 = MP3(video.path)
                mp3.write_tags({"website": video.url})
            except Exception:
                terminal.print_red("File not existing")

        self.directory.check_file_tags()

    def download_video(self, video):
        print(self.directory.path)
        print(video.url)
        subprocess.call(["youtube-dl", "-x", "--prefer-ffmpeg", "--audio-format", "mp3", "-o",
            os.path.join(self.directory.path, video.title + ".%(ext)s"), video.url])
