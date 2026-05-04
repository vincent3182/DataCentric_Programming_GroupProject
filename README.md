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

- Daily weather records from Malin Head.
- Main variables analysed:
  - Maximum temperature.
  - Minimum temperature.
  - Rainfall.
  - Wind speed.
  - Sunshine.

## Folder Layout

```bash
WeatherProject/
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
- Converted the date column to a proper date format.
- Removed columns that were not needed for the project.
- Converted weather values into numeric format.
- Checked for missing values and handled them appropriately.
- Added useful derived fields such as year, month, and mean temperature.

## Analysis Workflow

### 1. Loading the Data
- Import the raw weather file into Python using Pandas.
- Inspect the data structure, column names, and basic format.

### 2. Cleaning the Dataset
- Remove or fix invalid values.
- Convert data types where needed.
- Make sure the data is ready for analysis.

### 3. Descriptive Statistics
- Calculate mean, median, minimum, maximum, standard deviation, variance, and percentiles.
- Summarise the key weather variables.

### 4. Visualisation
- Create charts to show monthly and yearly patterns.
- Compare trends in temperature, rainfall, and wind speed.

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

## License

This project is for academic use as part of the Data-Centric Programming module.
