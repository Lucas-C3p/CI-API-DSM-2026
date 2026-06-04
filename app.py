from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API CI/CD funcionando!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"


if __name__ == "__main__":
    app.run(debug=True)

    