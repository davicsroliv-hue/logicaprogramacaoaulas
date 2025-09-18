import random
import os

def escolher_palavras():
    with open("temas2.txt", "r", encoding="utf-8") as arquivo:
        temas = {}
        for linha in arquivo:
            tema, palavras = linha.strip().split(":")
            temas[tema] = palavras.split(",")

    print("Escolha um tema:")
    for i, tema in enumerate(temas.keys(), start=1):
        print(f"{i} - {tema}")

    escolha = int(input("Digite o número do tema: "))
    tema_selecionado = list(temas.keys())[escolha - 1]

    return random.choice(temas[tema_selecionado])

def jogar_forca():
    palavra = escolher_palavras()
    letras_corretas = []
    letras_erradas = []
    tentativas = 10

    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas or letra == " ":
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print('palavra:', palavra_escondida)
        print('letras erradas:', letras_erradas)
        print('tentativas restantes:', tentativas)

        if palavra_escondida.lower() == palavra.lower():
            print('parabéns você ganhou!!!')
            break
        elif tentativas == 0:
            print('você perdeu! a palavra era:', palavra)
            break

        letra_usuario = input('digite uma letra: ').lower()

        if letra_usuario in palavra.lower():
            print('letra correta')
            letras_corretas.append(letra_usuario)
        else:
            print('letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('seja bem vindo ao jogo da forca')
    jogar_forca()