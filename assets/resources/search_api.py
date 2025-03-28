from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify([])

    conn = sqlite3.connect('/mnt/data/macpaving_site_seo.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT service_name, service, meta_description_sheet1
        FROM services
        WHERE LOWER(service_name) LIKE ? OR LOWER(service) LIKE ? OR LOWER(meta_description_sheet1) LIKE ?
    """, (f'%{query}%', f'%{query}%', f'%{query}%'))

    results = cursor.fetchall()
    conn.close()

    search_results = []
    for result in results:
        search_results.append({
            'title': result[0],
            'url': f"{result[1].lower().replace(' ', '_')}.html",
            'description': result[2]
        })

    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)