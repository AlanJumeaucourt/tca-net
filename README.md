# TCA-Net Discord Bot

![Test Status](https://github.com/AlanJumeaucourt/tca-net/actions/workflows/on_push.yml/badge.svg)

## Overview

TCA-Net is a Discord bot created for class-related activities. This bot offers various features to help manage your classes and engage with your classmates.

## Key Features

- **Course Reminders**: Receive timely reminders for your upcoming classes.

- **Homework Notifications**: Get notified about your homework assignments.

- **Croissant Duty**: Easily manage and track who is responsible for buying croissants for the class.

- **Dynamic Name Changes**: The bot can change the name of a user named Augusto based on the time of day, adding a touch of fun to your Discord server.

- **Ending Capitalism Era**: A humorous touch to lighten the mood.

## Getting Started

To use the TCA-Net Discord bot, you'll need to set up a `.env` file with the following variables:

**Mandatory Variables:**
- `authToken`: This token is required for scraping the calendar. You can find it in the header of the request when loading "tc-net."
- `discordToken`: This is the Discord API token for the bot.
- `channelId`: Specify the ID of the Discord channel where the bot will send reminders.

**Optional Variable:**
- `delta`: Set the number of minutes before the bot sends reminders for the next course. The default is 15 minutes.

```bash
authToken=Dht5bWVhdWNvdTpNMWNrM3lpbnNhLmZy
discordToken=MTE1OTU5MTU0MzUxOTMxNDA5Mg.Gggz7B.hcSKPwda8GCysq7TRI7xv_HW0_7HyVnz3jgd25
channelId=776468108038373573
delta=32400
# Hint: Don’t try it! These keys have been randomly generated ;-)
```

## Installation

To get started with TCA-Net, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Create a `.env` file with the mandatory and optional variables as described above.
4. Run the `crawler.py` script to start the scraping process.
5. Run the `discordBot.py` script to start the bot.

Now you're ready to enjoy the features of the TCA-Net Discord bot for your classes!

## How it works

### files descriptions :
**crawler.py** will scrap the calendar based on the "tc-net" site.
It will create 3 files wich contain the objects :
- professors.pkl : contains the list of professors
- rooms.pkl : contains the list of rooms
- courses.pkl : contains the list of courses

**discordBot.py** will use the 3 files as a DB to send the correct reminder messages on discord.



If you have questions or encounter any issues, feel free to reach out to the project maintainers.
