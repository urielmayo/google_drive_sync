# google_drive_sync

This project helps users to upload files to Google Drive, without the need to open the browser. It manages the events of a directory, and when file
is created or deleted the action gets reflected in the cloud.

## modules used:
- PyDrive
- WatchdogEventListener
- NotifyPy

Setup:
1. Create Google Developer user, setup credentials and enable Google Drive Api (more info in https://pythonhosted.org/PyDrive/quickstart.html).
2. Create virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
3. Setup Google Drive folder in "setup.py"
4. Run main.py

You are Done
