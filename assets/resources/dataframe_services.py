import pandas as pd

# Leer el archivo Excel
file_path = '/Users/ismartinez/Sites/mac_site/macpaving_site_seo_generated.xlsx'
df = pd.read_excel(file_path)

# Mostrar las primeras filas del dataframe para entender su estructura
print(df.head())
