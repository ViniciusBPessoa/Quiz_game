from verificador_valores.verificadores import *
from jogadores.Pegador_nomes import *


def linha(veses=20):  # cria divisorias
    print("-" * veses)


def cria_menu(text, possibilidades, Jogadores = False, plota_esse = 0):  # Gera um menu inteiro ja retornando uma variavel inteira referente as opçoes do menu

    if Jogadores:
        plota_nomes(plota_esse)

    tamanho = int(len(text))

    linha(tamanho+10)
    print(f"\033[33m{text:^{int(tamanho) + 10}}\033[m")
    linha(tamanho+10)
    print("")


    for x, y in enumerate(possibilidades):
        print(f"\033[36m{x + 1}\033[m - \033[33m{y}\033[m")

    Resposta = leia_menu(possibilidades)  # ativando um verificador de numeros inteiros proprio para menus

    return Resposta  # variavel inteira retornada
