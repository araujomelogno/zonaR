import pandas as pd
import pyreadstat
import os

def explore_data(data_path):
    """
    Loads and explores various data files (CSV, Excel, SAV) from a specified directory.

    For each file, it prints the filename, the first 5 rows, the column names,
    and the data types of the columns. This function serves as an initial
    assessment of the available data.

    Args:
        data_path (str): The absolute path to the directory containing the data files.
    """
    print(f"--- Starting Data Exploration in {data_path} ---")

    if not os.path.isdir(data_path):
        print(f"Error: The directory '{data_path}' was not found.")
        return

    file_list = sorted(os.listdir(data_path)) # Sort for consistent order

    for filename in file_list:
        filepath = os.path.join(data_path, filename)

        # Skip directories if any exist
        if os.path.isdir(filepath):
            continue

        print(f"\n{'='*25}")
        print(f"Analyzing file: {filename}")
        print(f"{'='*25}")

        try:
            if filename.lower().endswith('.csv'):
                df = pd.read_csv(filepath, low_memory=False)
            elif filename.lower().endswith('.xlsx'):
                df = pd.read_excel(filepath)
            elif filename.lower().endswith('.sav'):
                df, meta = pyreadstat.read_sav(filepath)
            else:
                print(f"Skipping unsupported file type: {filename}")
                continue

            print("\n[INFO] First 5 rows:")
            print(df.head())
            print("\n[INFO] Column names:")
            print(df.columns.tolist())
            print("\n[INFO] Data types:")
            print(df.dtypes)

        except Exception as e:
            print(f"\n[ERROR] Could not read or process file {filename}.")
            print(f"  Reason: {e}")

    print("\n--- Data Exploration Complete ---")

if __name__ == "__main__":
    # Data was extracted to a temporary directory to avoid repository size limits.
    data_directory = "/tmp/datos/datos"
    explore_data(data_directory)