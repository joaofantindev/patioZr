# Pega o crachá e valida esse trem

def validar_cracha(cracha):
    if not cracha:
        return False

    cracha = str(cracha).strip()

    if not cracha:
        return False

    return True


def buscar_placa_por_cracha(cracha):
    banco_crachas = {
        "123456": "ABC1234",
        "990TIZ": "A78998A"
    }

    return banco_crachas.get(cracha)


def processar_cracha(cracha):
    if not validar_cracha(cracha):
        return {
            "erro": "Cracha invalido"
        }, 400

    cracha = str(cracha).strip()
    placa = buscar_placa_por_cracha(cracha)

    if placa is None:
        return {
            "erro": "Cracha nao cadastrado, fiotao"
        }, 404

    return {
        "cracha": cracha,
        "placa": placa,
        "mensagem": "Caminhao identificado"
    }, 200