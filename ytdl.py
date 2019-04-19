#!/usr/bin/env python

from modules import terminal, fails
from modules.downloader import Downloader
from modules.mp3 import MP3

def main():
    if terminal.get_argument_count() < 3:
        terminal.print_help()
        exit()
    else:
        firstArg = terminal.get_argument(1)
        secondArg = terminal.get_argument(2)

        if firstArg == "help":
            terminal.print_help()
        elif firstArg == "edit":
            MP3(secondArg).edit()
        else:
            downloader = Downloader(secondArg)

            new_videos = downloader.find_new_videos(firstArg)
            terminal.print_green(str(len(new_videos)) + " new videos found in playlist")

            downloader.download_videos(new_videos)

            for fail in fails.fails:
                terminal.print_red("failed: " + fail)

main()
