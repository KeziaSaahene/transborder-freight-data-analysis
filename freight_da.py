import os
import pandas as pd

# Define the base folder and output file
base_folder = "data"
output_file = "freight_dataset.csv"

first_file = True

# Looping through each year folder
for year in os.listdir(base_folder):
    year_path = os.path.join(base_folder, year)
    if not os.path.isdir(year_path):
        continue

    # Looping through each month folder inside the year folder
    for month in os.listdir(year_path):
        month_path = os.path.join(year_path, month)
        if not os.path.isdir(month_path):
            continue

        # Looping through each CSV file in the month folder
        for file in os.listdir(month_path):
            if file.lower().endswith('.csv'):
                file_path = os.path.join(month_path, file)
                print(f" Found CSV file: {file_path}")

                try:
                    df = pd.read_csv(file_path, low_memory=False)


        
                    df.to_csv(output_file, mode='a', index=False, header=first_file)
                    first_file = False
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")

print(f"\n All CSVs streamed into '{output_file}' successfully!")
