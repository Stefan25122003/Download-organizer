import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")  
DESTINATION_FOLDER = os.path.expanduser("~/Sorted_Files")

if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        file_extension = file_name.split(".")[-1].lower() 
        destination_path = os.path.join(DESTINATION_FOLDER, file_extension)
        
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        
        shutil.move(file_path, os.path.join(destination_path, file_name))
        print(f"Mutat: {file_name} -> {destination_path}")

observer = Observer()
event_handler = FileHandler()
observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
observer.start()

try:
    print("Maybe download something...")
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
