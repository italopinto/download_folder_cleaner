import logging
import shutil
import os


def extension_type(event):
    try:
        return event.src_path[event.src_path.rindex('.') + 1:]
    except:
        return logging.info(f'File {str(event.src_path)} doesn\'t have extension!')


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


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
    if extension_type(event) in ('mp4', 'avi', 'mvk'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx', 'odt'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx', 'odp'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css', 'c'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def is_zip_file(event):
    if extension_type(event) in ('zip', 'gz'):
        return True
    return False


def make_folder(foldername):
    # os.chdir('/home/italo/Downloads')
    if os.path.exists(foldername):
        logging.info('Folder already exists, skipping creation')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        logging.info('moving file')
    except:
        logging.info('File already existed in target folder')
        pass
