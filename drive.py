from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from notifypy import Notify

DRIVE_ICON_PATH = './Google_Drive_logo.png'
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
            default_notification_title=f'New file created',
            default_notification_message=f'{file_name} uploaded to Drive',
            default_notification_icon= DRIVE_ICON_PATH
            ).send()
        print('File uploaded succesfully')
    
    def delete_file(self,file_name,path =''):
        
        delete_file = self.get_file_id(file_name)
        delete_file = self.drive.CreateFile({'id': delete_file})
        delete_file.Trash()

        notify = Notify(
            default_notification_title=f'File deleted',
            default_notification_message=f'{file_name} deleted from Drive',
            default_notification_icon= DRIVE_ICON_PATH
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


""" Use this for testing DriveApi methods

if __name__=='__main__':
    #your testing code goes here

"""
