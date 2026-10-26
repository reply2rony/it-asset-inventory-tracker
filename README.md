# IT Asset Inventory Tracker

A simple way to keep track of office IT equipment without buying asset software.

## What it does
- Keeps one row per asset: what it is, who has it, where it is, and its condition.
- Flags assets that are due for a check, and lists assets that are unassigned.
- Works in Excel (open the CSV) or with the small Python script, which prints a summary.

## Files
- `assets-sample.csv` — sample data only. Replace it with your own list.
- `scripts/check_inventory.py` — reads the CSV and prints: total assets, assets by condition, unassigned assets, and assets due for a check.

## How to use it (Excel only, no code)
1. Open `assets-sample.csv` in Excel.
2. Replace the sample rows with your real assets, keeping the same headings.
3. Filter the Status column to find assets due for a check.

## How to use it (with Python)
1. Install Python 3 (python.org) — no extra packages needed.
2. In a terminal, go to this folder and run: `python scripts/check_inventory.py`
3. Read the summary it prints. It does not change your CSV.

## Sample data note
All names, serial numbers, and locations in the sample file are made up.
Never put real employee data or real serial numbers in a public repository.

## Note on skills
Python is labelled "Learning" in the author's profile. This script is an intentionally short, commented starter template for IT asset work, and the Excel/CSV version works without it.
