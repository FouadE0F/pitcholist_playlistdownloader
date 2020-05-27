from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import pytube
import os
import requests
from bs4 import BeautifulSoup



Print("------Hi User in Download vidéos from YouTube------")
Print("-For Download vidéo type : V \n-For Download à playlist type L")
isVidorPlay = input('=> Your choise : ')


if (isVidorPlay.lower() == 'v' or isVidorPlay.lower() =='V') :
    video = input('Enter the video URL: ')
    yt = YouTube(video, on_progress_callback= on_progress)
    os.mkdir(yt.title)
    yt.streams[0].download(yt.title, filename=yt.title)
    x = input('Press ENTER to exit...')

elif (isVidorPlay.lower() == 'l' or isVidorPlay.lower()=='L') :
    count = 1
    playlist_input = input('Enter the playlist URL: ')
    playlist = Playlist(playlist_input)
    r = requests.get(playlist_input)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    foldername = soup.title.string
    os.mkdir(foldername)
    for vid in playlist:
        yt = YouTube(vid, on_progress_callback= on_progress)
        name = str(count)+'__'
        yt.streams[0].download(foldername, filename=name + yt.title)
        print('\n')
        print('Video number ' + str(count) + ' is completed')
        print('\n')
        count += 1
    local = os.getcwdb()
    print('Downloading done. You will find the playlist in "'+ str(local) +'"')
    x = input('Press ENTER to exit...')



'''

playlist = Playlist('https://www.youtube.com/playlist?list=PL6L4eAIx5ngAAP8BM97i1xcBKzTUyu7WK')
count = 0
#location = input('enter location: ')
for vid in playlist:
    yt = YouTube(vid)
    name = str(count)+'__'
    yt.streams[0].download('/home/topo/Desktop/',filename=name+yt.title)
    print("it's done")
    count += 1
'''
