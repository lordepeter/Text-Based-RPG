
def criar_personagem(nome):
    personagem = {
        "nome": nome,
        "nivel": 1,
        "vida": 100,
        "vida_maxima": 100,
        "xp": 0,
        "xp_maximo": 100,
        "forca": 8,
        "defesa": 5,
        "agilidade": 9,
    }
    return personagem


def receber_dano(personagem, dano):
    personagem["vida"] = max(0, personagem["vida"] - dano)


def curar_personagem(personagem, cura):
    personagem["vida"] = min(
        personagem["vida_maxima"],
        personagem["vida"] + cura,
    )


def esta_vivo(personagem):
    return personagem["vida"] > 0


def receber_xp(personagem, experiencia):
    personagem["xp"] += experiencia


def pode_subir_nivel(personagem):
    return personagem["xp"] >= personagem["xp_maximo"]


def subir_nivel(personagem):
    while pode_subir_nivel(personagem):
        personagem["xp"] -= personagem["xp_maximo"]
        personagem["nivel"] += 1
        personagem["xp_maximo"] = int(personagem["xp_maximo"] * 1.5)
        personagem["forca"] += 2
        personagem["defesa"] += 1
        personagem["agilidade"] += 3
        personagem["vida_maxima"] += 5
        curar_personagem(personagem, 5)


def processar_comando(comando):
    if comando == "explorar":
        return "Você começa a explorar a floresta."
    elif comando == "descansar":
        return "Você encontra um lugar seguro para descansar."
    else:
        return "Não entendi esse comando."


heroi = criar_personagem("Arthur")
