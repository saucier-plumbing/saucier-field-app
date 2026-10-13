# Saucier Field Tickets

Phone web app for Saucier Plumbing (Holden, LA): flat-rate price book, job tickets, weekly hours, and office exports for QuickBooks Online invoices and the Weekly Piece Pay Record (ADP payroll).

## What is published
The files at the top of this repository are the live app. Netlify publishes them as-is (no build step):

- `index.html` - the app
- `prices.json` - the price book; phones load it on start, so updating it updates every phone
- `manifest.json`, `sw.js`, `icon.svg` - home-screen icon and offline use

## Changing the app
- Prices only: replace `prices.json` (the app's Office > Settings > Update prices makes this file).
- Anything else: edit `source/app_template.html` (or the built-in price data in `source/data.json`), then run `python3 source/build.py` to regenerate `index.html` and the other files.

The field and office guide is "Saucier Field Tickets Guide - Part 3.docx" in the project files.
