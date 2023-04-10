import pandas as pd
import os

# Read the Excel file into a DataFrame
df = pd.read_excel("TEST1.xlsx", sheet_name="Feuil1")

# Loop through the rows of the DataFrame to create the folders and subfolders
for index, row in df.iterrows():
    # Create the main folder
    main_folder = row["Main Folder"]
    os.mkdir(main_folder)
    
    # Create the subfolders
    for level in range(1, len(row)):
        subfolder_name = row[f"Subfolder {level}"]
        subfolder_path = os.path.join(main_folder, str(subfolder_name))
        os.mkdir(subfolder_path)