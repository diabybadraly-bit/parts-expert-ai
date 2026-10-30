from flask import Flask, render_template_string, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "C:/Users/HP/PARTS_EXPERT_AI/parts_expert.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_number TEXT UNIQUE,
            name TEXT,
            category TEXT,
            vehicle_model TEXT,
            price REAL,
            stock INTEGER
        )
    ''')
    # Insert dummy data if empty
    cursor.execute('SELECT COUNT(*) FROM parts')
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("FLT-001", "Filtre à huile Premium", "Moteur", "Peugeot 308", 15.50, 42),
            ("BRK-202", "Plaquettes de frein avant", "Freinage", "Renault Clio V", 45.00, 18),
            ("BAT-12V", "Batterie 12V 70Ah", "Électricité", "Universel", 120.00, 7),
            ("SHK-999", "Amortisseur arrière", "Suspension", "Volkswagen Golf VII", 89.99, 12)
        ]
        cursor.executemany('INSERT INTO parts (part_number, name, category, vehicle_model, price, stock) VALUES (?, ?, ?, ?, ?, ?)', sample_data)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <title>PARTS EXPERT AI</title>
            <style>
                body { font-family: var(--font-sans, system-ui, sans-serif); background: var(--card, #f4f6f9); color: var(--foreground, #333); margin: 0; padding: 20px; }
                h1 { color: var(--accent, #0066cc); }
                .search-box { margin-bottom: 20px; }
                input[type="text"] { padding: 8px; width: 300px; border: 1px solid var(--border, #ccc); border-radius: 4px; }
                button { padding: 8px 16px; background: var(--accent, #0066cc); color: white; border: none; border-radius: 4px; cursor: pointer; }
                table { width: 100%; border-collapse: collapse; background: white; margin-top: 10px; }
                th, td { padding: 10px; border: 1px solid var(--border, #ddd); text-align: left; }
                th { background: var(--muted, #eee); }
            </style>
        </head>
        <body>
            <h1>PARTS EXPERT AI - Moteur de Recherche de Pièces</h1>
            <div class="search-box">
                <input type="text" id="query" placeholder="Référence, nom, modèle...">
                <button onclick="searchParts()">Rechercher</button>
            </div>
            <table id="results">
                <thead>
                    <tr><th>Réf</th><th>Désignation</th><th>Catégorie</th><th>Modèle</th><th>Prix (€)</th><th>Stock</th></tr>
                </thead>
                <tbody></tbody>
            </table>
            <script>
                async function searchParts(q = '') {
                    const res = await fetch('/api/search?q=' + encodeURIComponent(q));
                    const data = await res.json();
                    const tbody = document.querySelector('#results tbody');
                    tbody.innerHTML = '';
                    data.forEach(p => {
                        tbody.innerHTML += `<tr><td>${p[1]}</td><td>${p[2]}</td><td>${p[3]}</td><td>${p[4]}</td><td>${p[5]} €</td><td>${p[6]}</td></tr>`;
                    });
                }
                document.querySelector('button').addEventListener('click', () => {
                    searchParts(document.getElementById('query').value);
                });
                searchParts();
            </script>
        </body>
        </html>
    ''')

@app.route('/api/search')
def api_search():
    q = request.args.get('q', '')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM parts WHERE part_number LIKE ? OR name LIKE ? OR vehicle_model LIKE ?", (f'%{q}%', f'%{q}%', f'%{q}%'))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
