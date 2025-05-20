
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import urllib.request

# Constants
DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
FILE_NAME = "owid-covid-data.csv"

# Download the dataset if not already present
if not os.path.exists(FILE_NAME):
    print("Downloading dataset...")
    urllib.request.urlretrieve(DATA_URL, FILE_NAME)

# Load the data
df = pd.read_csv(FILE_NAME)
df['date'] = pd.to_datetime(df['date'])
df.fillna(method='ffill', inplace=True)

# Filter countries
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Plot total cases
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)
plt.title('Total COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.savefig('total_cases.png')
plt.clf()

# Plot total deaths
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.savefig('total_deaths.png')
plt.clf()

# Plot new cases
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['new_cases'], label=country)
plt.title('Daily New Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.savefig('new_cases.png')
plt.clf()

# Plot vaccinations
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)
plt.title('Total Vaccinations')
plt.xlabel('Date')
plt.ylabel('Vaccinations')
plt.legend()
plt.savefig('vaccinations.png')
plt.clf()

# Calculate and print insights
summary = df.groupby('location').agg({
    'total_cases': 'max',
    'total_deaths': 'max',
    'total_vaccinations': 'max'
})
summary['death_rate'] = summary['total_deaths'] / summary['total_cases']
summary.to_csv('summary_report.csv')
print(summary)
