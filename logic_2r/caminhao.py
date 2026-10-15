
from logic_2r.cracha import buscar_placa_por_cracha
from logic_2r.balanca import validar_peso
from database.db import salvar_pesagem


def registrar_caminhao(cracha, peso):
    if not cracha:
        return {
            "erro": "Cracha invalido"
        }, 400

    cracha = str(cracha).strip()

    placa = buscar_placa_por_cracha(cracha)

    if placa is None:
        return {
            "erro": "Cracha nao cadastrado"
        }, 404

    if not validar_peso(peso):
        return {
            "erro": "Peso invalido"
        }, 400

    peso = float(peso)

    salvar_pesagem(cracha, placa, peso)

    registro = {
        "cracha": cracha,
        "placa": placa,
        "peso": peso,
        "unidade": "kg"
    }

    return {
        "mensagem": "Caminhao registrado e salvo no banco",
        "dados": registro
    }, 200
