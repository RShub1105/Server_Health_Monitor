import psutil
from datetime import datetime

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk

def log_stats(cpu, memory, disk, logfile="logs/system_log.txt"):
    with open(logfile, "a") as f:
        f.write(f"{datetime.now()} | CPU={cpu}% | Memory={memory}% | Disk={disk}%\n")