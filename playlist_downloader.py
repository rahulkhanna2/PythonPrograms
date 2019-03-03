url= "https://www.youtube.com/playlist?list=PLf0swTFhTI8rT3ApjBqt338MCO0ZvReFt"

import requests
from bs4 import BeautifulSoup as bs
from pytube import YouTube
import os

def playlistDownloader(url, path):
    tags = parsing(url)
    if "watch" not in url:
        new_page_url = "https://www.youtube.com" + tags[0]
        final_watch_tags = parsing(new_page_url)
    else:
        final_watch_tags= parsing(url)
    download(final_watch_tags, path)        
 
def parsing(u):
    watch_tags= []
    r = requests.get(u)
    soup = bs(r.text, "html.parser")
    a_tags = soup.find_all("a")
    for link in a_tags:
        if(link.get("href").startswith("/watch") and "list" in link.get("href")):
            watch_tags.append(link.get("href"))
    return watch_tags

def download(tags, path):
    seen = set()
    tags= [x for x in tags if not (x in seen or seen.add(x))]
    for tag in tags:
        yt= YouTube("https://youtube.com" + tag)
        filesize= round(yt.streams.first().filesize / (1024*1024) ,2 )
        print ("Downloading:- " + yt.title + " (" + str(filesize)+ "MB)")
        yt.streams.first().download(str(path))
        
def videoDownload(url, path):
    yt= YouTube(url)
    filesize= round(yt.streams.first().filesize / (1024*1024) ,2 )
    print ("Downloading:- " + yt.title + " (" + str(filesize)+ "MB)")
    yt.streams.first().download(str(path))