import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.processor import process_pcap
from app.config import load_config

config = load_config()

class PcapHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pcap"):
            print(f"[+] New PCAP detected: {event.src_path}")
            try:
                process_pcap(event.src_path)
                shutil.move(event.src_path, os.path.join(config["processed_folder"], os.path.basename(event.src_path)))
                print(f"[✓] Processed: {event.src_path}")
            except Exception as e:
                print(f"[!] Error: {e}")

def start_watch():
    os.makedirs(config["processed_folder"], exist_ok=True)
    observer = Observer()
    observer.schedule(PcapHandler(), path=config["watch_folder"], recursive=False)
    observer.start()
    print(f"👀 Watching {config['watch_folder']} for .pcap files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
