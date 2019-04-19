import os
from modules import terminal
from modules.mp3 import MP3

class Directory:
    def __init__(self, path):
        self.path = path
        self.mkdir()

    def mkdir(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def find_new_videos(self, videos_in_playlist, files):
        if len(files) == 0:
            return videos_in_playlist

        new_videos = list(videos_in_playlist)

        for video in videos_in_playlist:
            for file in files:
                if video.url == MP3(file).read_url():
                    new_videos.remove(video)

        return new_videos

    def get_downloaded_files(self):
        files = []

        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                files.append(os.path.join(self.path, file))

        return files

    def check_file_tags(self):
        mp3s_without_tags = []
        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                mp3 = MP3(os.path.join(self.path, file))
                if not mp3.has_all_tags():
                    mp3s_without_tags.append(mp3)

        for mp3 in mp3s_without_tags:
            terminal.print_green("\n" + str(mp3s_without_tags.index(mp3)+1) + "/" + str(len(mp3s_without_tags)))
            mp3.set_tags()
