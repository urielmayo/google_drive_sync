from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from notifypy import Notify

"""
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
    print('title: %s' % (file1['title']))

new_file = drive.CreateFile({'title': 'hola.txt'})
new_file.SetContentFile('hola.txt')
new_file.Upload()
"""

class DriveApi:

    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()

        self.drive = GoogleDrive(gauth)
        print('succesfull login')
    
    def upload_file(self,filename, path):
        print('uploading file...')
        new_file = self.drive.CreateFile({'title' : filename })
        new_file.SetContentFile(path)
        new_file.Upload()

        notify = Notify(
            default_notification_title=f'Nuevo archivo creado',
            default_notification_message=f'Se subio {filename} a la nube'
            ).send()
        print('File uploaded succesfully')

#drive_api = DriveApi()
#drive_api.upload_file('main.py')