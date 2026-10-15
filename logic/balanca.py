# pega e valida o peso do bixão la ele

def validar_peso(peso):
    try:
        peso = float(peso)
    except (ValueError, TypeError):
        return False

    if peso <= 0:
        return False

    return True


def processar_peso(peso):
    if not validar_peso(peso):
        return {
            "erro": "Peso invalido"
        }, 400

    return {
        "peso": float(peso),
        "unidade": "kg",
        "mensagem": "Peso registrado"
    }, 200