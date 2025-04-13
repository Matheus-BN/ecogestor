from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dados fictícios de ecopontos
ecopontos = [
    {"id": 1, "nome": "Ecoponto Centro", "tipo": "Plástico", "lat": -23.5505, "lng": -46.6333},
    {"id": 2, "nome": "Cooperativa Verde", "tipo": "Eletrônico", "lat": -23.5432, "lng": -46.6298}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html", ecopontos=ecopontos)

@app.route("/api/ecopontos")
def api_ecopontos():
    return jsonify(ecopontos)

if __name__ == "__main__":
    app.run(debug=True)