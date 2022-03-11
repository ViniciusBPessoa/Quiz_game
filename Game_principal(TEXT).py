import webbrowser  # abre pajinas na web
from time import sleep  # Temporizador em menus
import pygame
from controladores_texto.Controladores import *  # importa os controladores de texto
from Perguntas.Leitor_perguntas import *  # importa os randomizadores e seletores de questões
from jogadores.Pegador_nomes import *

controlador = 0  # controla em qual parte do programa o jogador está

tempo_menu = 0.5  # empo em que o menu leva para aparecer

valores_premiacoes = [0, 500, 1000, 2000, 5000, 10000, 50000, 100000, 250000, 500000,
                      1000000]  # todos os valores de premiaçoes possiveis

numero_perguntas = len(valores_premiacoes) - 1  # quntas perguntas devem ser carregadas no sistema

pygame.init()

while True:  # loop principal

    if controlador == 0:  # menu inicial

        sleep(tempo_menu)  # temporizador para aparição do menu

        alternativa = cria_menu("Seja bem bindo a um jogo de perguntas e respostas!",
                                ["Novo Jogo", "Ranking", "Perguntas", "GitHub", "Youtube",
                                 "Sair"])  # criação do menu principal

        #  As prossimas linhas sãocom cada uma das possiveis respostas do menu, ecassando-as atraves da alteração da variavel alternativa

        if alternativa == 1:
            controlador = 1

        elif alternativa == 2:
            controlador = 2

        elif alternativa == 3:
            controlador = 4

        elif alternativa == 4:
            webbrowser.open("https://github.com/ViniciusBPessoa/Game_quiz_text")  # abertura da pagina na web 

        elif alternativa == 5:
            webbrowser.open("https://youtu.be/uSJlcuRCUQk")

        elif alternativa == 6:  # responsavel por fechar a aplicação

            print()
            break

        linha(60)

    if controlador == 1:  # A variavel controlador é responsavel por dizem em que parte do sistema o jogador está   nesse caso (novo jogo)

        sleep(tempo_menu)

        alternativa = cria_menu("Selecione uma dificuldade!", ["Clássico", "Fácil", "Médio", "Difícil",
                                                               "Voltar"])  # Foemação do menu para seleção de dificuladade

        #  cada uma das verificação a seguir é respónsavel por acertar a dificuldade ou voltar

        if alternativa != 5:  # recebe o nome do usuario

            while True:

                nome_player = str(input('\033[32mNome, em ate 15 caracteres: \033[m').capitalize())

                if len(nome_player) > 15:
                    print('\033[31mApenas nomes ate 15 caracteres!\033[m')
                    continue

                else:
                    break

        if alternativa == 1:
            perguntas = modo_classico()

        elif alternativa == 2:
            perguntas = modo_ease(numero_perguntas)

        elif alternativa == 3:
            perguntas = modo_medio(numero_perguntas)

        elif alternativa == 4:
            perguntas = modo_dificio(numero_perguntas)

        elif alternativa == 5:
            controlador = 0

        if alternativa != 5:
            controlador = 3

        linha(60)

    if controlador == 2:  # parte responsavel por procurar e mostrar em tela o Ranking de pontuaçoes dos jogadores

        sleep(tempo_menu)  # temporizador para a aparião do menu

        resposta = cria_menu('Esses são os melhores resultados em jogo!', ["Procurar Nome!", "Menu inicial!"],
                             Jogadores=True)  # criando o menu de procura de nomes e pontuaçoes

        if resposta == 1:

            while True:  # loop para certificar que o jogador colocol o nome de ate 15 caracteres

                nome_player = str(input(
                    '\033[32mNome, em ate 15 caracteres: \033[m').capitalize())  # recebe o nome que o jogador quer pesquisar

                if len(nome_player) > 15:
                    print('\033[31mApenas nomes ate 15 caracteres!\033[m')
                    continue

                else:
                    break

            linha(60)

            sleep(tempo_menu)

            resposta = cria_menu('Esses são os melhores resultados em jogo!',
                                 ["Voltar a tela de Ranking", "Menu inicial!"], Jogadores=True,
                                 plota_esse=f"{nome_player}")  # Plota o resultado da pesquisa
            linha(60)

            if resposta == 1:
                controlador = 2

            elif resposta == 2:
                controlador = 0

        else:
            controlador = 0

    if controlador == 3:  # menu responssavel pela tela em game

        contador = 0  # conta a quantidade de perguntas apresentadas ao usuario

        acertos = 0  # conta quantas quetões foram acertadas pelo usuario

        parar = True  # controla a opção de parada do usuario

        print("\033[33mO jogo esta para começar\033[m")

        sleep(tempo_menu)

        for valor in perguntas:  # loop que apresenta ao usuario qustão a questão

            tamanho = len(valor.loc["Pergunta"])  # carrega ga o tamanho da pergunta que sera realizada

            linha(tamanho + 6)

            print(f"\033[33m{valor.loc['Pergunta']:^{tamanho + 6}}\033[m")  # plota a qustão na tela

            # Apresenta ao usuario quanto ele ganha acertando, errando, parando.
            print(
                f"\033[31m   Errar: {int(valores_premiacoes[int(contador)] / 2)} R$\033[m - \033[32mAcertar: {valores_premiacoes[int(contador + 1)]} R$\033[m - \033[36mParar: {valores_premiacoes[int(contador)]} R$\033[m")

            print()
            for questao in range(1, 5):  # apresenta as possibilidades de resposta ao usuario

                print(f'\033[36m{questao}\033[m - {valor.loc[f"Resposta_{questao}"]}')

            print('\033[36m5\033[m - Parar')

            resposta = leia_menu([1, 2, 3, 4, 5])  # Questiona ao usuario qual é a sua resposta

            if resposta == valor.loc['Resposta']:
                acertos += 1
                 # toca sons caso o usuario acerte

            elif resposta == 5:
                # toca sons caso o usuario acerte
                break

            else:
                parar = False  # toca caso o usuario erre

                correta = valor.loc["Resposta"]

                print(f"Voce errou a resposta correta era \033[36m{valor.loc[f'Resposta_{correta}']}\033[m")

                sleep(1)

                break

            sleep(tempo_menu)

            contador += 1
            parar = True

        if parar == True:  # casso o usuario para
            pontuação = valores_premiacoes[acertos]

        else:  # Casso o usuario erre
            pontuação = valores_premiacoes[acertos] / 2

        resposta = cria_menu(f"\033[mParabéns \033[33m{nome_player}\033[m você ganhou \033[32m{pontuação} R$\033[m",
                             ['Voltar ao menu', 'abrir o Ranking'])  # tela de fim de jogo

        incert_nome(nome_player, pontuação)

        linha(60)

        if resposta == 1:  # recebe e realiza as funções do ultimo menu
            controlador = 0

        else:
            controlador = 2

    if controlador == 4:  # perguntas editor de perguntas
        resposta = cria_menu("Aqui voce pode adicionar e remover perguntas facilmente!",
                             ["Adicionar pergunta", "Remover pergunta", "Visualizar perguntas",
                              "Voltar ao menu"])  # menu de modificações de perguntas

        if resposta == 1:

            dificuldade = cria_menu('Qual deificuldade você deseja adicinar a pergunta!',
                                    ['Fácil', 'Medio', 'Difícil', 'Voltar'])  # menu de adicionar questões

            if dificuldade == 1:
                dificuldade = 'Fácil'

            elif dificuldade == 2:
                dificuldade = 'Medio'

            elif dificuldade == 3:
                dificuldade = 'Difícil'

            elif dificuldade == 4:
                controlador = 4

            if dificuldade == 'Fácil' or dificuldade == 'Medio' or dificuldade == 'Difícil':  # recebe cada uma das caracteristicas de uma pergunta
                linha(60)
                pergunta_adiciona = str(input("\033[32mQual a pergunta? \033[m"))
                linha(60)

                alternativa_adiciona_1 = str(input("\033[35mAqual a sua 1º alternativa: \033[m"))
                print()
                alternativa_adiciona_2 = str(input("\033[35mAqual a sua 2º alternativa: \033[m"))
                print()
                alternativa_adiciona_3 = str(input("\033[35mAqual a sua 3º alternativa: \033[m"))
                print()
                alternativa_adiciona_4 = str(input("\033[35mAqual a sua 4º alternativa: \033[m"))

                resposta_adiciona = leia_menu([1, 2, 3, 4], "Qual a resposta da sua pergunta? ")

                adicionar_questao(pergunta_adiciona, alternativa_adiciona_1, alternativa_adiciona_2,
                                  alternativa_adiciona_3, alternativa_adiciona_4, resposta_adiciona, dificuldade)

                print("\033[32mPergunta adicionada com sucesso!!\033[m")

        elif resposta == 2:  # remove perguntas

            dificuldade = cria_menu('Qual deificuldade você deseja remover a pergunta!', ['Fácil', 'Medio', 'Difícil',
                                                                                          'Voltar'])  # recebe a dificuldae em que a perunta sera removida

            if dificuldade == 1:
                dificuldade = 'Fácil'

            elif dificuldade == 2:
                dificuldade = 'Medio'

            elif dificuldade == 3:
                dificuldade = 'Difícil'

            elif dificuldade == 4:
                controlador = 4

            if dificuldade == 'Fácil' or dificuldade == 'Medio' or dificuldade == 'Difícil':
                plot_perguntas(dificuldade)  # apresenta em tela asopções de peuguntas

                pergunta_exel = pd.read_excel(f'Perguntas/{dificuldade}.xlsx', engine='openpyxl')

                tamanho_perguntas = pergunta_exel.shape[0] - 1

                escolha = verifica_int(tamanho_perguntas)

                if escolha != -1:  # remove a questão em especifico

                    delete_pergunta(dificuldade, escolha)

                    print("\033[32mPergunta excluida com sucesso!!\033[m")

                else:
                    print("\033[32mProcesso cancelado!\033[m")


        elif resposta == 3:  # mostra cada pergunta em uma dificuldade na tela

            dificuldade = cria_menu('Qual deificuldade você deseja remover a pergunta!',
                                    ['Fácil', 'Medio', 'Difícil', 'Voltar'])  # menu de seleçãe de dificuldade

            if dificuldade == 1:
                dificuldade = 'Fácil'

            elif dificuldade == 2:
                dificuldade = 'Medio'

            elif dificuldade == 3:
                dificuldade = 'Difícil'

            elif dificuldade == 4:
                controlador = 4

            if dificuldade == 'Fácil' or dificuldade == 'Medio' or dificuldade == 'Difícil':
                plot_perguntas(dificuldade)

        elif resposta == 4:
            controlador = 0
linha(27)
print("\033[31mObrigado por ter jogado!!!\033[m")
linha(27)
