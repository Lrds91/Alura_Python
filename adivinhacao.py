import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)  # gera num aleatorio entre 0.0 e 1.0
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível de dificuldade: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input(
            "Digite um número entre 1 e 100: ")  # método utilizado para pegar o input do usuário, sempre devolve o que o usuário digitar como string

        print("Você digitou ", chute_str)

        chute = int(chute_str)  # variável responsável por converter a string do input para int

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # volta ao início da interação com o jogador

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos! :)".format(pontos))
            break
        else:  # else não aceita receber condições, caso queira adicionar mais condicionais deve-se usar elif
            if (chute_maior):
                print("Você errou! :( O seu chute foi maior que o número secreto.")
            elif (chute_menor):
                print("Você errou! :( O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)  # 40-60 = -20
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")


if __name__ == "__main__": #utilizado para funcionar caso seja executado pelo arquivo adivinhacao.py
    jogar()
