from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.drive import GoogleDriveFile
from notifypy import Notify

class DriveApi:

    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile("mycreds.txt")

        if self.gauth.credentials is None:
            # Authenticate if they're not there
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            # Refresh them if expired
            self.gauth.Refresh()
        else:
            # Initialize the saved creds
            self.gauth.Authorize()
        # Save the current credentials to a file
        self.gauth.SaveCredentialsFile("mycreds.txt")

        self.drive = GoogleDrive(self.gauth)
        print('succesfull login')
    
    def upload_file(self,file_name, path):
        print('uploading file...')
        new_file = self.drive.CreateFile({'title' : file_name })
        new_file.SetContentFile(path)
        new_file.Upload()

        notify = Notify(
            default_notification_title=f'Nuevo archivo creado',
            default_notification_message=f'Se subio {file_name} a la nube'
            ).send()
        print('File uploaded succesfully')
    
    def delete_file(self,file_name,path =''):
        
        delete_file = self.get_file_id(file_name)
        delete_file = self.drive.CreateFile({'id': delete_file})
        delete_file.Trash()

        notify = Notify(
            default_notification_title=f'Archivo Borrado',
            default_notification_message=f'Se borro {file_name} de la nube'
            ).send()
        print('File deleted succesfully')
        

    def list_files(self):
        file_list = self.drive.ListFile(
            {'q':"'root' in parents and trashed=false"}
            ).GetList()
        return file_list
    
    def get_file_id(self, file_name):
        files = self.list_files()
        for file in files:
            if file['title'] == file_name:
                return file['id']



if __name__=='__main__':

    drive_api = DriveApi()
    file_list = drive_api.list_files()
    #print(file_list[0].keys())
    for file in file_list:
        print(file['title'])
        print(file['id'])
        print(file['parents'][0]['isRoot'])
