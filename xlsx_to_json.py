"""
prerequisite: pandas, and xlsx engine: openpyxl need to install in your python virtual machine
Use command: pip install pandas openpyxl
"""

import pandas as pd
import json
import os

def xlsx_to_json(xlsx_file_path: str) -> dict:
    """
    Convert a multi-tab Excel (.xlsx) file to a JSON object.
    
    Args:
        xlsx_file_path (str): The file path of the Excel (.xlsx) file.
    
    Returns:
        dict: A JSON object representing the data in the Excel file.
    """
    xlsx = pd.ExcelFile(xlsx_file_path)
    json_data = {}
    for sheet in xlsx.sheet_names:
      df = pd.read_excel(xlsx, sheet_name=sheet)
      json_str = df.to_json()
      json_data[sheet] = json.loads(json_str)
    return json_data

def main() -> None:
    """
    Enter the xlsx file path to convert it to json
    """
    user_input = input("Enter filepath: ")
    file_path = r"{}".format(user_input)

    json_data = xlsx_to_json(file_path)
    # Write the JSON data to a file
    with open("test_data.json", "w") as f:
        f.write(json.dumps(json_data, indent=4))
    print("Json file created successfully in the script directory.")

if __name__ == '__main__':
    main()