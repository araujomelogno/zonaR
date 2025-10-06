import pandas as pd
import os

def load_main_dataset(data_dir):
    """
    Loads the primary dataset from the specified directory.

    This function targets 'baseZona2024.xlsx' as the main data file. It constructs
    the full file path and uses pandas to read the Excel file into a DataFrame.
    It includes error handling to catch cases where the file may not be found.

    Args:
        data_dir (str): The path to the directory containing the dataset.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data, or None if
                      the file cannot be loaded.
    """
    file_path = os.path.join(data_dir, 'baseZona2024.xlsx')
    print(f"--- Loading dataset: {file_path} ---")
    try:
        df = pd.read_excel(file_path)
        print("Dataset loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found at {file_path}. Please check the path.")
        return None
    except Exception as e:
        print(f"[ERROR] An error occurred while loading the file: {e}")
        return None

def clean_column_names(df):
    """
    Cleans and standardizes the column names of a DataFrame.

    This function performs two main cleaning operations:
    1. Converts all column names to lowercase to ensure consistency.
    2. Removes any special characters (like accents or symbols) from the names,
       replacing them with their closest ASCII equivalent where possible. This
       makes columns easier to access in code.

    Args:
        df (pd.DataFrame): The DataFrame whose column names need to be cleaned.

    Returns:
        pd.DataFrame: A new DataFrame with the cleaned column names.
    """
    print("\n--- Cleaning column names ---")
    original_columns = df.columns.tolist()

    # Using a robust method to handle special characters
    cleaned_columns = (df.columns.str.lower()
                       .str.normalize('NFKD')
                       .str.encode('ascii', errors='ignore')
                       .str.decode('utf-8'))

    df.columns = cleaned_columns

    print("Column names cleaned successfully.")
    # Example of changed columns
    print("Example of changes: 'IDBASE' -> 'idbase', 'COMUNICACIN5' -> 'comunicacin5'")
    return df

def analyze_demographics(df):
    """
    Performs and displays a basic demographic analysis of the dataset.

    This function calculates and prints the value counts for several key
    demographic columns: 'sexo' (gender), 'edad_tramo' (age group),
    and 'depto' (department/region). This provides a quick overview of the
    respondent population.

    Args:
        df (pd.DataFrame): The DataFrame containing the demographic data.
                           It is expected to have cleaned column names.
    """
    print("\n--- Performing Demographic Analysis ---")

    demographic_vars = ['sexo', 'edad_tramo', 'depto']

    for var in demographic_vars:
        if var in df.columns:
            print(f"\n[INFO] Analysis of '{var}':")
            print(df[var].value_counts(normalize=True).mul(100).round(2).astype(str) + '%')
        else:
            print(f"\n[WARNING] Column '{var}' not found in the DataFrame.")

def calculate_nps(df):
    """
    Calculates and prints the Net Promoter Score (NPS).

    The NPS is calculated based on the 'nps' column. Respondents are categorized:
    - Promoters: score 9-10
    - Passives: score 7-8
    - Detractors: score 0-6

    The final NPS score is (% Promoters - % Detractors).

    Args:
        df (pd.DataFrame): The DataFrame containing the 'nps' column.
    """
    print("\n--- Calculating Net Promoter Score (NPS) ---")
    if 'nps' not in df.columns:
        print("[WARNING] 'nps' column not found. Cannot calculate NPS.")
        return

    # Ensure NPS column is numeric, coercing errors to NaN
    nps_scores = pd.to_numeric(df['nps'], errors='coerce')

    # Drop rows where NPS is not a valid number
    nps_scores = nps_scores.dropna()

    promoters = (nps_scores >= 9).sum()
    passives = nps_scores.between(7, 8).sum()
    detractors = (nps_scores <= 6).sum()

    total_respondents = len(nps_scores)

    if total_respondents == 0:
        print("[INFO] No valid NPS scores found.")
        return

    promoter_percentage = (promoters / total_respondents) * 100
    detractor_percentage = (detractors / total_respondents) * 100

    nps_score = promoter_percentage - detractor_percentage

    print(f"Total NPS Respondents: {total_respondents}")
    print(f"Promoters (9-10): {promoters} ({promoter_percentage:.2f}%)")
    print(f"Passives (7-8):   {passives} ({((passives / total_respondents) * 100):.2f}%)")
    print(f"Detractors (0-6): {detractors} ({detractor_percentage:.2f}%)")
    print(f"\nFinal NPS Score: {nps_score:.2f}")


def main():
    """
    Main function to run the data analysis pipeline.

    This function orchestrates the entire process:
    1. Defines the data directory.
    2. Loads the main dataset.
    3. Cleans the column names.
    4. Performs demographic analysis.
    5. Calculates the Net Promoter Score.
    """
    # The data was extracted to a temporary directory to manage file sizes.
    data_directory = "/tmp/datos/datos"

    df = load_main_dataset(data_directory)

    if df is not None:
        df = clean_column_names(df)
        analyze_demographics(df)
        calculate_nps(df)
        print("\n--- Analysis Complete ---")

if __name__ == "__main__":
    main()