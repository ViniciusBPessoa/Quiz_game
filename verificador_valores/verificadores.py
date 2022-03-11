def leia_menu(lista, pergunta = 'Qual voce deseja selecionar: '):  # verifica se os valores respondidos em menus são inteiros e dentro das possibilidades
    while True:

        try:  # retorna erros casso o mesmo ocorra
            minha_alternativa = int(input(f"\033[33m\n{pergunta}\033[m"))

        except(TypeError, ValueError):
            print("\033[31mPor favor insira apenas numeros inteiros!!!\033[m")
            continue

        if minha_alternativa > len(lista) or minha_alternativa <= 0:
            print(f"\033[31mValores dentro de penas valores entre 1 e {len(lista)}\033[m")
            continue

        else:
            return minha_alternativa

def verifica_int(tamanho_perguntas):  # verifica se numeros em jeral são inteiros

    while True:

        try:  # retorna erros casso o mesmo ocorra
            meu_valor = int(input("Qual numero da questão que você quer excluir(-1 cancela): "))

        except(ValueError, TypeError):
            print("\033[31mPor favor insira apenas numeros inteiros!!!\033[m")
            continue

        if meu_valor > tamanho_perguntas or meu_valor <= -1:

            if meu_valor == 0 or meu_valor == -1:
                return meu_valor

            print(f"\033[31mValores dentro de penas valores entre -1 e {tamanho_perguntas + 1}\033[m")
            continue

        else:
            return meu_valor
