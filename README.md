# Discord Attachment Scraper |Educational Purposes Only|

This is a small Python tool that lets you scrape images, videos, and other attachments from a Discord channel your user has access to. It runs in the terminal, asks what you want to scrape, and then pulls everything from newest to oldest while showing a clean progress bar.

It’s meant to be simple to use and easy to understand.

---

## How it works
When you start the script, it connects to Discord using your user token from the `.env` file. After it logs in, it asks you two things:

1. What type of files you want to scrape  
   - Images  
   - Videos  
   - Everything  

2. The channel ID you want to scrape from

Once you enter those, the self-bot walks through the entire message history of that channel. It collects all attachments that match your filter, figures out how many files there are total, and then starts downloading them one by one.

The progress bar updates on the same line, so your console doesn’t flood with text. You’ll always see the current file being downloaded, along with a counter like:

# Discord Attachment Scraper — Installation Guide

---

## 1. Install Python (correct version)
You need Python **3.8, 3.9, or 3.10**.  
Newer versions won’t work with discord.py 1.7.3.

You can download Python 3.10 here:
https://www.python.org/downloads/release/python-31011/

During installation, make sure to check:

---

## 2. Install the required packages
Open your terminal in the project folder and run: ` pip install discord.py==1.7.3 aiohttp python-dotenv `


When it logs in, it’ll ask:

1. What type of files you want to scrape  
2. Which channel ID you want to scrape from  

After that, it builds a list of everything and starts the progress bar while downloading.

---

## 6. Where your files appear
A folder called `output/` will show up in the project directory.

Inside it:

output/
images/
videos/
files/

