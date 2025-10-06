# ZonaR Data Analysis Project

## 1. Project Purpose

This repository contains a data analysis project focused on survey data from ZonaR. The primary goal is to provide a clear, well-documented, and reproducible analysis of the survey results. This includes demographic breakdowns and the calculation of key business metrics like the Net Promoter Score (NPS).

This project serves as a practical example of how to:
- Structure a data analysis project.
- Clean and process raw survey data.
- Perform exploratory data analysis.
- Document code and processes for clarity and maintainability.

The scripts provided are designed to be a starting point for more advanced analysis.

## 2. Data Files Overview

The data for this project is contained within `datos.rar`. Due to the large size of the data files, they are not tracked in this repository and are instead extracted to a temporary directory during analysis.

The key files within the archive are:

- **`baseZona2024.xlsx`**: The primary dataset used for the analysis. It contains the main survey responses in a wide format, with each row representing a respondent and each column a question.
- **`BASE_PBI.sav`**: The same dataset in SPSS format, which may be useful for statistical software users.
- **`Indice.xlsx`**: A data dictionary or index file that provides metadata about the variables in the main dataset, including question text and variable names.
- **`df_*.csv` / `df_*.xlsx`**: Various intermediate and pivoted versions of the data, likely used for specific analyses or visualizations.
- **`Sorted_Data.csv`**: A long-format version of the data, which can be useful for certain types of analysis.

## 3. Setup and Installation

To run the analysis scripts, you need to set up a Python environment with the required libraries.

### Prerequisites
- Python 3.x
- `unrar` command-line utility. To install it on Debian/Ubuntu, run:
  ```bash
  sudo apt-get update && sudo apt-get install -y unrar
  ```

### Installation
Clone the repository and install the necessary Python packages using pip:

```bash
# 1. Clone the repository
git clone <repository-url>
cd <repository-name>

# 2. Install required Python libraries
pip install pandas openpyxl pyreadstat
```

## 4. How to Run the Analysis

This project includes two Python scripts: one for initial data exploration and one for the main analysis.

### Step 1: Data Extraction
The analysis scripts are configured to read data from a temporary directory (`/tmp/datos/datos`). Before running any script, you must first extract the data from `datos.rar`.

From the root of the project directory, run the following command in your terminal. This command creates the temporary directory and extracts the data into it.

```bash
mkdir -p /tmp/datos/datos && unrar x /app/datos.rar /tmp/datos/
```
*Note: The path `/app/datos.rar` assumes the project is running in an environment where the repository is located at `/app`. Adjust this path if your setup is different.*

### Step 2: Running the Scripts

#### A. Data Exploration
To get a quick overview of all the data files, you can run the exploration script. This script iterates through each file, printing its first few rows, column names, and data types.

```bash
python3 data_exploration.py
```

#### B. Main Analysis
To run the primary analysis, which includes data cleaning, demographic summaries, and NPS calculation, execute the main analysis script.

```bash
python3 analysis.py
```

You should see a clean, formatted output in your terminal summarizing the key findings from the `baseZona2024.xlsx` dataset.