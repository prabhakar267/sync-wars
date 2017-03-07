"""
upload.py
author : Prabhakar Gupta
link : http://www.prabhakargupta.com | https://www.github.com/prabhakar267

The script is used to upload all the files from a local directory
(LOCAL_DIRECTORY) and syncs it with a directory at Dropbox (DROPBOX_DIRECTORY)
"""

import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import dropbox
from dropbox.client import DropboxClient

from config import ACCESS_TOKEN, LOCAL_DIRECTORY, DROPBOX_DIRECTORY

client = dropbox.Dropbox(ACCESS_TOKEN)


class ModificationHandler(FileSystemEventHandler):
    """
    an event is fired whenever any modification occurs in LOCAL_DIRECTORY
    """
    
    def on_modified(self,event):
        """
        Every modification is uploaded to the Dropbox server to keep it
        synced with the DROPBOX_DIRECTORY
        """

        for root, dirs, files in os.walk(LOCAL_DIRECTORY):
            for filename in files:
                local_path = os.path.join(root, filename)
                DROPBOX_FILEPATH = local_path.replace("/home","")            
                DROPBOX_FILEPATH = DROPBOX_DIRECTORY + DROPBOX_FILEPATH                               
                try:
                    with open(local_path, 'rb') as f:
                        data = f.read()
                        client.files_upload(
                            data,
                            DROPBOX_FILEPATH,
                            mode = dropbox.files.WriteMode.overwrite
                        )
                except Exception as e:
                    print e                             


if __name__ == "__main__":    
    event_handler = ModificationHandler()
    
    # observer to keep a track of modifications on LOCAL_DIRECTORY
    observer = Observer()
    observer.schedule(event_handler, path = LOCAL_DIRECTORY, recursive = True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
