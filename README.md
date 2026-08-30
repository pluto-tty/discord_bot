# Discord Accountability Bot

A lightweight Discord bot that sends scheduled accountability check-ins throughout the day.

The idea is simple: instead of relying on motivation or remembering to check in, the bot sends a short message at scheduled times to prompt you to pause, refocus, and reflect.

## Features

* Morning, midday, and evening check-ins
* Different message pools for different days of the week
* Randomized messages for variety
* Weekend-specific behavior
* Runs automatically with GitHub Actions
* Uses Discord's API to send messages
* No database required
* Messages are stored locally in `messages.py`
* Timezone can be configured
* Personal messages can be added without changing the bot logic

## Project structure

```text
discord-accountability-bot/
├── .github/
│   └── workflows/
│       └── accountability.yml
├── bot.py
├── messages.py
├── schedule.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### `bot.py`

Handles the Discord connection and sends the selected message.

It reads the Discord bot token and channel ID from environment variables rather than storing credentials in the source code.

### `schedule.py`

Controls which message pool is used for each day and time period.

The week is divided into:

* Monday–Thursday
* Friday
* Saturday
* Sunday

### `messages.py`

Contains the actual message pools.

These are intentionally kept separate from the bot logic so they can easily be replaced with your own messages.

### `accountability.yml`

Controls when GitHub Actions runs the bot.

GitHub Actions cron schedules use UTC in this project. Change the cron expressions in this file to create your preferred schedule.

## Requirements

You need:

* Python 3.12 or newer
* A Discord account
* A Discord application/bot
* A Discord server where the bot can send messages
* A GitHub repository with GitHub Actions enabled

## Setting up the Discord bot

Create a Discord application and create a bot for it.

Invite the bot to your server with permission to view and send messages in the channel you want to use.

You will need two values:

* Discord bot token
* Discord channel ID

Never publish your bot token.

## GitHub Actions setup

After pushing the project to GitHub, add the following repository secrets:

```text
DISCORD_BOT_TOKEN
DISCORD_CHANNEL_ID
```

You can optionally add:

```text
BOT_TIMEZONE
```

For example:

```text
America/New_York
```

or:

```text
Europe/London
```

or:

```text
Asia/Karachi
```

If `BOT_TIMEZONE` is not provided, the bot defaults to UTC.

### Adding repository secrets

In your GitHub repository:

**Settings → Secrets and variables → Actions → New repository secret**

Add each secret separately.

Do not put the actual values inside `bot.py`, `messages.py`, or the workflow file.

## Customizing the schedule

Open:

```text
.github/workflows/accountability.yml
```

The default schedule is:

```yaml
schedule:
  - cron: "0 7 * * *"    # Morning
  - cron: "0 12 * * *"   # Midday
  - cron: "0 20 * * *"   # Evening
```

These times are in UTC.

Cron uses the following format:

```text
minute hour day-of-month month day-of-week
```

For example:

```yaml
- cron: "30 8 * * *"
```

runs at 08:30 UTC every day.

If you want to use another timezone, convert the desired local time to UTC before entering the cron expression.

## Customizing the messages

Open:

```text
messages.py
```

Replace the example messages with your own.

For example:

```python
MORNING_MOTIVATION = [
    "Start with the thing that matters.",
    "What would make today a good day?",
]
```

You can add as many messages as you like.

The bot randomly selects from the appropriate pool, which prevents the same message from appearing every day.

## Running locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set the required environment variables:

```text
DISCORD_BOT_TOKEN
DISCORD_CHANNEL_ID
```

Then run one of the available periods:

```bash
python bot.py morning
```

```bash
python bot.py midday
```

```bash
python bot.py evening
```

The bot sends one message and exits.

## Why GitHub Actions?

The bot does not need to run continuously.

GitHub Actions can start the Python script at the scheduled time, send the Discord message, and then shut down the runner.

This keeps the project simple and avoids the need for a permanently running server.

## Contributing

Feel free to fork the project, customize the message pools, adjust the schedule, or improve the bot.

Pull requests and ideas are welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
