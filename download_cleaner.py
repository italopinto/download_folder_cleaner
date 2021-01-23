#!/usr/bin/python3

import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from file_utilities import *


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        if os.path.isdir(event.src_path):
            return
        if is_code_file(event):
            path_to_folder = make_folder('code')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_text_file(event):
            path_to_folder = make_folder('text')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_pdf_file(event):
            path_to_folder = make_folder('pdf')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_mp3_file(event):
            path_to_folder = make_folder('audio')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_image_file(event):
            path_to_folder = make_folder('images')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_video_file(event):
            try:
                # if the video is larger than 50 mb
                if os.path.getsize(str(event.src_path)) > 50000000:
                    return logging.info('File is too large!')
                else:
                    path_to_folder = make_folder('videos')
                    move_to_new_corresponding_folder(event, path_to_folder)
                    return
            except FileNotFoundError:
                pass
        elif is_doc_file(event):
            path_to_folder = make_folder('documents')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_spreadsheet_file(event):
            path_to_folder = make_folder('spreadsheets')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_presentation_file(event):
            path_to_folder = make_folder('presentation files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_executable_file(event):
            path_to_folder = make_folder('executable files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_zip_file(event):
            return logging.info(f'{str(event.src_path)} is a compacted file, do nothing')

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


logging.basicConfig(level=logging.INFO,
                    filename='folder_watcher.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')
file_change_handler = Handler()
event_handler = LoggingEventHandler()
observer = Observer()
os.chdir('/home/italo/Downloads')
pwd = os.getcwd()
logging.info('Watchdog is watching: ' + pwd)
observer.schedule(file_change_handler, pwd, recursive=False)
observer.schedule(event_handler, pwd, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
