import csv

FILENAME = r"C:\Users\PC\OneDrive\Desktop\protein_ids.csv"
protein_ids = []
with open(FILENAME, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # Make sure the CSV has the right column
    if "protein_id" not in reader.fieldnames:
        raise ValueError("CSV file must have a column named 'protein_id'.")

    for row in reader:
        pid = row["protein_id"].strip()
        if pid:
            protein_ids.append(pid)

print("Protein ID Explorer (simple version)")
print(f"Loaded file: {FILENAME}")
print(f"Total IDs: {len(protein_ids)}")
print()

print("First 10 protein IDs:")
for pid in protein_ids[:10]:
    print(" ", pid)
print()

prefix = input("Enter a prefix to search (e.g. P0, Q9): ").strip()

matches = [pid for pid in protein_ids if pid.startswith(prefix)]

print()
print(f"Found {len(matches)} IDs starting with '{prefix}':")


for pid in matches[:20]:
    print(" ", pid)

if len(matches) > 20:
    print(f"... and {len(matches) - 20} more")
