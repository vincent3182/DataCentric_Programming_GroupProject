# Malin Head Weather Pattern Analysis

**Course:** Data-Centric Programming  
**Domain:** Climate and Weather Data Analysis  
**Project Focus:** Exploring weather trends at Malin Head through cleaning, statistical analysis, and visualisation

## Team Members

| Name | Role | GitHub |
|------|------|--------|
| Vincent Mikalauskas | Data Engineer | [@vincent3182](https://github.com/vincent3182) |
| Eric Meagher | Data Analyst / Documentation Lead | [@ericmeagher](https://github.com/ericmeagher) |
| Laurentiu Codreanu | Visualization Lead | [@LaurCD](https://github.com/LaurCD) |

## Project Summary

This project investigates daily weather observations from Malin Head to identify patterns in temperature, rainfall, wind speed, and sunshine. The raw dataset is first cleaned and prepared in Python, then explored using descriptive statistics and charts to highlight seasonal changes and overall variability in the weather data.

The goal of the project is to turn the raw measurements into a clearer story about local weather behaviour over time. By using summary statistics such as mean, median, percentiles, variance, and standard deviation, the analysis gives both a general overview and a better sense of how spread out the data is.

## Main Insights

- Weather conditions vary noticeably across the year.
- Temperature follows a strong seasonal cycle, with warmer periods and colder periods clearly visible.
- Rainfall and wind speed are less stable and show greater variation.
- Percentiles help describe the typical range of values in the dataset.
- Standard deviation and variance show how widely the weather measurements are distributed.

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
