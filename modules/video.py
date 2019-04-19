import re, os

class Video:
    def __init__(self, title, url, path):
        self.title = self.remove_bad_chars(title)
        self.url = "https://www.youtube.com" + self.remove_url_parameters(url)
        self.path = os.path.join(path, self.title + ".mp3")

    def remove_url_parameters(self, url):
        head, separator, tail = url.partition("&")
        return head

    def remove_bad_chars(self, str):
        str = str.replace("'", "").replace("\"", "").replace("/", "").replace("\\", "").replace(".", "").replace("_", "").replace(":", "")
        str = self.remove_square_brackets(str)
        return str

    def remove_square_brackets(self, str):
        return re.sub(r'\[.*?\]', '', str)
