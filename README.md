<h1 align="center">Disclone</h1>
<p align="center"><img src="https://github.com/tarranprior/disclone/blob/main/assets/disclone.png" width="600" /></p>

<p align="center">Disclone is a self-host bot which uses Rclone/Gclone integration for collaborative Google Drive automation.</p>
<p align="center">Note: This project is still in early development.</p>

![GitHub License](https://img.shields.io/github/license/:tarranprior/:disclone)

## Introduction
For cloning all the things!

Gclone is a modded version of Rclone, a command-line program to manage files on cloud storage, and allows users to bypass [Google Drive](https://www.google.co.uk/drive/)'s daily data transfer limits by utilising and cycling through hundreds of Google service accounts.

Disclone brings this to [Discord](https://discord.com/) with slash integration, and allows for easy and collaborative management, combining all of Google Drive features and more, into an AIO (all-in-one) and easy-to-use tool.

By default, this tool will generate x 100 service accounts, which is equal to approx. 75TB of daily quota.

## Disclaimer
This tool was made for educational purposes.

## Features
- [ ] Rclone Utilities:
    - [X] `/remotes`: Lists all existing remotes
    - [ ] `/new`: Creates a new Google Drive remote
    - [ ] `/mkdir`: Creates a new directory if it doesn't already exist

- [ ] Gclone Utilities:
    - [X] `/clone`: Copies all files from source to destination (skipping identical files)
    - [ ] `/move`: Moves all files from source to destination
    - [ ] `/sync`: Syncs all files from source to destination
    - [ ] `/md5`: Produces MD5 file hashes for all files in a directory
    - [ ] `/empty`: Empties all files in a directory
    - [ ] `/dedupe`: Removes duplicate files in a directory
    - [ ] `/clean`: Removes any empty directories
    - [ ] `/rmdir`: Removes a directory (and all files inside)

## Prerequisites
- Python 3.8 +
- [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool.)
- Service accounts (for Google Drive)
- `rclone.exe` and `gclone.exe` executable files.

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

## Support
If you have any questions about this project, please submit an issue [here](https://github.com/tarranprior/disclone/issues).<br/>

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/tarranprior/disclone/blob/main/LICENSE) file for details.

## References
- Disnake Docs https://docs.disnake.dev/en/latest/index.html
- Discord Developer Applications https://discord.com/developers/applications
