from logic_2r.cracha import buscar_placa_por_cracha
from logic_2r.balanca import validar_peso


def registrar_caminhao(cracha, peso):
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

    registro = {
        "cracha": cracha,
        "placa": placa,
        "peso": float(peso),
        "unidade": "kg"
    }

    return {
        "mensagem": "Caminhao registrado",
        "dados": registro
    }, 200