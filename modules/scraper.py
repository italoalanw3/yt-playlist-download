import requests
from bs4 import BeautifulSoup
from modules.video import Video

def scrape(url):
    return requests.get(url).text

def parse_HTML(str):
    return BeautifulSoup(str, "lxml")

def select_a_tags(parsed_HTML):
    return parsed_HTML.select("a.spf-link.playlist-video.clearfix.yt-uix-sessionlink.spf-link")

def get_video_title(a_tag):
    return a_tag.find("h4").contents[0].replace("\n", "").strip()

def find_videos_in_playlist(url, path):
    parsed_HTML = parse_HTML(scrape(url))
    a_tags = select_a_tags(parsed_HTML)

    videos = []

    for a_tag in a_tags:
        title = get_video_title(a_tag)
        url = a_tag["href"]
        videos.append(Video(title, url, path))

    return videos
