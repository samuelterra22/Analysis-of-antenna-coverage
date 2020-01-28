import os
import zipfile

def unzip(filename, extract_to):

    this_folder = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(this_folder, filename)

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
