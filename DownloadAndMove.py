import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/danie/Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"{event.src_path} was created")
    #2_on_deleted
    def on_deleted(self, event):
        print(f"{event.src_path} was deleted")        
    #3_on_modified
    def on_modified(self, event):
        print(f"{event.src_path} was modified")
    #4_on_moved
    def on_moved(self, event):
        print(f"{event.src_path} was moved")
        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt

try:
    while True:
        time.sleep(2)
        print("Executing...")
except keyboardInterrupt:
    print("Stopped")
    observer.stop()





