import os
from pathlib import Path

while True:
    try:
        google_sync_folder = input("Insert google synchronization folder from home: ")
        os.mkdir(Path.home() / google_sync_folder)
        with open('./folderpath.txt','w') as f:
            f.write(str(Path.home() / google_sync_folder))
        break
    except FileNotFoundError:
        print('Folder cannot be created, path error ocurred. Please try again')
