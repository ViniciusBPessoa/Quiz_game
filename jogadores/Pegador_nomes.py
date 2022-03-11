import pandas as pd  #  importa o pandas para poder trabalhar com arquivos tipo xlsx



def plota_nomes(nome = int(0)):  #  mostra em tela os nomes e os melhores resultados em ordem decressente
    
    jogadores = pd.read_excel('jogadores/Jogadores.xlsx', engine= "openpyxl")

    if nome != 0:  # realiza a pesquisa por nomes 
        jogadores = jogadores.loc[jogadores["Nome"] == f'{nome}']

    jogadores = jogadores.sort_values('Pontuação', ascending = False)

    jogadores = jogadores.head(10)

    jogadores.to_excel("jogadores/Jogadores_pos_seleção.xlsx", index=False)

    jogadores = pd.read_excel('jogadores/Jogadores_pos_seleção.xlsx', engine= "openpyxl")

    if jogadores.shape[0] != 0:

        for player in range (0, jogadores.shape[0]):

            print (f"\033[36m{player + 1:<2}\033[m - {jogadores.loc[player, 'Nome']:.<15} - \033[32m{jogadores.loc[player, 'Pontuação']} R$\033[m")

    else:  # apresenta uma mensagem em tela caso não seja obtido nem um resultado
        print("\033[31mNão tivemos nenhum resultado!\033[m")


def incert_nome(nome, pontuação):  # adciona um nome e um resultado apos o termino de uma partida! tudo salvo em arquivos tipo xlsx

    jogadores = pd.read_excel('jogadores/Jogadores.xlsx', engine= "openpyxl")

    jogadores = jogadores.append({'Nome': f'{nome}', 'Pontuação': pontuação}, ignore_index = True)

    jogadores.to_excel('jogadores/Jogadores.xlsx', index=False)
