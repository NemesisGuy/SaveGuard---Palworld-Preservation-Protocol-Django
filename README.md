# SaveGuard - Palworld Preservation Protocol

SaveGuard is a Python script designed to automatically backup the save data for Palworld game servers running on Windows. It helps prevent loss of game progress in case of server restarts or crashes.

## Features

- Automatic periodic backup of Palworld save data.
- Customizable backup interval and file paths.
- Logging to track backup operations.

## Requirements

- Python 3.x
- `python-dotenv` library (install via `pip install python-dotenv`)

## Installation

1. Clone this repository to your local machine:

- git clone https://github.com/your-username/saveguard-palworld.git

2. Install the required dependencies:

- pip install python-dotenv

3. Configure the `.env` file with your desired save data and backup paths.

4. Run the script:

-  python saveguard.py


## Configuration

SaveGuard uses a `.env` file to manage configuration settings. You can customize the following settings:

- `SAVE_DATA_PATH`: Path to the Palworld save data directory.
- `BACKUP_PATH`: Path to the directory where backups will be stored.

## Usage

Once configured, SaveGuard will automatically run in the background and perform backups according to the specified interval. You can monitor the backup process by checking the logs in the `saveguard.log` file.

## Contributing

Contributions are welcome! If you'd like to contribute to the SaveGuard project, please follow these guidelines:

- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes and test them thoroughly
- Submit a pull request detailing your changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
