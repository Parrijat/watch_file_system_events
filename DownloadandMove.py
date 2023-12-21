import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "Downloads"


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} was modified")

    def on_moveed(self, event):
        print(f"Hey, {event.src_path} was moved")
        
    def on_deleted(self, event):
        print(f"Oops! someone deleted {event.src_path}")


event_handler = FileMovementHandler()


observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    
