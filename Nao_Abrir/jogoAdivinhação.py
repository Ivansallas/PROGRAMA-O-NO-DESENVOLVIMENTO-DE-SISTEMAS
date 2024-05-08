import random


def jogar():

    print("*********************************")
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("*********************************")

    # definindo numero secreto
    numerosecreto = random.randrange(1, 101)
    totaldetentativas = 0
    pontos = 1000
    # Adicionando niveis de pontuação no jogo
    print("Qual o nível de dificuldade?")
    print("[1] Fácil \n[2] Médio \n[3] Difícil")
    nivel = int(input("Defina o nível: "))
    # condicional de pontuação
    if nivel == 1:
        totaldetentativas = 20
    elif nivel == 2:
        totaldetentativas = 10
    else:
        totaldetentativas = 5

    # Adicionando a estrutura de loop
    for rodada in range(1, totaldetentativas + 1):
        # A função range() em Python é uma ferramenta poderosa para gerar sequências de números inteiros.
        print("Tentativa {} de {}".format(rodada, totaldetentativas))

        # estrutura de entrada de dados
        chutejogador = input("Digite um número entre 1 e 100! ")
        print("Você digitou: ", chutejogador)

        # convertendo chutejogador para intereiro e passando para variavel chute
        chute = int(chutejogador)

        # Adicionando um controle de continuação de rodada
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            # continue apenas pula para próxima iteração.
            continue

        # se numerosecreto for igual a chute se.nao voce errou
        if numerosecreto == chute:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if chute > numerosecreto:
                print("Você errou! O seu chute foi maior do que número secreto.")
            # adicionando mais uma condição
            elif chute < numerosecreto:
                print("Você errou! O seu chute foi menor do que número secreto.")
                # Para calcular o valor absoluto de um número em Python, podemos utilizar a função embutida abs().
                # Essa função recebe um número como argumento e retorna o seu valor absoluto
            pontos_perdidos = abs(numerosecreto - chute)
            pontos = pontos - pontos_perdidos

    # fim do jogo
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
