import os
from django.shortcuts import render
from dotenv import dotenv_values

def backup_status(request):
    print("Backup status view function is being called.")  # Add debug print statement
    # Load environment variables from .env file
    env_vars = dotenv_values("saveguard_config.env")

    # Get the backup path from the environment variables
    backup_path = env_vars.get("BACKUP_PATH")

    # If the backup path is not set, handle the error accordingly
    if not backup_path:
        print("Backup path is not set.")  # Add debug print statement
        return render(request, 'backup_status.html', {'error_message': 'Backup path is not set.'})

    # If the backup path exists, list the folders inside it
    backup_folders = []
    if os.path.exists(backup_path):
        print("Backup directory exists:", backup_path)  # Add debug print statement
        backup_folders = [folder for folder in os.listdir(backup_path) if os.path.isdir(os.path.join(backup_path, folder))]
        print("Backup folders:", backup_folders)  # Add debug print statement
    else:
        print("Backup directory does not exist:", backup_path)  # Add debug print statement

    return render(request, 'backup_status.html', {'backup_folders': backup_folders})
