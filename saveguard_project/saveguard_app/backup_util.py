# backup_util.py
import shutil
import time
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="saveguard_config.env")

import shutil
import time
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="saveguard_config.env")

def backup_save_data(save_data_path, backup_path):
    try:
        # Get the current date and time
        current_datetime = time.strftime('%Y-%m-%d_%H-%M-%S')

        # Generate a human-readable backup folder name
        backup_folder_name = f"Backup_{current_datetime}"

        # Create the full backup folder path
        full_backup_path = os.path.join(backup_path, backup_folder_name)

        # Perform backup
        shutil.copytree(save_data_path, full_backup_path)
        
        # Log success message
        logging.info("Save data backed up successfully!")
    except Exception as e:
        # Log error message
        logging.error(f"Error backing up save data: {e}")
