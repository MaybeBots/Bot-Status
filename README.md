# Telegram Bot Status Repository

Monitor your bots' uptime and CPU usage effortlessly with this Telegram bot. It refreshes automatically, ensuring your bots are always active. Runs 24/7 for your convenience.

[![Made with Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![Stars](https://img.shields.io/github/stars/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status/stargazers)
[![Forks](https://img.shields.io/github/forks/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status/network/members)
[![Watchers](https://img.shields.io/github/watchers/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status/watchers)
[![Repository Size](https://img.shields.io/github/repo-size/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status)
[![Contributors](https://img.shields.io/github/contributors/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/MaybeBots/Bot-Status?style=for-the-badge)](https://github.com/MaybeBots/Bot-Status/issues)

## Config Vars
1. `API_ID` : Telegram API_ID, obtain it from my.telegram.org/apps
2. `API_HASH` : Telegram API_ID, obtain it from my.telegram.org/apps
3. `SESSION_STRING` : A valid Pyrogram session string, get it from [@MaybexSessionBot](https://t.me/MaybexSessionBot)
4. `BOT_TOKEN` : A valid bot token, obtain it from [@BotFather](https://t.me/BotFather)
5. `BOT_LIST` : Your bot username list without '@' (Example: Maybexsessionbot MaybexHackBot)
6. `CHANNEL_OR_GROUP_ID` : Your channel's or group's Telegram id (Example: -1001246808642)
7. `MESSAGE_ID` : Telegram id of message from your channel or group (Example: 10)
8. `OWNER_ID` : Owner id (Example: 1357907531 2468097531 3579864213)
9. `TIME_ZONE`: Your time zone (Example: Asia/Kolkata)

## Tutorial 

### Method 1 (Easy)
1. Install using pip3 in your bot (Pyrogram or Telethon):

**For Pyrogram**
```
pip3 install git+https://github.com/maybebots/bot-status.git@pyro
```

**For Telethon**
```
pip3 install git+https://github.com/maybebots/bot-status.git@tele
```

2. Import the Client Class:

**For Pyrogram**
```python
from PyroStatus import PyroClient
```

**For Telethon**
```python
from TeleStatus import TeleClient
```

3. Replace the normal Client:

**For Pyrogram**
```python
app = PyroClient(
    name="bot",
    api_id=69696,
    api_hash="",
    bot_token=""
)
```

**For Telethon**
```python
app = TeleClient(
    "bot",
    api_id,
    api_hash,
).start(bot_token="")
```

4. Deploy this repo!

### Method 2 (Manual)

1. Add this code snippet at the beginning of your `__init__.py` file:
```python
import time

start_time = time.time()
```

2. Copy the provided code into your repository (in plugins directory or wherever your plugins exist).

3. Add the bot to your channel and make it admin.

## Deployment Methods

### Heroku

To deploy on Heroku:

1. Fork this repository.

2. Click the Deploy button below:
    
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MaybeBots/Bot-Status)

### Vps

To deploy on a VPS:

1. Update and upgrade your system packages:
```
sudo apt-get update && sudo apt-get upgrade -y
```

2. Clone the repository and navigate to the project directory:
```
git clone https://github.com/maybebots/Bot-Status && cd Bot-Status
```

3. Install the required packages:
```
pip3 install -U -r requirements.txt
```

4. Create .env using example.env:
```
cp example.env .env
```

5. Open the .env file using **vi .env**.

6. Edit the vars by pressing **I** on the keyboard.

7. After editing, save the file using **ctrl + c** then **:wq**.

8. Run the script using Python 3:
```
python3 main.py
```

## Support
- [Channel](https://t.me/Maybebots)
- [Group](https://t.me/MaybeBotsSupport)

## Credits
- [TeLe TiPs](https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)
- [Pyrogram](https://github.com/pyrogram/pyrogram)
