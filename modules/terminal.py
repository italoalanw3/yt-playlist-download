import sys, colorama

colorama.init(autoreset=True)

def get_argument_count():
    return len(sys.argv)

def get_argument(index):
    return sys.argv[index]


def print_green(str):
    try:
        print(colorama.Fore.GREEN + str)
    except:
        print(colorama.Fore.GREEN + 'Não foi possível exibir string')

def print_red(str):
    print(colorama.Fore.RED + str)

def print_help():
    print("usage:")
    print("")

    print_green("ytdl.py <url> <dir>")
    print("<url> - url to a video in the playlist that you want to download")
    print("<dir> - the directory where the videos should be downloaded to")

    print("")
    print_green("ytdl.py edit <mp3file>")
    print("<mp3file> - path to the mp3 file that you want to edit the tags of")
    print("ytdl will output the id3 tags of the mp3 file")
    print("you can edit those tags by first using this edit command and then typing the tag that you want to change with an equality sign and the value")
    print("e.g.:")
    print("url=https://www.youtube.com/watch?v=oHg5SJYRHA0")
    print("artist=Adele")
    print("type \"exit\" to exit editing mode")
