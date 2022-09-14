import random

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________          ")
    print("   /               \         ")
    print("  /                 \        ")
    print(" /                   \       ")
    print(" |   XXXX     XXXX   |       ")
    print(" |   XXXX     XXXX   |       ")
    print(" |   XXX       XXX   |       ")
    print(" |                   |       ")
    print(" \__      XXX      __/       ")
    print("   |\     XXX     /|         ")
    print("   | |           | |         ")
    print("   | I I I I I I I |         ")
    print("   |  I I I I I I  |         ")
    print("   \_             _/         ")
    print("     \_         _/           ")
    print("       \_______/             ")

def acerta_letra(palavra,kick,status):
    index = 0
    for letra in palavra:
        if(kick == letra):
            status[index] = letra
        index += 1

def pede_chute():
    kick = input('Escolha letra')
    kick = kick.strip().upper()
    return kick

def inicia_status(p):
    return ['_' for letra in p]

def obter_palavra_secreta():
        arquivo = open('palavras.txt','r',encoding='utf-8')
        listap = []

        for linha in arquivo:
            linha = linha.strip()
            listap.append(linha)

        arquivo.close()

        numero = random.randrange(0,len(listap))
        palavra = listap[numero].upper()

        return palavra

def imprime_mensagem_abertura():
    print("************************************")
    print("***Bem vindo(a) ao jogo da Forca!***")
    print("************************************")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()