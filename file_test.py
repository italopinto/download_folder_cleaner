import os
import shutil
import sys
from pytube import YouTube

#the directory source (SRC) and destination (DST)
SRC = '/home/italo/Pictures'
DST = '/home/italo/Downloads'


def menu():
    print('Test of the folder_cleaner on Downloads directory:')
    print('[1] Move file.')
    print('[2] Delete file.')
    print('[3] Download a video from YouTube')
    print('[4] Exit.')
    option = input('Option: ')

    if option == '1':
        move_file()
        print()
        menu()
    elif option == '2':
        delete_file()
        print()
        menu()
    elif option == '3':
        download_from_youtube()
        print()
        menu()
    elif option == '4':
        sys.exit()


def move_file():
    os.chdir(SRC)
    if not os.path.exists(DST + '/<some>.<extension>'):
        shutil.copy2(SRC + '//<some>.<extension>', DST)
        print('File moved succesfuly!')
    else:
        print('File already exists.')


def delete_file():
    os.chdir(DST)
    if not os.path.exists('/<some>.<extension>'):
        print('File no long here.')
    else:
        os.remove('/<some>.<extension>')
        print('File deleted succesfuly!')


def download_from_youtube():
    video = input('Paste here the vídeo URL from YouTube: ')
    yt = YouTube(video)
    try:
        yt.streams.filter(progressive=True).first().download(DST)
        print('Downloaded succesfuly!')
    except:
        print('Something went wrong!')


if __name__ == '__main__':
    menu()
