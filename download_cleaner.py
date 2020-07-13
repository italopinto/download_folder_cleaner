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
        try:
            if is_code_file(event) == True:
                path_to_folder = make_folder('code')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_text_file(event) == True:
                path_to_folder = make_folder('text')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_pdf_file(event) == True:
                path_to_folder = make_folder('pdf')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_mp3_file(event) == True:
                path_to_folder = make_folder('audio')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_image_file(event) == True:
                path_to_folder = make_folder('images')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_video_file(event) == True:
                path_to_folder = make_folder('videos')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_doc_file(event) == True:
                path_to_folder = make_folder('word documents')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_spreadsheet_file(event) == True:
                path_to_folder = make_folder('spreadsheets')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
            if is_presentation_file(event) == True:
                path_to_folder = make_folder('presentation files')
                move_to_new_corresponding_folder(event,path_to_folder)
                return
        except:
            print('File processing error')
    @staticmethod
    def on_modified(event):
        pass

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Users\\jdsjh\\Downloads')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()