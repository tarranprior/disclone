<h1 align="center">Disclone</h1>
<p align="center"><img src="https://github.com/tarranprior/disclone/blob/main/assets/disclone.png" width="600" /></p>

<p align="center">Disclone is a self-host bot with Rclone integration, Gclone support and Google Drive automation utilities.</p>
<p align="center">Note: This project is still in development.</p>

## Introduction
For cloning all the things!

Gclone is a moderation of Rclone, a command-line program to manage files on cloud storage, and allows users to easily bypass [Google Drive](https://www.google.co.uk/drive/)'s daily data transfer limits by utilising and cycling through hundreds of service accounts.

Disclone brings this to [Discord](https://discord.com/), and allows for easy and collaborative management, combining all of Google Drive features and more, into an AIO tool.

By default, this tool will generate one hundred accounts, which is equal to approx. **75TB** of daily quota.

## Disclaimer
This tool was made for educational purposes.

## Features
- [ ] Rclone Utilities:
    - [ ] **new**: Create a new Google Drive remote
    - [X] **list**: List all existing remotes
    - [ ] **mkdir**: Make a path (directory) if it doesn't already exist

- [ ] Gclone Utilities:
    - [X] **clone**: Copy all files from source to destination (skipping identical files)
    - [ ] **move**: Move all files from source to destination
    - [ ] **sync**: Sync all files from source to destination
    - [ ] **md5**: Produces MD5 file hashes for all files in a directory
    - [ ] **empty**: Delete all files in a directory
    - [ ] **dedupe**: Remove duplicate files in a directory
    - [ ] **clean**: Remove any empty directories
    - [ ] **remove**: Remove a directory (and all files inside)

## Prerequisites
- Python 3.8 +
- [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool.)
- Service Accounts (*for Google Drive - auto-creation utility coming soon*)

## Tools
- [Disnake API Wrapper](https://github.com/DisnakeDev/disnake)
- [Rclone](https://rclone.org/)
- [Google Drive API](https://developers.google.com/drive/api)
- [Gclone](https://github.com/donwa/gclone)

## Installation
Preferably, you should use Poetry to run this bot for local development:

1. Clone the repository. `git clone https://github.com/tarranprior/disclone.git`

2. Navigate to the project folder. `cd disclone`

3. Install the dependencies:
   ```s
   poetry install
   ```
   Alternatively, you can install the dependencies using pip:
   ```s
   pip install -r requirements.txt
   ```

## Configuration
Update the values in .env.EXAMPLE and rename to .env.
```s
BOT_TOKEN='YOUR_BOT_TOKEN'
BOT_OWNER='YOUR_USER_ID'
```

## Usage
Under construction.

## Support
If you have any questions about this project, please submit an issue [here](https://github.com/tarranprior/disclone/issues).<br/>

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/tarranprior/disclone/blob/main/LICENSE) file for details.

## References
- Disnake Docs https://docs.disnake.dev/en/latest/index.html
- Discord Developer Applications https://discord.com/developers/applications