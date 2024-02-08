# SaveGuard - Palworld Preservation Protocol (Django)

SaveGuard is a Django-based application designed to automate the backup process for Palworld game data. It allows users to configure backup settings and schedule automatic backups of their game data.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NemesisGuy/SaveGuard---Palworld-Preservation-Protocol-Django.git
```

### 2. Navigate to the Project Directory

```bash
cd SaveGuard---Palworld-Preservation-Protocol-Django
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

- Create a `.env` file in the project root directory.
- Define the following environment variables in the `.env` file:

    ```
    SAVE_DATA_PATH="<path_to_save_data>"
    BACKUP_PATH="<path_to_backup_directory>"
    ```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Visit `http://127.0.0.1:8000/` in your web browser to access the SaveGuard application.

## Deployment

To deploy SaveGuard to a production environment, follow these general steps:

1. **Choose a Hosting Provider**: Select a hosting provider that supports Django applications. Popular options include Heroku, AWS, and DigitalOcean.

2. **Configure Server**: Set up a server environment with the necessary software dependencies, including Python, Django, and any database required (e.g., PostgreSQL).

3. **Set Environment Variables**: Define environment variables for your production environment, including database credentials and any other sensitive information.

4. **Configure Static Files and Media**: Set up serving static files and media files using a web server or cloud storage service.

5. **Collect Static Files**: Run the Django `collectstatic` command to collect static files into one directory.

6. **Configure Web Server**: Configure your web server (e.g., Nginx, Apache) to serve the Django application.

7. **Enable HTTPS**: Enable HTTPS to secure communication between the client and server.

8. **Automate Deployment**: Set up a deployment pipeline using tools like GitLab CI/CD, GitHub Actions, or Jenkins for automated deployment.

## Contributing

Contributions are welcome! If you'd like to contribute to the SaveGuard project, please follow these guidelines:

- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes and test them thoroughly
- Submit a pull request detailing your changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshots

![Screenshot - Home](Screenshots\image-home.png)

![Screenshot - Backup Settings](screenshots/image-backup-settings.png)  

![Screenshot - Backups Status](screenshots/image-backup-status.png) 