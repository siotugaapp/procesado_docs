import pandas as pd
import os
import shutil

def bulk_rename_files(excel_path, sheet_name, destination_directory):
    
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    print(df.columns)
    
    for _, row in df.iterrows():
        original_path = row['A']  
        new_name = row['B']  
               
        new_path = os.path.join(destination_directory, new_name + '.pdf')
              
        try:
            shutil.copy2(original_path, new_path)
        except Exception as e:
            print(f"Error processing file {original_path}: {e}")

