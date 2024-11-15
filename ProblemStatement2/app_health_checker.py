import requests
import time
import logging

# Configuration
url = "https://www.youtube.com"  # Replace with your application URL
check_interval = 60  # Interval in seconds to check the application status
log_file = "application_health.log"  # Log file name

# Setup logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def check_application_status():
    try:
        response = requests.get(url, timeout=10)  # Set timeout to 10 seconds
        if response.status_code == 200:
            status_message = f"The application is UP. Status code: {response.status_code}"
            print(status_message)
            logging.info(status_message)
        else:
            status_message = f"The application is DOWN. Status code: {response.status_code}"
            print(status_message)
            logging.warning(status_message)
    except requests.exceptions.RequestException as e:
        error_message = f"The application is DOWN. Error: {e}"
        print(error_message)
        logging.error(error_message)

if __name__ == "__main__":
    print("Starting Application Health Checker...")
    logging.info("Starting Application Health Checker...")
    while True:
        check_application_status()
        time.sleep(check_interval)
