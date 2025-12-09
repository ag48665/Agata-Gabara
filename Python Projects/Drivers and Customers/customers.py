# logistics_analysis_desktop.py
#
# Make sure this file is in the SAME folder as:
#   - customers.csv
#   - drivers.csv
#
# Run it in Mu (Python 3), not MicroPython.
# You will need the 'pandas' and 'matplotlib' packages installed.
#
# Every chart is saved to:
#   C:/Users/PC/OneDrive/Desktop

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ===============================
# 0. CONFIG: WHERE TO SAVE CHARTS
# ===============================

SAVE_DIR = r"C:/Users/PC/OneDrive/Desktop"  # your Desktop path

def save_and_show(filename, show=True):
    """
    Save current matplotlib figure to Desktop and optionally show it.
    """
    # Make sure directory exists
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)

    full_path = os.path.join(SAVE_DIR, filename)
    plt.savefig(full_path)
    print(f"Chart saved to: {full_path}")

    if show:
        plt.show()
    else:
        plt.close()


# ===============================
# 1. LOAD DATA
# ===============================

def load_data():
    print("Loading data...")
    customers = pd.read_csv("customers.csv")
    drivers = pd.read_csv("drivers.csv")

    # Parse date columns
    customers["contract_start_date"] = pd.to_datetime(customers["contract_start_date"])
    drivers["hire_date"] = pd.to_datetime(drivers["hire_date"])
    drivers["termination_date"] = pd.to_datetime(drivers["termination_date"], errors="coerce")
    drivers["date_of_birth"] = pd.to_datetime(drivers["date_of_birth"])

    # Add derived columns for drivers
    today = pd.Timestamp.today().normalize()

    drivers["age_years"] = (today - drivers["date_of_birth"]).dt.days / 365.25
    drivers["tenure_years"] = (
        drivers["termination_date"].fillna(today) - drivers["hire_date"]
    ).dt.days / 365.25

    return customers, drivers

# ===============================
# 2. BASIC STATISTICS
# ===============================

def basic_stats(customers, drivers):
    print("\n===== BASIC STATISTICS =====\n")

    print("Customers – numeric description:\n")
    print(customers[["credit_terms_days", "annual_revenue_potential"]].describe())
    print("\nCustomers – by customer_type:\n")
    print(customers["customer_type"].value_counts())
    print("\nCustomers – by account_status:\n")
    print(customers["account_status"].value_counts())

    print("\nDrivers – numeric description:\n")
    print(drivers[["years_experience", "age_years", "tenure_years"]].describe())
    print("\nDrivers – by employment_status:\n")
    print(drivers["employment_status"].value_counts())
    print("\nDrivers – by home_terminal (top 10):\n")
    print(drivers["home_terminal"].value_counts().head(10))

    # Example: average annual revenue by customer type
    print("\nAverage annual revenue by customer_type:\n")
    print(
        customers.groupby("customer_type")["annual_revenue_potential"]
        .mean()
        .round(2)
    )

    # Example: total annual revenue by account_status
    print("\nTotal annual revenue by account_status:\n")
    print(
        customers.groupby("account_status")["annual_revenue_potential"]
        .sum()
        .round(2)
    )

# ===============================
# 3. VISUALISATIONS – CUSTOMERS
# ===============================

def plot_customer_revenue_hist(customers):
    plt.figure()
    plt.hist(customers["annual_revenue_potential"], bins=20)
    plt.title("Distribution of Annual Revenue Potential")
    plt.xlabel("Annual revenue potential")
    plt.ylabel("Number of customers")
    plt.tight_layout()
    save_and_show("customer_revenue_hist.png", show=True)

def plot_customer_revenue_by_type_box(customers):
    plt.figure()
    customers.boxplot(column="annual_revenue_potential", by="customer_type")
    plt.title("Annual Revenue Potential by Customer Type")
    plt.suptitle("")  # remove automatic suptitle
    plt.xlabel("Customer type")
    plt.ylabel("Annual revenue potential")
    plt.tight_layout()
    save_and_show("customer_revenue_by_type_box.png", show=True)

def plot_customers_by_freight_type(customers):
    counts = customers["primary_freight_type"].value_counts()

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title("Number of Customers by Primary Freight Type")
    plt.xlabel("Primary freight type")
    plt.ylabel("Number of customers")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    save_and_show("customers_by_freight_type.png", show=True)

def plot_contracts_start_by_year(customers):
    # Count customers by contract start year
    years = customers["contract_start_date"].dt.year
    year_counts = years.value_counts().sort_index()

    plt.figure()
    plt.plot(year_counts.index, year_counts.values, marker="o")
    plt.title("Number of Customer Contracts Started per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of new contracts")
    plt.grid(True)
    plt.tight_layout()
    save_and_show("contracts_started_by_year.png", show=True)

# ===============================
# 4. VISUALISATIONS – DRIVERS
# ===============================

def plot_driver_experience_hist(drivers):
    plt.figure()
    plt.hist(drivers["years_experience"], bins=15)
    plt.title("Distribution of Driver Experience")
    plt.xlabel("Years of experience")
    plt.ylabel("Number of drivers")
    plt.tight_layout()
    save_and_show("driver_experience_hist.png", show=True)

def plot_driver_age_hist(drivers):
    plt.figure()
    plt.hist(drivers["age_years"], bins=15)
    plt.title("Distribution of Driver Age")
    plt.xlabel("Age (years)")
    plt.ylabel("Number of drivers")
    plt.tight_layout()
    save_and_show("driver_age_hist.png", show=True)

def plot_driver_status_counts(drivers):
    counts = drivers["employment_status"].value_counts()

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title("Drivers by Employment Status")
    plt.xlabel("Employment status")
    plt.ylabel("Number of drivers")
    plt.tight_layout()
    save_and_show("drivers_by_employment_status.png", show=True)

def plot_driver_hires_by_year(drivers):
    years = drivers["hire_date"].dt.year
    year_counts = years.value_counts().sort_index()

    plt.figure()
    plt.plot(year_counts.index, year_counts.values, marker="o")
    plt.title("Number of Drivers Hired per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of hires")
    plt.grid(True)
    plt.tight_layout()
    save_and_show("driver_hires_by_year.png", show=True)

# ===============================
# 5. CORRELATION HEATMAP (ADVANCED)
# ===============================

def plot_correlation_heatmap(customers, drivers):
    import numpy as np

    # Select numeric columns from both datasets
    cust_num = customers[["credit_terms_days", "annual_revenue_potential"]].copy()
    cust_num.columns = ["credit_terms_days", "annual_revenue_potential"]

    drv_num = drivers[["years_experience", "age_years", "tenure_years"]].copy()
    drv_num.columns = ["years_experience", "age_years", "tenure_years"]

    # Create one combined numeric DataFrame (just to show a small correlation example)
    combined = pd.concat(
        [
            cust_num.reset_index(drop=True),
            drv_num.reset_index(drop=True)
        ],
        axis=1
    )

    corr = combined.corr()

    plt.figure()
    plt.imshow(corr, interpolation="nearest")
    plt.title("Correlation Heatmap (Customers + Drivers numeric fields)")
    plt.colorbar(label="Correlation")
    tick_marks = range(len(corr.columns))
    plt.xticks(tick_marks, corr.columns, rotation=45, ha="right")
    plt.yticks(tick_marks, corr.columns)
    plt.tight_layout()
    save_and_show("correlation_heatmap.png", show=True)

# ===============================
# 6. SIMPLE MENU SYSTEM
# ===============================

def print_menu():
    print("\n===== MENU =====")
    print("1  - Show basic statistics")
    print("2  - Plot customer revenue histogram")
    print("3  - Boxplot: revenue by customer type")
    print("4  - Bar chart: customers by freight type")
    print("5  - Line chart: contracts started per year")
    print("6  - Histogram: driver experience")
    print("7  - Histogram: driver age")
    print("8  - Bar chart: drivers by employment status")
    print("9  - Line chart: driver hires per year")
    print("10 - Correlation heatmap (advanced)")
    print("0  - Exit")

def main():
    customers, drivers = load_data()

    while True:
        print_menu()
        choice = input("Choose an option (0-10): ")

        if choice == "0":
            print("Exiting. Bye!")
            break
        elif choice == "1":
            basic_stats(customers, drivers)
        elif choice == "2":
            plot_customer_revenue_hist(customers)
        elif choice == "3":
            plot_customer_revenue_by_type_box(customers)
        elif choice == "4":
            plot_customers_by_freight_type(customers)
        elif choice == "5":
            plot_contracts_start_by_year(customers)
        elif choice == "6":
            plot_driver_experience_hist(drivers)
        elif choice == "7":
            plot_driver_age_hist(drivers)
        elif choice == "8":
            plot_driver_status_counts(drivers)
        elif choice == "9":
            plot_driver_hires_by_year(drivers)
        elif choice == "10":
            plot_correlation_heatmap(customers, drivers)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
