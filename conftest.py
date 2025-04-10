import os
from zipfile import ZipFile

import pytest

@pytest.fixture(scope='module')
def create_archive():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Папка с файлами
    files_folder = os.path.join(current_dir, 'resources')
    arhive_path = os.path.join(current_dir, 'resources/files.zip')
    # Файлы, которые будем архивировать
    files_to_archive = [os.path.join(files_folder, f) for f in os.listdir(files_folder)]
    if not os.path.isfile(arhive_path):
        with ZipFile("resources/files.zip", mode='w') as myzip:
            for file in files_to_archive:
                myzip.write(file)
