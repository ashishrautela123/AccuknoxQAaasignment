import psutil
import time
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # CPU usage threshold (%)
MEMORY_THRESHOLD = 80  # Memory usage threshold (%)
DISK_THRESHOLD = 80  # Disk usage threshold (%)

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")

    # Check Memory usage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")

    # Check Disk usage
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")

    # Log running processes
    processes = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent'])]
    logging.info(f"Running processes: {processes}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(60)  # Run the check every 60 seconds
