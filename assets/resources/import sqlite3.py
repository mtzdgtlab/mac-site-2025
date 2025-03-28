import sqlite3

# Crear una conexión a la base de datos SQLite
db_path = '/mnt/data/macpaving_site_seo.db'
conn = sqlite3.connect(db_path)

# Crear un cursor
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS services (
    page_title TEXT,
    service TEXT,
    meta_description_sheet1 TEXT,
    service_name TEXT,
    category TEXT,
    category_name TEXT,
    service_title TEXT,
    breadcum TEXT,
    description_p1 TEXT,
    description_p2 TEXT,
    details_list TEXT,
    image_path1 TEXT,
    image_path2 TEXT,
    image_path3 TEXT,
    image_path4 TEXT,
    service_alt TEXT,
    meta_description_sheet2 TEXT,
    service_category TEXT
)
''')

# Importar los datos normalizados a la base de datos
normalized_data.to_sql('services', conn, if_exists='replace', index=False)

# Confirmar y cerrar la conexión
conn.commit()
conn.close()