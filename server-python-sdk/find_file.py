import os


def find_file(filename: str, search_path: str):
    for dirpath, _, filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None
