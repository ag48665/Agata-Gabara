import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Aviation Accidents Dashboard")

df = pd.read_csv("AviationData.csv", encoding="latin1", low_memory=False)

df["Event.Date"] = pd.to_datetime(df["Event.Date"], errors="coerce")
df["year"] = df["Event.Date"].dt.year
df["Weather.Condition"] = df["Weather.Condition"].str.upper()

df = df[df["year"] >= 1980]

st.write("Data preview:")
st.dataframe(df.head())

st.subheader("Number of accidents per year”")

accidents_per_year = df.groupby("year").size()

fig, ax = plt.subplots()
accidents_per_year.plot(ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of accidents")
st.pyplot(fig)

st.subheader("Total fatal injuries per year")

fatalities = df.groupby("year")["Total.Fatal.Injuries"].sum()

fig, ax = plt.subplots()
fatalities.plot(ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Fatalities")
st.pyplot(fig)

st.subheader("Average number of casualties per accident")

fatal_per_accident = fatalities / accidents_per_year

fig, ax = plt.subplots()
fatal_per_accident.plot(ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Average fatalities")
st.pyplot(fig)

st.subheader("Top ten countries")

top_countries = df["Country"].value_counts().head(10)
st.bar_chart(top_countries)

st.subheader("Weather conditions")

weather_counts = df["Weather.Condition"].value_counts()
st.bar_chart(weather_counts)

st.subheader("Average number of casualties by weather")

weather_fatalities = df.groupby("Weather.Condition")["Total.Fatal.Injuries"].mean()
st.write(weather_fatalities)