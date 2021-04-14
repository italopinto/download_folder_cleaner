#!/usr/bin/env python3

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_utils import *


# Function to wait until the download, move or creation event ends
def wait_event_finish(event):
    time.sleep(5)
    # if file > 1,5 mb
    if os.path.getsize(str(event.src_path)) >= 1500000:
        time.sleep(5)
        count = 1
        while os.path.getsize(str(event.src_path)) != count:
            count += 1
    # logging.warning(f'Counter: {count}{os.linesep}File size: {os.path.getsize(str(event.src_path))}')
    time.sleep(3)
    return


# Function to check if the file have extension
def check_extension(event):
    try:
        event.src_path[event.src_path.rindex('.') + 1:]
        return True
    except:
        return False


# Main routine for the handlers
def main(event):
    try:
        # check if the event was a directory
        if os.path.isdir(event.src_path):
            return
        # if the event wasn't a directory: check if the file has extension
        if check_extension(event) is False:
            return logging.warning(f'File {str(event.src_path)} doesn\'t have extension!')
        # if the file has extension: check if the file exists yet
        if os.path.exists(event.src_path):
            if is_pdf_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('pdf')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_doc_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('documents')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_image_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('images')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_spreadsheet_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('spreadsheets')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_presentation_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('presentation files')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_executable_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('windows executable files')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_csv_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('csv')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_code_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('code')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_mp3_file(event):
                wait_event_finish(event)
                path_to_folder = make_folder('audio')
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_video_file(event):
                wait_event_finish(event)
                # if the video is larger than 50 mb
                if os.path.getsize(str(event.src_path)) > 50000000:
                    return
                else:
                    path_to_folder = make_folder('videos')
                    move_to_new_corresponding_folder(event, path_to_folder)
                    return
            else:
                return
        else:
            return 
    except:
        return logging.warning('Error in the main() Function!')


# logging configuration
logging.basicConfig(level=logging.WARNING,
                    filename='download_watcher.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')


# Overriding the handler class from watchdog
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        pass

    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        main(event)

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        main(event)


# Instancing classes of watchdog
event_handler = Handler()
observer = Observer()
os.chdir('/home/italo/Downloads')
pwd = os.getcwd()
observer.schedule(event_handler, pwd, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
