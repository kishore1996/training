from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
def parse_download(folderid):
    file = drive.CreateFile({'id': folderid})
    root_name=file['title']
    try:
        os.mkdir(root_name)
    except:
        pass
    os.chdir(root_name)
    file_list = drive.ListFile({'q': "'{0}' in parents and trashed=false".format(file["id"])}).GetList()
    for file1 in file_list:
        try :
            if (not file1["mimeType"]=='application/vnd.google-apps.folder') :
                if not file1["title"] in os.listdir():
                    download = drive.CreateFile({'id': '{0}'.format(file1["id"])})
                    download.GetContentFile('{}'.format(file1["title"]))
            else:
                print('title: %s, id: %s' % (file1['title'], file1['id']))
                parse_download(file1["id"])
                os.chdir("../")
            
        except:
            continue    
            
parse_download("1t-AOk5ymdLRY0_bc4Kqzxwa7M3U9Lm1P")        
def drive_download_folder(folderid):
    try:
        parse_download(folderid)
    except:
        pass
    os.chdir('../')