from flask import Flask, render_template, jsonify
import json  # Para carregar dados dos ecopontos

app = Flask(__name__)

# Dados mockados (substitua por conexão com banco de dados)
ECOPONTOS = [
    {"nome": "Ecoponto Centro", "lat": -23.5505, "lng": -46.6333, "tipo": "Recicláveis", "endereco": "Rua Principal, 123", "horario": "08h-18h"},
    {"nome": "Ecoponto Parque", "lat": -23.5600, "lng": -46.6500, "tipo": "Eletrônicos", "endereco": "Av. Verde, 456", "horario": "09h-17h"}
]

# Rotas principais
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html", ecopontos=ECOPONTOS)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# API Endpoints
@app.route('/api/reciclagem')
def dados_reciclagem():
    return jsonify({
        'labels': ['Plástico', 'Vidro', 'Eletrônico', 'Papel', 'Metal'],
        'values': [12, 8, 5, 7, 9]  # Dados simulados
    })

@app.route('/api/ecopontos')
def api_ecopontos():
    return jsonify(ECOPONTOS)

@app.route('/api/estatisticas')
def estatisticas():
    return jsonify({
        'total_reciclado': 1240,
        'usuarios_ativos': 42,
        'meta_mensal': 2000
    })

# Configurações importantes
if __name__ == '__main__':
    app.run(debug=True)