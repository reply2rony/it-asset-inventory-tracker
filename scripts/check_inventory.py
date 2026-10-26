# IT Asset Inventory Tracker — summary script
# Reads assets-sample.csv and prints a simple summary.
# It does not change the file. Sample data only.

import csv
from collections import Counter
from pathlib import Path

# Find the CSV file next to this script's parent folder.
CSV_FILE = Path(__file__).resolve().parent.parent / "assets-sample.csv"

def main():
    # Open the CSV and read every row as a dictionary.
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Total assets: {len(rows)}")
    print()

    # Count assets by their Status column (In use, In stock, Needs repair).
    print("Assets by status:")
    for status, count in Counter(row["Status"] for row in rows).items():
        print(f"  {status}: {count}")
    print()

    # List assets that have no person assigned yet.
    print("Unassigned assets:")
    unassigned = [row for row in rows if row["AssignedTo"].strip() == "Unassigned"]
    if unassigned:
        for row in unassigned:
            print(f"  {row['AssetID']} — {row['Type']} ({row['BrandModel']}) at {row['Location']}")
    else:
        print("  None — every asset has a person assigned.")
    print()

    # List assets due for a check before the end of 2026 (sample cutoff).
    print("Assets with a check date in 2026:")
    for row in rows:
        if row["NextCheckDate"].startswith("2026"):
            print(f"  {row['AssetID']} — check by {row['NextCheckDate']} ({row['Status']})")

if __name__ == "__main__":
    main()
