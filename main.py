from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from pathlib import Path
from drive import DriveApi

FOLDER_PATH_FILE = 'folderpath.txt'
file_type = ['directorio', 'archivo']
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.drive = DriveApi()

    #file added to folder
    def on_created(self, event):
        """function called when file is created"""
        tipo = self.get_type(event)
        file_name = self.get_name(event)
        file_path = event.src_path

        self.drive.upload_file(file_name,file_path)
        

    #file deleted from folder
    def on_deleted(self, event):
        """function called if file is deleted"""
        tipo = self.get_type(event)
        file_name = self.get_name(event)

        self.drive.delete_file(file_name)
        
    def get_type(self, event):
        if event.is_directory:
            return file_type[0]
        else:
            return file_type[1]
    
    def get_name(self,event):
        return event.src_path.split('/')[-1]


def main():
    with open('folderpath.txt','r') as f:
        file_dir = f.readline()

    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, file_dir, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    

if __name__=='__main__':
    if FOLDER_PATH_FILE not in os.listdir('.'):
        print('Google drive folder not created. ')
    else:
        main()