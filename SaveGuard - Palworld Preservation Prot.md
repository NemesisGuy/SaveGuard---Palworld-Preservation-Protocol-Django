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

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve SaveGuard.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



