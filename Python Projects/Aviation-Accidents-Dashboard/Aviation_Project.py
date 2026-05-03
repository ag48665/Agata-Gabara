import pandas as pd
df = pd.read_csv("AviationData.csv", encoding="latin1")
print(df.head())

print(df.columns)
print(df.info())


df["Event.Date"] = pd.to_datetime(df["Event.Date"], errors="coerce")
df["year"] = df["Event.Date"].dt.year

accidents_per_year = df.groupby("year").size()
print(accidents_per_year.tail(10))

top_countries = df["Country"].value_counts().head(10)
print(top_countries)

print(df["Total.Fatal.Injuries"].describe())
print(df["Weather.Condition"].value_counts())

import matplotlib.pyplot as plt

# accidents_per_year.plot(title="Accidents per year")
# plt.show()
#
# df.groupby("year")["Total.Fatal.Injuries"].sum().plot()
# plt.show()
#
# accidents = df.groupby("year").size()
# fatalities = df.groupby("year")["Total.Fatal.Injuries"].sum()
# fatal_per_accident = fatalities / accidents
# fatal_per_accident.plot(title="Average fatalities per accident")
# plt.show()
#
#
# df.groupby("Weather.Condition")["Total.Fatal.Injuries"].mean()
#
# df["Weather.Condition"] = df["Weather.Condition"].str.upper()
# df["Weather.Condition"].value_counts()
# df.groupby("Weather.Condition")["Total.Fatal.Injuries"].mean()

# daty
df["Event.Date"] = pd.to_datetime(df["Event.Date"], errors="coerce")
df["year"] = df["Event.Date"].dt.year

# pogoda – ujednolicenie
df["Weather.Condition"] = df["Weather.Condition"].str.upper()

# liczby – upewnij się, że są liczbami
cols = ["Total.Fatal.Injuries","Total.Serious.Injuries",
        "Total.Minor.Injuries","Total.Uninjured"]
for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")


accidents = df.groupby("year").size()
fatalities = df.groupby("year")["Total.Fatal.Injuries"].sum()
fatal_per_accident = fatalities / accidents

import matplotlib.pyplot as plt

plt.figure()
accidents.plot(title="Accidents per year")
plt.xlabel("Year"); plt.ylabel("Count")
plt.show()

plt.figure()
fatalities.plot(title="Fatalities per year")
plt.xlabel("Year"); plt.ylabel("Fatalities")
plt.show()

plt.figure()
fatal_per_accident.plot(title="Average fatalities per accident")
plt.xlabel("Year"); plt.ylabel("Avg fatalities")
plt.show()

weather_mean = df.groupby("Weather.Condition")["Total.Fatal.Injuries"].mean()
print(weather_mean)

country_counts = df["Country"].value_counts()
country_pct = (country_counts / country_counts.sum()) * 100

print(country_pct.head(10))

df = df[df["year"] >= 1980]

