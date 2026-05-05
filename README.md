# Global Air Quality Analysis

**Course:** Data-Centric Programming  
**Domain:** Enviromental Monitoring

**Project Focus:** Exploring air quality patterns across 10 major cities using AQI and pollutant data

## Team Members

| Name | Role | GitHub |
|------|------|--------|
| Vincent Mikalauskas | Data Engineer | [@vincent3182](https://github.com/vincent3182) |
| Eric Meagher | Data Analyst / Documentation Lead | [@ericmeagher](https://github.com/ericmeagher) |
| Laurentiu Codreanu | Visualization Lead | [@LaurCD](https://github.com/LaurCD) |


## Project Summary

This project analyses daily air quality readings from 10 major cities across 9 countries to identify pollution patterns across locations throughout the year. The raw dataset is loaded, cleaned, and prepared in Python, then explored using descriptive statistics and visualizations to highlight differences in pollutant levels between cities and across months.

The goal is to turn raw air quality measurements into a clearer picture of global pollution trends. Summary statistics such as mean, variance, percentiles, and rolling averages are used to give both a general overview and a deeper understanding of how pollutant levels are distributed and how they change over time.

## Main Insights

- AQI levels vary significantly across cities, with some cities consistently recording dangerous levels.
- PM2.5 is the most commonly exceeded pollutant relative to WHO guidelines.
- Air quality shows seasonal patterns, with certain months recording higher average AQI
- Rolling averages reveal underlying pollution trends that daily readings alone can obscure.
- Pollutant types differ by city, with some cities more affected by NO2 and others by PM2.5 or O3,

## Data Used

- Globail Air Quality dataset covering 10 cities across 2024
- Main variables analysed:
  - AQI (Air Quality Index)
  - PM2.5 and PM10 (particulate matter)
  - NO2 (nitrogen dioxide)
  - SO2 (sulphur dioxide)
  - CO (carbon monoxide)
  - O3 (ozone)
  - Temperature, humidity, wind speed

## Folder Layout

```bash
DataCentric_Programming_GroupProject/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── analysis.py
│   └── visualizations.py
├── outputs/
│   └── .gitkeep
├── requirements.txt
└── README.md
```

## Data Preparation

Before analysis, the dataset was prepared using the following steps:
- Renamed columns to cleaner, lowercase names.
- Converted the date column to a proper datetime format.
- Extracted month and year as separate columns.
- Converted all pollutant measurements to numeric format.
- Detected and capped outliers using the IQR method.
- Filled remaining missing values with column medians.
- Exported the cleaned data as both CSV and JSON.

## Analysis Workflow

### 1. Loading the Data
- Import the raw air quality CSV file into Python using Pandas.
- Inspect the data structure, column names, and basic format.

### 2. Cleaning the Dataset
- Rename and standardise columns.
- Handle missing values and outliers.
- Extract temporal features from the date column.

### 3. Descriptive Statistics
- Calculate mean, median, variance, and percentiles for each pollutant.
- Summarise AQI and pollutant levels by city, country, and by month.
- Compute rolling averages to identify pollution trends over time.
- Export summary results to CSV files in data/processed.

### 4. Visualisation
- Compare AQI levels across cities.
- Show how pollution changes month by month.
- Visualise the distribution of PM2.5 against WHO guidelines.
- Compare key pollutants side by side across cities.
- Plot 30-day rolling average AQI for the most polluted cities.

## Technical Notes

- Python is used for all stages of the project.
- Pandas supports loading, cleaning, and summarising the data.
- NumPy is used for numerical calculations.
- The project is organised into separate scripts for loading, preprocessing, analysis, and visualisation.
- Outputs are saved in a structured folder setup for easier access.

## Libraries

- numpy — numerical and statistical operations.
- pandas — data handling and analysis.
- matplotlib — chart creation.
- seaborn — statistical plotting.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/vincent3182/DataCentric_Programming_GroupProject
cd DataCentric_Programming_GroupProject
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Run preprocessing
```bash
python src/preprocessing.py
```

### 4. Run analysis
```bash
python src/analysis.py
```
### 5. Run visualizations
```bash
python src/visualizations.py
```

## License

This project is for academic use as part of the Data-Centric Programming module.
