# saveguard_app/views.py

import os
import re
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BackupSettingsForm
from .backup_util import backup_save_data
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'saveguard_config.env')
try:
    load_dotenv(dotenv_path=dotenv_path)
except Exception as e:
    print("Error loading .env file:", e)

# Define global variable for environment variables
env_vars = dotenv_values(dotenv_path=dotenv_path)

# Define global variables for save data path and backup path
save_data_path = env_vars.get("SAVE_DATA_PATH")
backup_path = env_vars.get("BACKUP_PATH")

# Optionally, modify paths if necessary
save_data_path = re.sub(r'\s+', ' ', save_data_path.strip())
backup_path = re.sub(r'\s+', ' ', backup_path.strip())

def home(request):
    return render(request, 'home.html')

def backup_status(request):
    print("Backup status view function is being called.")
    print("Loaded environment variables:", env_vars)

    # Get the backup path from the environment variables
    backup_path = env_vars.get("BACKUP_PATH")

    # If the backup path is not set, handle the error accordingly
    if not backup_path:
        print("Backup path is not set.")
        return render(request, 'backup_status.html', {'error_message': 'Backup path is not set.'})

    # If the backup path exists, list the folders inside it
    backup_folders = []
    if os.path.exists(backup_path):
        print("Backup directory exists:", backup_path)
        backup_folders = [folder for folder in os.listdir(backup_path) if os.path.isdir(os.path.join(backup_path, folder))]
        print("Backup folders:", backup_folders)
    else:
        print("Backup directory does not exist:", backup_path)

    return render(request, 'backup_status.html', {'backup_folders': backup_folders})

def perform_backup():
    global save_data_path, backup_path

    # Check if paths exist
    if not os.path.exists(save_data_path):
        print("ERROR: Save data path does not exist.")
        return
    if not os.path.exists(backup_path):
        print("ERROR: Backup path does not exist.")
        return

    # Optionally, get absolute paths
    save_data_path = os.path.abspath(save_data_path)
    backup_path = os.path.abspath(backup_path)

    print("Save data path:", save_data_path)
    print("Backup path:", backup_path)

    # Call the backup function with the corrected paths
    backup_save_data(save_data_path, backup_path)

def backup_now(request):
    perform_backup()  # Perform the backup immediately
    return redirect('settings')

def schedule_backup(request):
    if request.method == 'POST':
        form = BackupSettingsForm(request.POST)
        if form.is_valid():
            frequency = form.cleaned_data['frequency']
            
            # Implement different backup schedules based on frequency
            if frequency == 'hourly':
                while True:
                    time.sleep(3600)  # Sleep for 1 hour (3600 seconds) between backups
                    perform_backup()
            elif frequency == 'daily':
                # Implement daily backup logic here
                pass
            elif frequency == 'weekly':
                # Implement weekly backup logic here
                pass
    else:
        form = BackupSettingsForm()
    
    return render(request, 'schedule_backup.html', {'form': form})

def settings(request):
    env_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'saveguard_config.env')

    if request.method == 'POST':
        form = BackupSettingsForm(request.POST)
        if form.is_valid():
            with open(env_file_path, 'w') as f:
                f.write(f'SAVE_DATA_PATH="{form.cleaned_data["save_data_path"]}"\n')
                f.write(f'BACKUP_PATH="{form.cleaned_data["backup_path"]}"\n')

            os.environ['SAVE_DATA_PATH'] = form.cleaned_data['save_data_path']
            os.environ['BACKUP_PATH'] = form.cleaned_data['backup_path']
            return redirect('settings')
    else:
        current_settings = {}
        with open(env_file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                current_settings[key.strip()] = value.strip().strip('"')
        
        form = BackupSettingsForm(initial=current_settings)
    return render(request, 'settings.html', {'form': form, 'current_settings': current_settings})
