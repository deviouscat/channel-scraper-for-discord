# Discord Attachment Scraper

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

