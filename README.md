# COVID-19 Global Data Tracker

## Project Description

This Python project analyzes and visualizes global COVID-19 trends. It covers data loading, cleaning, exploratory data analysis (EDA), and visualization of key metrics including total cases, deaths, and vaccinations across countries.

## Project Objectives

- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries/regions
- Visualize trends with charts and maps
- Communicate findings via narrative and visuals

## Step-by-Step Implementation

### 1. Data Collection
- Source: [Our World in Data COVID-19 Dataset](https://covid.ourworldindata.org/data/owid-covid-data.csv)
- Format: CSV
- Downloaded and saved locally.

### 2. Data Loading & Exploration
- Used pandas to load and explore the dataset
- Key columns: `date`, `location`, `total_cases`, `total_deaths`, `new_cases`, `new_deaths`, `total_vaccinations`

### 3. Data Cleaning
- Converted `date` column to datetime format
- Filtered selected countries (Kenya, India, USA)
- Handled missing values with forward fill

### 4. Exploratory Data Analysis (EDA)
- Line charts: Total cases, deaths, new cases
- Calculated death rate = total_deaths / total_cases
- Summary statistics exported to CSV

### 5. Vaccination Progress
- Visualized total vaccinations over time
- Line charts for each country

### 6. Optional: Choropleth Map (not implemented in CLI version)

### 7. Reporting & Insights
- Insights printed in console and summary exported to `summary_report.csv`

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn

## How to Run

```bash
pip install pandas matplotlib seaborn
python covid_tracker.py
```

## Deliverables

- `covid_tracker.py`: Python script
- `summary_report.csv`: Summary stats by country
- `total_cases.png`, `total_deaths.png`, `new_cases.png`, `vaccinations.png`: Charts
- `README.md`: Project documentation
