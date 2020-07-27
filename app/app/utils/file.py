import os
import uuid
from pathlib import Path
from fastapi import UploadFile

ROOT_DIR = '/app/'
UPLOADS_DIR = os.path.join(ROOT_DIR, 'uploads')
BANK_LOGOS_DIR = '/static/banks/'


def get_unique_filename(filename):
    return f'{uuid.uuid4()}-{filename}'

def get_file_destination(filename):
    return os.path.join(UPLOADS_DIR, 'banks', filename)

def save_uploaded_file(file: UploadFile):
    filename = get_unique_filename(file.filename)
    path = get_file_destination(filename)
    url = BANK_LOGOS_DIR + filename
    with open(path, 'w+b') as destination:
        destination.write(file.file.read())
        return url

def delete_file(path: str):
    real_path = path.replace('/static', UPLOADS_DIR, 1)
    if os.path.exists(real_path):
        os.remove(real_path)
