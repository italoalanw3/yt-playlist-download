import os
from modules import terminal, fails
from mutagen.easyid3 import EasyID3
from mutagen.easyid3 import EasyID3KeyError

class MP3:
    def __init__(self, path):
        self.path = path
        self.tags = EasyID3(self.path)

    def read_artist(self):
        return self.read_tag("artist")

    def read_title(self):
        return self.read_tag("title")

    def read_url(self):
        return self.read_tag("website")

    def read_tag(self, tag):
        try:
            if tag in self.tags:
                return self.tags[tag][0]
            else:
                return ""
        except EasyID3KeyError:
            return ""


    def write_tags(self, tags):
        for tag in tags:
            self.tags[tag] = tags[tag]

        self.save()

    def save(self):
        self.tags.save()

    def has_all_tags(self):
        if not self.read_url():
            fails.add_fail(self.path)
            return False

        if not self.read_artist() or not self.read_title():
            return False

        return True

    def set_tags(self):
        filename_with_ext = os.path.basename(self.path)
        filename = os.path.splitext(filename_with_ext)[0]

        artist = ""
        title = ""

        terminal.print_green(filename)

        if "-" in filename and filename.count("-") == 1:
            try:
                artist = filename[:filename.index("-")].strip()
                print("Artist: " + artist)
            except Exception as e:
                print("Artist: não identificado")
                artist = 'não identificado'

            try:
                title = filename[filename.index("-")+1:].strip()
                print("Title: " + title)
            except Exception as e:
                print("Title: não identificado")
                title = 'não identificado'
        else:
            print("Enter artist name:")
            artist = input()

            print("\nEnter title:")
            title = input()

        self.write_tags({"artist": artist, "title": title})

    def edit(self):
        terminal.print_green("\n" + self.path)
        print("Artist: " + self.read_artist())
        print("Title: " + self.read_title())
        print("URL: " + self.read_url())

        while(True):
            userInput = input()

            if userInput.lower() == "exit" or userInput.lower() == "quit" or userInput.lower() == "stop" or userInput.lower() == "end" or userInput == "":
                break

            if self.user_wants_to_edit("artist", userInput):
                self.write_tags({"artist": userInput[7:].strip()})
            elif self.user_wants_to_edit("title", userInput):
                self.write_tags({"title": userInput[6:].strip()})
            elif self.user_wants_to_edit("url", userInput):
                self.write_tags({"website": userInput[4:].strip()})

    def user_wants_to_edit(self, value, userInput):
        return userInput.lower().startswith(value + "=") or userInput.lower().startswith(value + ":")
