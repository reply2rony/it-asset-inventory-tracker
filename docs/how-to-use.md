# How to use the IT Asset Inventory Tracker

> Note: this short guide was written to match the README. The package draft lists this file in the folder structure but does not give its full text.

## Excel only (no code)
1. Open `assets-sample.csv` in Excel.
2. Replace the sample rows with your own list, keeping the same headings:
   AssetID, Type, BrandModel, SerialNumber, AssignedTo, Location, Status, PurchaseYear, NextCheckDate.
3. Filter the Status column to find assets due for a check, and filter AssignedTo for "Unassigned".

## With the Python script
1. Install Python 3 — no extra packages needed.
2. From this project's folder, run: `python scripts/check_inventory.py`
3. Read the printed summary: total assets, assets by status, unassigned assets, and assets with a check date in 2026.
4. The script does not change your CSV.

## Sample data rule
All names, serial numbers, and locations in the sample file are made up. Never put real employee data or real serial numbers in a public repository.
