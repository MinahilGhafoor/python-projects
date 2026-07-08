import shutil
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

SOURCE = r"C:\Users\Acer\OneDrive\Desktop\git projects\Auto File Backup Script\WatchFolder"
BACKUP = r"C:\Users\Acer\OneDrive\Desktop\git projects\Auto File Backup Script\Backup Folder"


logging.basicConfig(
    filename='logs/backup.log',
    level=logging.INFO,
    format= "%(asctime)s - %(message)s"
)

class BackupHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            shutil.copy2(event.src_path, BACKUP)
            logging.info(f"Modified file backed up: {event.src_path}")
            print(f"Updated backup: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            shutil.copy2(event.src_path, BACKUP)
            logging.info(f'New File backed up: {event.src_path}')
            print(f"Backed Up: {event.src_path}")


def main():
    handler = BackupHandler()
    observer = Observer()
    observer.schedule(handler, SOURCE, recursive=False)
    observer.start()
    print(f"👀 Watching {SOURCE}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

main()