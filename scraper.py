import discord
from discord.ext import commands
import os
import aiohttp
import asyncio
import sys
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

meow = commands.Bot(command_prefix=".", intents=intents, help_command=None)


async def ensure_folders():
    if not os.path.exists("output"):
        os.mkdir("output")

    for folder in ["images", "videos", "files"]:
        path = os.path.join("output", folder)
        if not os.path.exists(path):
            os.mkdir(path)


def classify(name):
    ext = name.split(".")[-1].lower()
    if ext in ["png", "jpg", "jpeg", "gif", "webp"]:
        return "images"
    if ext in ["mp4", "mov", "webm", "m4v"]:
        return "videos"
    return "files"


async def download(att, current, total):
    folder = classify(att.filename)
    path = os.path.join("output", folder, att.filename)

    async with aiohttp.ClientSession() as session:
        async with session.get(att.url) as r:
            if r.status == 200:
                data = await r.read()
                with open(path, "wb") as f:
                    f.write(data)

    bar = int((current / total) * 40)
    bar_text = "[" + "#" * bar + "-" * (40 - bar) + "]"
    line = f"\r{bar_text} {current}/{total}  {att.filename}"
    sys.stdout.write(line)
    sys.stdout.flush()


async def scrape(channel, mode):
    await ensure_folders()

    all_attachments = []

    last = None
    while True:
        if last is None:
            batch = await channel.history(limit=100).flatten()
        else:
            batch = await channel.history(limit=100, before=last).flatten()

        if not batch:
            break

        for msg in batch:
            for att in msg.attachments:
                t = classify(att.filename)
                if mode == "1" and t != "images":
                    continue
                if mode == "2" and t != "videos":
                    continue
                all_attachments.append(att)

        last = batch[-1]

    total = len(all_attachments)
    if total == 0:
        print("no files found")
        return

    print(f"found {total} files\n")

    current = 0

    for att in all_attachments:
        current += 1
        await download(att, current, total)

    print("\n\ndone ^_^")



@meow.event
async def on_ready():
    print(f"logged in as {meow.user}\n")
    print("choose file type to scrape")
    print("1) images")
    print("2) videos")
    print("3) everything\n")

    mode = input("> ").strip()
    channel_id = input("channel id: ").strip()

    channel = meow.get_channel(int(channel_id))
    if not channel:
        print("invalid channel")
        await meow.close()
        return

    await scrape(channel, mode)
    await meow.close()


meow.run(TOKEN, bot=False)
