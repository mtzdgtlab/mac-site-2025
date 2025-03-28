import pandas as pd

# Define the path to your Excel file
file_path = 'macpaving_site_seo.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Load the specific sheet into a dataframe
df = pd.read_excel(excel_data, sheet_name='macpaving_site_seo')

# Display the first few rows of the dataframe to verify the data
print(df.head())