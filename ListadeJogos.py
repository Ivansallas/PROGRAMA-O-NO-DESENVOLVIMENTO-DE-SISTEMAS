import JogodaForca
import jogoAdivinhação
def escolhe_jogo():
    print("*********************************")
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    print("*********************************")
    print("(1) Forca \n(2) Adivinhação")

    jogo = int(input("Escolha Qual jogo Você quer Jogar?\n"))

    if jogo == 1:
        print("Jogando forca")
        JogodaForca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        jogoAdivinhação.jogar()


if __name__ == "__main__":
    escolhe_jogo()
