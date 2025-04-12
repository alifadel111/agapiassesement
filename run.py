import subprocess
import threading
import time

def start_monitoring():
    while True:
        subprocess.run(["python", "app/monitor.py"])
        time.sleep(300)  # check every 5 minutes

def start_api():
    subprocess.run(["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"])

monitor_thread = threading.Thread(target=start_monitoring)
monitor_thread.start()

start_api()
