# Electricity Demand and Pricing Analysis

## Overview

This project explores electricity demand and pricing in Victoria, Australia. The analysis aims to investigate how electricity demand and prices vary over time and how they relate to external factors such as temperature, seasonality, weekends, and public holidays.

## Setup

To obtain the data for this project, run the data_loading.py script found in scripts/. The data will get downloaded in data/raw/.

The raw dataset is used only in '01_initial_eda.ipynb' and '02_data_preparation.ipynb' files, both found in notebooks/. '02_data_preparation.ipynb' cleans the data and creates a new dataset.csv file, which gets saved in data/processed/dataset.csv.

## Dataset

- Source: Kaggle
- Geographic coverage: Victoria, Australia
- Time period: 1 January 2015 - 6 October 2020

## Research Questions

- How does electricity demand change with temperature and season?
- Are high-demand days associated with higher prices?
- How do weekends and holidays differ from working days?
- How often do negative prices occur, and under what conditions?

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
electricity-demand-pricing/
├── data/           # Raw and processed datasets
├── notebooks/      # Data understanding, cleaning and EDA
├── reports/        # Project documentation and analytical report
├── visualizations/ # Exported visualizations
├── scripts/        # Reusable Python modules
├── README.md
├── requirements.txt
└── .gitignore
```

## Key Findings

TBD
