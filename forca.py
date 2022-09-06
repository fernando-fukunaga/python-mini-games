import random
import forca_funcoes

def jogar():
    forca_funcoes.imprime_mensagem_abertura()

    palavra = forca_funcoes.obter_palavra_secreta()

    status = forca_funcoes.inicia_status(palavra)

    erros = 0
    ganhou = False
    perdeu = False
    jafoi = []

    print(status)

    while (not ganhou and not perdeu):
        kick = forca_funcoes.pede_chute()

        if(kick in jafoi):
            print('Essa letra já foi escolhida')

        else:
            if(kick in palavra):
                forca_funcoes.acerta_letra(palavra,kick,status)
            else:
                erros += 1
                forca_funcoes.desenha_forca(erros)

        perdeu = erros == 7
        ganhou = '_' not in status
        jafoi.append(kick)
        
        print(status)
        print('Chances restantes: {}'.format(7-erros))

    if(ganhou):
        forca_funcoes.imprime_mensagem_vencedor()
    else:
        forca_funcoes.imprime_mensagem_perdedor(palavra)

if(__name__ == "__main__"):
    jogar()
