import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Load the CSV file
file_path = 'macpaving_site_seo.xlsx'
df = pd.read_excel(file_path)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Set up Jinja2 to load the template
try:
    env = Environment(
        loader=FileSystemLoader(searchpath="./"),  # Asegúrate de que la plantilla HTML está en el mismo directorio o ajusta la ruta
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template("plantilla.html")
except Exception as e:
    print(f"Error setting up Jinja2: {e}")
    exit(1)

# Define required fields
required_fields = [
    'service', 'meta_description', 'service_name', 'breadcum', 
    'service_title', 'description_p1', 'description_p2', 
    'description_p3', 'service_details', 'image_path1', 
    'image_path2', 'image_path3', 'image_path4', 'service_alt'
]

# Validate product data
def validate_data(row, required_fields):
    for field in required_fields:
        if pd.isna(row[field.strip()]):
            return False, f"The field '{field.strip()}' is missing or NaN."
    return True, ""

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row['service']) and isinstance(row['service'], str) and row['service'].strip():
        product_data = row.fillna('').to_dict()
        
        # Convert details_list to a list
        product_data['product_uses'] = [item.strip() for item in product_data['details_list'].split('\n')] if 'details_list' in product_data and product_data['details_list'] else []
        
        # Validate data
        valid, message = validate_data(row, required_fields)
        if not valid:
            print(f"Error at index {index}: {message}")
            continue
        
        # Generate HTML content
        try:
            html_content = template.render(product_data)
            file_name = f"{row['service_title'].replace(' ', '_').lower()}.html"
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(html_content)
            print(f"Generated file: {file_name}")
        except Exception as e:
            print(f"Error generating HTML file for {row['service']}: {e}")

print("HTML generation complete.")