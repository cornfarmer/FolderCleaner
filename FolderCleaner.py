from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime,strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i=1
            new_name = filename
            extension = 'noname'
            try:
                extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                path = extensions_folders[extension]
            except Exception:
                extension = 'noname'
            
            folder_destination_path = extensions_folders[extension]

            for folder_name in os.listdir(extensions_folders[extension]):
                file_exists=os.path.isfile(folder_destination_path +"/"+new_name)

            while file_exists:
                i += 1
                new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                new_name = new_name.split("/")[4]
                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
            src = folder_to_track + "/" + filename

            new_name = folder_destination_path + "/"+ new_name
            os.rename(src,new_name)

extensions_folders = {
#No name
    'noname': "/Users/techn/Downloads",
#Apps
    '.exe': "/Users/techn/Downloads/Apps",
#Text
    '.txt' : "/Users/techn/Downloads/Text",
    '.doc' : "/Users/techn/Downloads/Text",
    '.docx' : "/Users/techn/Downloads/Text",
    '.odt ' : "/Users/techn/Downloads/Text",
    '.pdf': "/Users/techn/Downloads/Text",
    '.rtf': "/Users/techn/Downloads/Text",
    '.tex': "/Users/techn/Downloads/Text",
    '.wks ': "/Users/techn/Downloads/Text",
    '.wps': "/Users/techn/Downloads/Text",
    '.wpd': "/Users/techn/Downloads/Text",
#Images
    '.ai':"/Users/techn/Downloads/Images",
    '.bmp': "/Users/techn/Downloads/Images",
    '.gif': "/Users/techn/Downloads/Images",
    '.ico': "/Users/techn/Downloads/Images",
    '.jpg': "/Users/techn/Downloads/Images",
    '.jpeg': "/Users/techn/Downloads/Images",
    '.png': "/Users/techn/Downloads/Images",
    '.ps': "/Users/techn/Downloads/Images",
    '.psd': "/Users/techn/Downloads/Images",
    '.svg': "/Users/techn/Downloads/Images",
    '.tif': "/Users/techn/Downloads/Images",
    '.tiff': "/Users/techn/Downloads/Images",
    '.CR2': "/Users/techn/Downloads/Images",
    '.jfif': "/Users/techn/Downloads/Images",

#Compressed
    '.7z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.arj': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.deb': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.pkg': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rar': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rpm': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.tar.gz': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.zip': "/Users/kalle/Desktop/kalle/Other/Compressed",

#Presentations
    '.key': "/Users/techn/Downloads/Presentations",
    '.odp': "/Users/techn/Downloads/Presentations",
    '.pps': "/Users/techn/Downloads/Presentations",
    '.ppt': "/Users/techn/Downloads/Presentations",
    '.pptx': "/Users/techn/Downloads/Presentations",
#Programming
    '.c': "/Users/techn/Downloads/Programming",
    '.class': "/Users/techn/Downloads/Programming",
    '.dart': "/Users/techn/Downloads/Programming",
    '.py': "/Users/techn/Downloads/Programming",
    '.sh': "/Users/techn/Downloads/Programming",
    '.swift': "/Users/techn/Downloads/Programming",
    '.html': "/Users/techn/Downloads/Programming",
    '.h': "/Users/techn/Downloads/Programming",
}

folder_to_track = '/Users/techn/Downloads'
folder_destination = '/Users/techn/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
    