import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import discord

import schedule


TIMEZONE = ZoneInfo(os.getenv("BOT_TIMEZONE", "UTC"))

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")


def get_current_day():
    return datetime.now(TIMEZONE).weekday()


def send_message(period):
    day = get_current_day()
    text = schedule.get_message(day, period)

    if not text:
        print(f"No message configured for day={day}, period={period}")
        return

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(int(CHANNEL_ID))

        if channel is None:
            print("Could not find the Discord channel.")
            await client.close()
            return

        await channel.send(text)
        print(f"Sent {period} message for day {day}.")
        await client.close()

    client.run(TOKEN)


def main():
    if not TOKEN:
        raise RuntimeError("DISCORD_BOT_TOKEN is not set.")

    if not CHANNEL_ID:
        raise RuntimeError("DISCORD_CHANNEL_ID is not set.")

    if len(sys.argv) != 2:
        print("Usage: python bot.py <morning|midday|evening>")
        sys.exit(1)

    period = sys.argv[1]

    valid_periods = {
        "morning",
        "midday",
        "evening",
    }

    if period not in valid_periods:
        print(f"Invalid period: {period}")
        sys.exit(1)

    send_message(period)


if __name__ == "__main__":
    main()
