



## criando alguns jogos em sequencia para praticar os códigos, e mostrar meus conhecimentos.
## pedra papel tesoura


import random

def playerChoice():
    return input(f"Escolha entre pedra papel tesoura ").lower()

def computerChoice():
    computerOptions = ["pedra", "papel", "tesoura"]
    return random.choice(computerOptions)

def game(player,computer):
    if player == computer:
        print(f"Foi empate. Escolha do jogador: {player}. Escolha do computador: {computer}")
        return "empate"
    elif player == "pedra" and computer == "tesoura":
        print(f"Você ganhou. Escolha do jogador: {player}. Escolha do computador: {computer}")
        return "playerWon"
    elif player == "papel" and computer == "pedra":
        print(f"Você ganhou. Escolha do jogador: {player}. Escolha do computador: {computer}")
        return "playerWon"
    elif player == "tesoura" and computer == "papel":
        print(f"Você ganhou. Escolha do jogador: {player}. Escolha do computador: {computer}")
        return "playerWon"
    else:
        print(f"Você perdeu. Escolha do jogador: {player}. Escolha do computador: {computer}")
        return "computerWon"

playerPoints = 0
computerPoints = 0
gameOn = True
print(f"Player points: {playerPoints}. ")
print(f"Computer points: {computerPoints}. ")


while gameOn:

    resultado = game(playerChoice(), computerChoice())

    if resultado == "empate":
        print(f"Player points: {playerPoints}. ")
        print(f"Computer points: {computerPoints}. ")
    elif  resultado == "playerWon":
        playerPoints += 1
        if playerPoints == 3:
            print(f"Você fez 3 pontos primeiro, você ganhou o jogo.")
            print(f"Pontuação final do jogador: {playerPoints}. contra pontuação final do computador: {computerPoints}")
            gameOn = False
        else:
            print(f"Player points: {playerPoints}. ")
            print(f"Computer points: {computerPoints}. ")
    else:
        computerPoints += 1
        if computerPoints == 3:
            print(f"O computador fez 3 pontos primeiro, você perdeu o jogo.")
            print(f"Pontuação final do jogador: {playerPoints}. contra pontuação final do computador: {computerPoints}")
            gameOn = False
        else:
            print(f"Player points: {playerPoints}. ")
            print(f"Computer points: {computerPoints}. ")



# jogo da forca

print("Jogo da forca.")

bibliotecaDePalavras = ["monitor", "teclado", "controle"]
palavra = random.choice(bibliotecaDePalavras)

mostrar = []

for letra in palavra:
    mostrar += "_"


vidasJogador = 6
letrasTentadas = ""
jogoLigado = True
print(f"Palavra secreta: {mostrar}.")
print(f"Número de vidas do jogador: {vidasJogador}.")

while jogoLigado:

    letraTentativa = input("Tente adivinhar uma letra da palavra secreta.")
    if letraTentativa in letrasTentadas or letraTentativa in mostrar:
        print(f"Você já tentou essa letra.")
    letrasTentadas += letraTentativa

    for letter in range(0, len(palavra)):
        letra = palavra[letter]
        if letraTentativa == letra:
            mostrar[letter] = letra
    if letraTentativa not in palavra:
        print(f"Você errou, a palavra secreta não tem essa letra.")
        vidasJogador -= 1
        if vidasJogador == 0:
            print(f"Infelizmente o seu número de vidas chegou a 0. Você perdeu o jogo.")
            print(f"Palavra secreta: {palavra}.")
            jogoLigado = False
        else:
            print(f"Você perdeu uma vida.")
            print(f"Número de vidas do jogador: {vidasJogador}.")
            print(f"Palavra secreta: {mostrar}.")

    elif "_" not in mostrar:
        print(f"Você adivinhou a palavra secreta {palavra} parabéns!")
        jogoLigado = False

    else:
        print(f"Você acertou! A letra '{letraTentativa}' esta na palavra secreta.")
        print(f"Palavra secreta: {mostrar}.")


