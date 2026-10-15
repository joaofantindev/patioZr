# inicia o flask aq
from flask import Flask
from logic.cracha import processar_cracha
# requisicao de processamento em outro arquivo pra separacao
from logic.balanca import processar_peso
# take the peso e processa the trem
from logic.caminhao import registrar_caminhao
from database.db import criar_tabela


app = Flask(__name__)
criar_tabela()


@app.route("/", methods=["GET"])
def index():
    return "Servidor Zella Patio funcionando!"

@app.route("/api/status", methods=["GET"])
def status():
    return {
        "servidor": "Zella Patio",
        "status": "online",
        "balanca": "desconectada",
        "leitor_cracha": "desconectado"
    }


@app.route("/api/cracha", methods=["POST"])
def ler_cracha():

    from flask import request

    dados = request.get_json()#silent=True) isso faz retornar None, mas prefiro que retorne erro
    # FORMATO DO ERRO: 127.0.0.1 - - [15/Oct/2026 10:10:32] "GET /api/cracha HTTP/1.1" 405 -

    if not isinstance(dados, dict): # verifica se dados é um dicionario. exemplo:isinstance({"cracha": "123"}, dict)  # True
        return {"erro": "JSON invalido"}, 400

    return processar_cracha(dados.get("cracha"))

# testa com:
# curl -X POST http://127.0.0.1:5000/api/cracha -H "Content-Type: application/json" -d "{\"cracha\":\"123456\"}"

@app.route("/api/pesagem", methods=["POST"])
def registrar_pesagem():
    from flask import request

    dados = request.get_json()

    if not isinstance(dados, dict) or "peso" not in dados:
        return {"erro": "Informe o peso"}, 400

    return processar_peso(dados["peso"])

@app.route("/api/caminhao", methods=["POST"])
def criar_caminhao():
    from flask import request

    dados = request.get_json()

    if not isinstance(dados, dict):
        return {"erro": "JSON invalido"}, 400

    if "cracha" not in dados or "peso" not in dados:
        return {"erro": "Informe cracha e peso"}, 400

    return registrar_caminhao(
        dados["cracha"],
        dados["peso"]
    )

if __name__ == "__main__":
    app.run(debug=True)
