"""
download.py
author : Prabhakar Gupta
link : http://www.prabhakargupta.com | https://www.github.com/prabhakar267

The script is used to download all the files from a directory at Dropbox
(DROPBOX_DIRECTORY) and syncs it with the local directory (LOCAL_DIRECTORY)
"""

import os
import time
import unicodedata

import dropbox
from dropbox.client import DropboxClient

from config import ACCESS_TOKEN, DROPBOX_DIRECTORY, LOCAL_DIRECTORY


# dropbox client to download files from dropbox sync path
client = dropbox.Dropbox(ACCESS_TOKEN)

# repeat the sync process every 120 seconds (2 minutes)
DELAY_TIME = 120


while True:
    dropbox_response = client.files_list_folder(DROPBOX_DIRECTORY, recursive=True)
    results = dropbox_response.entries

    # iterate through all the files and directories and get their file paths
    for file_object in results:
        if isinstance(file_object, dropbox.files.FileMetadata):
            file_path = file_object.path_display
            file_path = unicodedata.normalize('NFKD', file_path).encode('ascii','ignore')
            
            # download the file from dropbox
            md, res = client.files_download(file_path)
            data = res.content
            
            # set the local file path where we want the files to be
            # synced and stored.
            file_path = file_path.replace(DROPBOX_DIRECTORY,"/home")

            # if file doesn't exist then create the respective directories
            # before writing it to disk.
            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))
            
            with open(file_path, "w+") as f:
                f.write(data)

    time.sleep(DELAY_TIME)
