def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "python"
    enforcou = False
    acertou = True

    #enquanto não enforcou e não acertou
    while(not enforcou == True and not acertou == False):

        chute = input("Qual a letra?")
        chute = chute.strip()  # remove espaços em brandco caso sejam colocados pelo usuário

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index +1
        print("jogando...")

    print("Fim de jogo!")


if __name__ == "__main__": #utilizado para funcionar caso seja executado pelo arquivo forca.py
    jogar()
