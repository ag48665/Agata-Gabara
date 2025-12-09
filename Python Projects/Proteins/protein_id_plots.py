import csv
from collections import Counter
import matplotlib.pyplot as plt

FILENAME = r"C:\Users\PC\OneDrive\Desktop\protein_ids.csv"

protein_ids = []

with open(FILENAME, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    if "protein_id" not in reader.fieldnames:
        raise ValueError("CSV file must contain a 'protein_id' column.")

    for row in reader:
        pid = row["protein_id"].strip()
        if pid:
            protein_ids.append(pid)

print(f"Loaded {len(protein_ids)} protein IDs")

lengths = [len(pid) for pid in protein_ids]
first_letters = [pid[0] for pid in protein_ids if len(pid) >= 1]
two_letter_prefixes = [pid[:2] for pid in protein_ids if len(pid) >= 2]

plt.figure()
plt.hist(lengths, bins=20)
plt.title("Protein ID Length Distribution")
plt.xlabel("ID length (number of characters)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

first_letter_counts = Counter(first_letters)

plt.figure()
plt.bar(list(first_letter_counts.keys()), list(first_letter_counts.values()))
plt.title("Frequency of First Character in Protein IDs")
plt.xlabel("First character")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

prefix_counts = Counter(two_letter_prefixes)
top20 = prefix_counts.most_common(20)

prefixes = [p[0] for p in top20]
counts = [p[1] for p in top20]

plt.figure()
plt.bar(prefixes, counts)
plt.title("Top 20 Most Common 2-Letter Prefixes")
plt.xlabel("2-letter prefix")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(range(len(lengths)), lengths, s=2)
plt.title("Protein ID Length by Index")
plt.xlabel("Row index in dataset")
plt.ylabel("ID length")
plt.tight_layout()
plt.show()

plt.figure()
plt.boxplot(lengths)
plt.title("Boxplot of Protein ID Lengths")
plt.ylabel("ID length")
plt.tight_layout()
plt.show()
