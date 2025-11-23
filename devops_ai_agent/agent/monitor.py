import psutil

def health_check():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return f"""
CPU: {cpu}%
Memory: {mem}%
Disk: {disk}%
"""
