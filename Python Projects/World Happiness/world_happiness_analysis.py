import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


CSV_FILE = "world_happiness_report.csv"
SAVE_DIR = r"C:/Users/PC/OneDrive/Desktop/Python Projects/World Happiness"


def save_and_show(filename, show=False):
    """Save charts to desktop folder (no pop-ups)."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)

    full_path = os.path.join(SAVE_DIR, filename)
    plt.savefig(full_path, bbox_inches="tight")
    print(f"Saved: {full_path}")

    if show:
        plt.show()
    else:
        plt.close()


def load_data():
    df = pd.read_csv(CSV_FILE)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    return df


# ===============================
# 2. ADVANCED STATISTICS
# ===============================


def basic_overview(df):
    print("\n=== BASIC OVERVIEW ===")
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print("Years:", sorted(df["year"].unique()))
    print("\n--- Descriptive statistics ---")
    print(df.describe().round(3))


def stats_by_year(df):
    print("\n=== HAPPINESS BY YEAR ===")
    yearly = (
        df.groupby("year")["Happiness Score"]
        .agg(["mean", "median", "min", "max", "std"])
        .round(3)
    )
    print(yearly)


def stats_by_region(df):
    print("\n=== BY REGION ===")
    reg = (
        df.groupby("Region")["Happiness Score"]
        .agg(["mean", "median", "min", "max", "std", "count"])
        .sort_values("mean", ascending=False)
        .round(3)
    )
    print(reg)


def top_bottom(df, year=None, n=10):
    if year is None:
        year = df["year"].max()

    d = df[df["year"] == year]

    print(f"\n=== TOP {n} COUNTRIES ({year}) ===")
    print(
        d.sort_values("Happiness Score", ascending=False)[
            ["Country", "Region", "Happiness Score"]
        ].head(n)
    )

    print(f"\n=== BOTTOM {n} COUNTRIES ({year}) ===")
    print(
        d.sort_values("Happiness Score", ascending=True)[
            ["Country", "Region", "Happiness Score"]
        ].head(n)
    )


def compute_changes(df):
    df2 = df.sort_values(["Country", "year"])
    df2["Happiness_Change"] = df2.groupby("Country")["Happiness Score"].diff()
    return df2


def stats_changes(df_change):
    print("\n=== YEAR-TO-YEAR CHANGES ===")
    print(df_change["Happiness_Change"].dropna().describe().round(3))


# ===============================
# 3. VISUALISATIONS
# ===============================


def hist_happiness(df):
    plt.figure()
    plt.hist(df["Happiness Score"], bins=20)
    plt.title("Distribution of Happiness Score")
    plt.xlabel("Happiness Score")
    plt.ylabel("Count")
    save_and_show("hist_happiness.png")


def boxplot_region(df):
    plt.figure(figsize=(10, 6))
    df.boxplot(column="Happiness Score", by="Region")
    plt.title("Happiness Score by Region")
    plt.suptitle("")
    plt.xticks(rotation=45)
    save_and_show("boxplot_region.png")


def line_global(df):
    yearly = df.groupby("year")["Happiness Score"].mean()
    plt.figure()
    plt.plot(yearly.index, yearly.values, marker="o")
    plt.title("Global Average Happiness Over Time")
    plt.xlabel("Year")
    plt.ylabel("Happiness Score")
    plt.grid(True)
    save_and_show("line_global.png")


def line_regions(df):
    pivot = df.pivot_table(
        values="Happiness Score", index="year", columns="Region", aggfunc="mean"
    )

    plt.figure(figsize=(10, 6))
    for col in pivot.columns:
        plt.plot(pivot.index, pivot[col], marker="o", label=col)

    plt.legend(fontsize=7)
    plt.title("Happiness by Region Over Time")
    plt.xlabel("Year")
    plt.ylabel("Score")
    save_and_show("line_regions.png")


def bars_top_bottom(df, year=None, n=10):
    if year is None:
        year = df["year"].max()

    d = df[df["year"] == year]
    top = d.sort_values("Happiness Score", ascending=False).head(n)
    bottom = d.sort_values("Happiness Score", ascending=True).head(n)

    plt.figure(figsize=(10, 5))
    plt.barh(top["Country"], top["Happiness Score"])
    plt.title(f"Top {n} Happiest Countries ({year})")
    plt.gca().invert_yaxis()
    save_and_show(f"top_{n}_{year}.png")

    plt.figure(figsize=(10, 5))
    plt.barh(bottom["Country"], bottom["Happiness Score"])
    plt.title(f"Bottom {n} Happiest Countries ({year})")
    plt.gca().invert_yaxis()
    save_and_show(f"bottom_{n}_{year}.png")


def scatter_reg(df, x_col, name):
    x = df[x_col].to_numpy()
    y = df["Happiness Score"].to_numpy()

    m, b = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = m * x_line + b

    plt.figure()
    plt.scatter(x, y, alpha=0.7)
    plt.plot(x_line, y_line, color="red")
    plt.title(f"Happiness vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel("Happiness Score")
    save_and_show(f"scatter_{name}.png")


def heatmap(df):
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, interpolation="nearest")
    plt.title("Correlation Heatmap")
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)
    save_and_show("heatmap.png")


def hist_changes(df_change):
    plt.figure()
    plt.hist(df_change["Happiness_Change"].dropna(), bins=30)
    plt.title("Year-to-Year Changes")
    plt.xlabel("Change")
    plt.ylabel("Count")
    save_and_show("hist_changes.png")


# ===============================
# MENU
# ===============================


def menu():
    print(
        """
=========== MENU ===========
1  - Basic stats
2  - Stats by year
3  - Stats by region
4  - Top/bottom countries
5  - Year-to-year stats
6  - Histogram of happiness
7  - Boxplot by region
8  - Line (global)
9  - Line (regions)
10 - Top/bottom charts
11 - Scatter: GDP
12 - Scatter: Health
13 - Heatmap
14 - Histogram of changes
0  - Exit
============================
"""
    )


def main():
    df = load_data()
    df_change = compute_changes(df)

    while True:
        menu()
        choice = input("Choose 0-14: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            basic_overview(df)
        elif choice == "2":
            stats_by_year(df)
        elif choice == "3":
            stats_by_region(df)
        elif choice == "4":
            top_bottom(df)
        elif choice == "5":
            stats_changes(df_change)
        elif choice == "6":
            hist_happiness(df)
        elif choice == "7":
            boxplot_region(df)
        elif choice == "8":
            line_global(df)
        elif choice == "9":
            line_regions(df)
        elif choice == "10":
            year = input("Year: ")
            if year.isdigit():
                bars_top_bottom(df, int(year))
            else:
                print("Invalid year.")
        elif choice == "11":
            scatter_reg(df, "Economy (GDP per Capita)", "gdp")
        elif choice == "12":
            scatter_reg(df, "Health (Life Expectancy)", "health")
        elif choice == "13":
            heatmap(df)
        elif choice == "14":
            hist_changes(df_change)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
