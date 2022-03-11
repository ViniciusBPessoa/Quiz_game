import pandas as pd

def leitor_arquivo(arquivo_pedido): # devolve o arquivo .TXT ja lido
    
    arquivo = open(f"Perguntas/{arquivo_pedido}.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    return linhas

def criador_de_exel(txt, dificuldade):

    linhas = leitor_arquivo(txt)

    jogadores = pd.read_excel('Perguntas/Padrão_exel.xlsx', engine= "openpyxl")

    posi = 0

    for x in linhas:

        if posi != len (linhas):
            jogadores = jogadores.append({"Pergunta": linhas[posi], "Resposta_1": linhas[posi + 1], "Resposta_2": linhas[posi + 2], "Resposta_3": linhas[posi + 3], "Resposta_4": linhas [posi+ 4], "Resposta": linhas[posi + 5]}, ignore_index = True)

            posi += 6


    jogadores.to_excel(f"Perguntas/{dificuldade}.xlsx", index = False)


criador_de_exel('facil', "Fácil")
