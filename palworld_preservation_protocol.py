import logging
import shutil
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Paths
save_data_path = os.getenv("SAVE_DATA_PATH")
backup_path = os.getenv("BACKUP_PATH")

# Configure logging
logging.basicConfig(filename='saveguard.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to perform backup
def backup_save_data():
    try:
        shutil.copytree(save_data_path, f"{backup_path}/save_backup_{time.strftime('%Y%m%d_%H%M%S')}")
        logging.info("Save data backed up successfully!")
    except Exception as e:
        logging.error(f"Error backing up save data: {e}")

# Run backup every hour
while True:
    backup_save_data()
    time.sleep(3600)  # Sleep for 1 hour
