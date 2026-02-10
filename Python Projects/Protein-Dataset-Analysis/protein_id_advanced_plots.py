import csv
from collections import Counter
from statistics import mean, median
from pathlib import Path

import matplotlib.pyplot as plt

FILENAME = r"C:\Users\PC\OneDrive\Desktop\protein_ids.csv"

def load_protein_ids(filename):

    protein_ids: list[str] = []

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if "protein_id" not in reader.fieldnames:
            raise ValueError("CSV must contain a 'protein_id' column")

        for row in reader:
            pid = row["protein_id"].strip()
            if pid:
                protein_ids.append(pid)

    return protein_ids


protein_ids = load_protein_ids(FILENAME)
print(f"Loaded {len(protein_ids)} protein IDs from {FILENAME}")

# Pre-computed basic data
lengths = [len(pid) for pid in protein_ids]
first_letters = [pid[0] for pid in protein_ids if len(pid) >= 1]
two_letter_prefixes = [pid[:2] for pid in protein_ids if len(pid) >= 2]


# Small helper so all images go into the same folder as the script
OUTPUT_DIR = Path(__file__).parent


def plot_length_histogram():
    """1) Histogram of ID lengths with mean & median lines."""
    m = mean(lengths)
    med = median(lengths)

    plt.figure()
    plt.hist(lengths, bins=20)
    plt.axvline(m, linestyle="--", label=f"Mean = {m:.2f}")
    plt.axvline(med, linestyle="-.", label=f"Median = {med:.2f}")
    plt.title("Protein ID Length Distribution")
    plt.xlabel("ID length (characters)")
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()

    out_path = OUTPUT_DIR / "plot1_length_histogram.png"
    plt.savefig(out_path)
    print(f"Saved {out_path}")
    plt.show()


def plot_first_letter_bar():
    """2) Bar chart of first letters, sorted by frequency."""
    counts = Counter(first_letters)
    # Sort by count (descending)
    letters, freqs = zip(*sorted(counts.items(), key=lambda x: x[1], reverse=True))

    plt.figure()
    plt.bar(letters, freqs)
    plt.title("Frequency of First Character in Protein IDs")
    plt.xlabel("First character")
    plt.ylabel("Count")
    plt.tight_layout()

    out_path = OUTPUT_DIR / "plot2_first_letter_frequency.png"
    plt.savefig(out_path)
    print(f"Saved {out_path}")
    plt.show()


def plot_top_prefixes():
    """3) Horizontal bar chart of top 15 2-letter prefixes."""
    counts = Counter(two_letter_prefixes)
    top15 = counts.most_common(15)

    prefixes = [p for p, _ in top15]
    freqs = [c for _, c in top15]

    prefixes = prefixes[::-1]
    freqs = freqs[::-1]

    plt.figure()
    plt.barh(prefixes, freqs)
    plt.title("Top 15 Most Common 2-Letter Prefixes")
    plt.xlabel("Count")
    plt.ylabel("2-letter prefix")
    plt.tight_layout()

    out_path = OUTPUT_DIR / "plot3_top_prefixes.png"
    plt.savefig(out_path)
    print(f"Saved {out_path}")
    plt.show()


def plot_first_letter_pie():
    """4) Pie chart of main starting letters (Q, P, A, other)."""
    counts = Counter(first_letters)

    q = counts.get("Q", 0)
    p = counts.get("P", 0)
    a = counts.get("A", 0)
    other = sum(c for letter, c in counts.items() if letter not in {"Q", "P", "A"})

    sizes = [q, p, a, other]
    labels = ["Q", "P", "A", "Other"]

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Distribution of First Character (Q / P / A / Other)")
    plt.tight_layout()

    out_path = OUTPUT_DIR / "plot4_first_letter_pie.png"
    plt.savefig(out_path)
    print(f"Saved {out_path}")
    plt.show()


def plot_running_fraction_q9():
    """
    5) Line plot of running fraction of IDs starting with 'Q9'.
       This shows whether 'Q9' IDs are spread evenly in the file.
    """
    total_seen = 0
    q9_seen = 0
    fractions = []

    for pid in protein_ids:
        total_seen += 1
        if pid.startswith("Q9"):
            q9_seen += 1
        fractions.append(q9_seen / total_seen)

    plt.figure()
    plt.plot(range(1, len(fractions) + 1), fractions)
    plt.title("Running Fraction of IDs Starting with 'Q9'")
    plt.xlabel("Index in dataset")
    plt.ylabel("Fraction of 'Q9' IDs")
    plt.tight_layout()

    out_path = OUTPUT_DIR / "plot5_running_fraction_Q9.png"
    plt.savefig(out_path)
    print(f"Saved {out_path}")
    plt.show()

if __name__ == "__main__":
    plot_length_histogram()
    plot_first_letter_bar()
    plot_top_prefixes()
    plot_first_letter_pie()
    plot_running_fraction_q9()

