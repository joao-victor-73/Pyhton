# Importando bibliotecas
import random
from os import system, name
import estagios
import mensagens as msg
import menu
import config


def limpa_tela():
    '''Função para limpar a tela a cada execução.'''

    # Se for Windows:
    if name == 'nt':
        _ = system('cls')

    # Se for outro sistema (Mac ou Linux):
    else:
        _ = system('clear')


def game():

    limpa_tela()

    msg.cabecalho()

    palavra = config.palavras_escolhida()

    print("\n|>>> Adivinhe a palavra abaixo: <<<|\n")

    # Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista para as digitadas
    letras_tentativas = []

    # Loop enquanto número de chances for maior do que zero:
    while chances > 0:

        print(estagios.display_hangman(chances))
        print(f"Palavra: {tabuleiro}")
        print("\n")

        # Tentativa / Digita a palavra desejada
        tentativa = input("\nDigite uma letra: ").upper().strip()

        # Condicional
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        # Condicional 2
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")

            # Loop
            for indice in range(len(lista_letras_palavras)):

                # Condicional 3
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print(f"\nVocê venceu! A palavra era: {palavra}")
                break

        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1

    # Condicional fora do while
    if "_" in tabuleiro:
        print(f"\nVocê perdeu! A palavra era: {palavra}")


def game_2():
    # Se a escolha for com 2 jogadores

    pass


# Principal


menu.escolha_jogadores()


game()


'''
FALTA COLOCAR A OPCAO PARA DOIS JOGADORES OU UM JOGADOR
'''