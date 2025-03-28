import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os

# Leer el archivo Excel
file_path = '/Users/ismartinez/Sites/mac_site/macpaving_site_seo_generated.xlsx'
df = pd.read_excel(file_path)

# Configurar Jinja2
env = Environment(loader=FileSystemLoader('/Users/ismartinez/Sites/mac_site'))
template = env.get_template('services_plantilla.html')

# Definir las categorías y servicios
categories = {
    'Sealer': ['Sealcoating', 'Asphalt Maintenance', 'Crack Filling', 'Line Striping'],
    'Asphalt Paving': ['Installation', 'Resurfacing', 'Replacement', 'Extension'],
    'Pavers': ['Pavers Installation', 'Paver Maintenance', 'Retaining Walls', 'Belgium Blocks'],
    'Concrete': ['Walkways', 'Sidewalks', 'Curbs', 'Aprons'],
    'Landscaping': ['Sod Installation', 'Top Soil', 'Seed Grass', 'Drainage', 'Gutters', 'Power Wash', 'Hauling', 'Winter Services']
}

# Crear directorio de salida si no existe
output_dir = '/Users/ismartinez/Sites/mac_site/generated_pages'
os.makedirs(output_dir, exist_ok=True)

# Definir campos requeridos
required_fields = [
    'service', 'meta_description', 'service_name', 'breadcum', 
    'service_title', 'description_p1', 'description_p2', 
    'description_p3', 'service_details', 'image_path1', 
    'image_path2', 'image_path3', 'image_path4', 'service_alt'
]

# Función para validar los datos
def validate_data(service_data):
    for field in required_fields:
        if field not in service_data or pd.isna(service_data[field]):
            return False, f"The field '{field}' is missing or NaN."
    return True, ""

# Generar las páginas HTML para cada categoría
for category, services in categories.items():
    category_services = df[df['service'].isin(services)]
    services_list = category_services.to_dict('records')
    
    for service in services_list:
        service['images'] = [service.get('image_path1', ''), service.get('image_path2', ''), service.get('image_path3', ''), service.get('image_path4', '')]
        
        # Validar los datos del servicio
        valid, message = validate_data(service)
        if not valid:
            print(f"Error for service '{service.get('service', 'Unknown')}': {message}")
            continue

    # Verificar los datos antes de renderizar
    print(f"Category: {category}")
    print(services_list)
    
    rendered_html = template.render(
    category_service=category,
    meta_services=category_services['meta_description'].iloc[0] if not category_services.empty else '',
    services=services_list
)
    
    output_path = os.path.join(output_dir, f'{category.lower().replace(" ", "_")}.html')
    with open(output_path, 'w') as f:
        f.write(rendered_html)