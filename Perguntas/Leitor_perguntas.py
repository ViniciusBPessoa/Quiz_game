from random import randint
import pandas as pd


def randomisa_questão(veses, arquivo): # retorna os valores referentes as perguntas respostas e alternativas corretas

    pergunta_exel = pd.read_excel(f'Perguntas/{arquivo}.xlsx', engine = 'openpyxl')

    possibilidades = [] # possue cada valor responssavel por uma possivel pergunta
    perguntas_escolhidas = [] # valor a ser retornado contendo todas as perguntas que o usuario quer

    while True: # retornas as perguntas que vão ser oferecidas ao jogador

        escolha = randint(0, pergunta_exel.shape[0] - 1) # randomiza as possiveis questões

        if escolha not in possibilidades: 
            possibilidades.append(escolha)

            if len(possibilidades) == veses:
                break

    for valor in possibilidades:
        perguntas_escolhidas.append(pergunta_exel.loc[valor])


    return perguntas_escolhidas  # retorna uma lista com as perguntas utilizadas

# as proximas linão se referem a o questionario retornado em suas referentes dificuldades

def modo_ease(numero):
    perguntas = randomisa_questão(numero, "Fácil")

    return perguntas
    

def modo_medio(numero):
    perguntas = randomisa_questão(numero, "Medio")

    return perguntas

def modo_dificio(numero):
    perguntas = randomisa_questão(numero, "Difícil")

    return perguntas

def modo_classico(): #o modo classico é uma formatação de perguntas em que a deficuldade é cressente (10 perguntas: 3 faceis, 4 medias, 3 dificeis)

    perguntas = []
    perguntas_1 = randomisa_questão(3, "Fácil")
    perguntas_2 = randomisa_questão(4, "Medio")
    perguntas_3 = randomisa_questão(3, "Difícil")

    for x in perguntas_1:
        perguntas.append(x)

    for x in perguntas_2:
        perguntas.append(x)

    for x in perguntas_3:
        perguntas.append(x)



    return perguntas
    
def adicionar_questao(pergunta, alternativa_1, alternativa_2, alternativa_3, alternativa_4, resposta, arquivo):  # responsavel por abrir o arquivo exel com o pandas e salvar o mesmo com uma nova pergunta

    
    pergunta_exel = pd.read_excel(f'Perguntas/{arquivo}.xlsx', engine = 'openpyxl')

    pergunta_exel = pergunta_exel.append({'Pergunta': f'{pergunta}', 'Resposta_1': f'{alternativa_1}', 'Resposta_2': f'{alternativa_2}', 'Resposta_3': f'{alternativa_3}', 'Resposta_4': f'{alternativa_4}', 'Resposta': int(resposta)}, ignore_index = True)

    pergunta_exel.to_excel(f'Perguntas/{arquivo}.xlsx', index=False)


def plot_perguntas(dificuldade): # exibe as perguntas de um arquivo exel em tela

    perguntas = []

    pergunta_exel = pd.read_excel(f'Perguntas/{dificuldade}.xlsx', engine = 'openpyxl')

    print('-'*60)

    for pergunta in range(0, pergunta_exel.shape[0]):
        perguntas.append(pergunta_exel.loc[pergunta, 'Pergunta'])
    
    for posicao, valores in enumerate(perguntas):
        print(f'\033[36m{posicao}\033[m - \033[33m{valores}\033[m')
        

def delete_pergunta(dificuldade, linha):  # responsavel por abrir o exel e salvar o arquivo novamente com uma correta pergunta a menos

    pergunta_exel = pd.read_excel(f'Perguntas/{dificuldade}.xlsx', engine = 'openpyxl')

    pergunta_exel = pergunta_exel.drop(linha, axis=0)

    pergunta_exel.to_excel(f'Perguntas/{dificuldade}.xlsx', index = False)
