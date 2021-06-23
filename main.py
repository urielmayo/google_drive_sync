from notifypy import Notify
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from pathlib import Path

FOLDER_DIR = str(Path.home())+'/Escritorio/event_handler_test/'
file_type = ['directorio', 'archivo']
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        tipo = self.get_type(event)
        name = self.get_name(event)

        notify = Notify(
            default_notification_title=f'Nuevo {tipo} creado',
            default_notification_message=f'Se creo un {tipo} nuevo: {name}'
            ).send()

    def on_deleted(self, event):
        tipo = self.get_type(event)
        name = self.get_name(event)

        notify = Notify(
            default_notification_title=f'{tipo} Borrado',
            default_notification_message=f'Se borro un {tipo}: {name}'
        ).send()
    
    def get_type(self, event):
        if event.is_directory:
            return file_type[0]
        else:
            return file_type[1]
    
    def get_name(self,event):
        return event.src_path.split('/')[-1]


def main():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_DIR, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__=='__main__':
    main()