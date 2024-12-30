# Data Quality Analysis and Reporting

This repository contains the code, data, and documentation for performing data quality analysis on a given dataset. The project focuses on assessing and reporting key statistics, handling missing values, and identifying potential data quality issues.

## Features
- Descriptive statistics for key variables:
  - Mean, Median, Range
  - Skewness and Kurtosis
- Identification of outliers and data quality issues
- Handling missing values with imputation or column removal
- Visualizations (e.g., histograms, box plots) for data distribution analysis
- **Data Version Control (DVC)** for tracking dataset changes

## Project Structure
```plaintext
.
├── data
│   └── machinelearning.csv        # Input dataset
├── reports
│   └── analysis_report.md         # Detailed analysis report
├── scripts
│   ├── analysis.py                # Script for data analysis
│   ├── cleaning.py                # Script for handling missing values and outliers
│   └── visualization.py           # Script for generating data visualizations
├── .dvc                           # DVC metadata directory
├── README.md                      # Project documentation
├── dvc.yaml                       # DVC pipeline configuration
└── requirements.txt               # Python dependencies
