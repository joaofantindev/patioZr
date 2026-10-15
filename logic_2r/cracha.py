# pega o cracha e valida esse trem

def validar_cracha(cracha):
    if not cracha: # se nao tiver nada nesse trem
        return False

    cracha = str(cracha).strip()

    if not cracha:
        return False

    return True


def processar_cracha(cracha):
    if not validar_cracha(cracha):
        return {
            "erro": "Cracha invalido"
        }, 400

    return {
        "mensagem": "Cracha recebido",
        "cracha": str(cracha).strip()
    }, 200

    def buscar_placa_por_cracha(cracha):
        banco_crachas = {
            "123456": "ABC1234",
            "990TIZ": "A78998A"
        }

        return banco_crachas.get(cracha)
