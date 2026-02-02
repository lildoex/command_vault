from flask import Flask, jsonify

app = Flask(__name__)

# Toto je naše "falešná" databáze pro dnešek (jen seznam v paměti)
prikazy = [
    {"id": 1, "cmd": "ls -la", "popis": "list all files with details"},
    {"id": 2, "cmd": "docker ps", "popis": "list running Docker containers"},
    {"id": 3, "cmd": "git status", "popis": "show the working tree status"},
    {"id": 4, "cmd": "htop", "popis": "interactive process viewer"},
    {"id": 5, "cmd": "curl http://example.com", "popis": "fetch a URL content"}
]

# Hlavní stránka
@app.route('/')
def home():
    return "Vítej v CommandVault! Jdi na /api/prikazy pro data."

# API endpoint - vrátí data ve formátu JSON (pro budoucí JavaScript)
@app.route('/api/prikazy')
def get_prikazy():
    return jsonify(prikazy)

if __name__ == '__main__':
    # debug=True zajistí, že se server restartuje, když změníš kód
    app.run(debug=True, port=5000)