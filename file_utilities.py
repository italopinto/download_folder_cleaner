import shutil
import os
import logging


# Indentifiers for the extension_type of the archives
def extension_type(event):   
    return event.src_path[event.src_path.rindex('.') + 1:]   


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'jpeg', 'bmp', 'gif', 'raw', 'svg'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mp4', 'avi'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx', 'odt'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx', 'ods'):
        return True
    return False


def is_csv_file(event):
    if extension_type(event) in ('csv'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx', 'odp'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cpp', 'js', 'php', 'html', 'sql', 'css', 'c'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def make_folder(foldername):
    if os.path.exists(foldername):
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
    except:
        logging.warning(
            f'Can\'t complete the move operation for {event.src_path}, already exists.')
        return
