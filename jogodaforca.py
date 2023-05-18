import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from time import sleep

# Carrega a música e os sons
pygame.mixer.init()
pygame.mixer.music.load("maintheme.mp3")
pygame.mixer.music.play(-1)
acertou = pygame.mixer.Sound("acertou.wav")
errou = pygame.mixer.Sound("errou.wav")
vitoria = pygame.mixer.Sound("vitoria.wav")
derrota = pygame.mixer.Sound("derrota.wav")
gameover = pygame.mixer.Sound("gameover.wav")

# Função que printa a imagem da forca dependendo dos erros e acertos do jogador
def forca():
    if tentativas == 0:
        print("__________")
        print("| /      |")
        print("|/")
        print("|")
        print("|")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 1:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|")
        print("|")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 2:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|        |")
        print("|")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 3:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|       /|")
        print("|")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 4:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|       /|\\")
        print("|")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 5:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|       /|\\")
        print("|       /")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))
        print(f"Você ainda pode errar {chances-tentativas} vezes")

    elif tentativas == 6:
        print("__________")
        print("| /      |")
        print("|/       O")
        print("|       /|\\")
        print("|       / \\")
        print("|__")
        print("Qual é a palavra?", "".join(resposta))


# Abertura
errou.play()
print("░░░░░░░░▓█▒░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
print("░░░░░░░█████▒░░░░░▒████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
errou.play()
print("░░░░░▓██▓░░░▓█░░░▓██████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
print("░░░░▓██░░░░░░░▓▓▓██████░░░░░░░░░░░▒████████░░▒▓████▓░░░░██████▓▒░░░░░▓█████▒░░░░░▒████░░░░")
sleep(0.2)
errou.play()
print("░░░██▓░░░░░░░░░▒███████░░░░░░░░░░░▒████████░▒████████░░░████████▓░░░████▓███▓░░░░▓████▓░░░")
sleep(0.2)
print("░░██▒░░░░░░░░░░████████▒░░░░░░░░░░▒███░░░░░░▓███░░███▓░░███▓░▒███▒░▒███░░▒███░░░░██████░░░")
sleep(0.2)
errou.play()
print("░██▒░░░░░░░░░░█████████▓░░░░░░░░░░▒███░░░░░░███▓░░███▓░░███▓░░███▓░▒███░░▒███░░░▒██████░░░")
sleep(0.2)
print("▒█▒░░░░░░░░░░░▒▓███████▓░░░░░░░░░░▒███░░░░░░███▓░░███▓░░███▓░░███▒░▒███░░░░░░░░░▓██▓▓██▒░░")
sleep(0.2)
errou.play()
print("█▒░░░░░░░░░░░░░▓█████████▒░░░░░░░░▒██████▒░░███▓░░███▓░░████▓████░░▒███░░░░░░░░░███▒▒██▓░░")
sleep(0.2)
print("▓░░░░░░░░░░░░░░█████████░▓▓░░░░░░░▒██████▒░░███▓░░███▓░░████████░░░▒███░░░░░░░░░███░░███░░")
sleep(0.2)
errou.play()
print("░░░░░░░░░░░░░░░█████████░░░▓▓░░░░░▒███░░░░░░███▓░░███▓░░███▓▒███░░░▒███░░░░░░░░▒███░░███▒░")
sleep(0.2)
print("░░░░░░░░░░░░░░▓█████████▒░░░▒▓░░░░▒███░░░░░░███▓░░███▓░░███▓░███▒░░▒███░░▒███░░▓████████▓░")
sleep(0.2)
errou.play()
print("░░░░░░░░░░░░░░██████████▒░░░░░░░░░▒███░░░░░░███▓░░███▓░░███▓░▓███░░▒███░░▒███░░███▓▓▓████░")
sleep(0.2)
print("░░░░░░░░░░░░░▒██████████░░░░░░░░░░▒███░░░░░░▓███▓▓███▒░░███▓░░███░░░███▓▒███▓░▒███░░░░███░")
sleep(0.2)
errou.play()
print("░░░░░░░░░░░░░███████████░░░░░░░░░░▒███░░░░░░░▓██████▒░░░███▓░░███▓░░░██████▓░░▓██▓░░░░███▓")
sleep(0.2)
print("░░░░░░░░░░░░▒██████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
errou.play()
print("░░░░░░░░░░▓▓███████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
print("░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
sleep(0.2)
acertou.play()

# Inicia o jogo
while True:
    # Escolhe o tema, cria a lista que recebe os nomes do arquivo .txt do tema, sorteia a palavra
    print("""\nEscolha um tema:
    1. Animais
    2. Marcas de carros
    3. Países""")

    tema = input("\nQual tema você escolhe? [1/2/3]: ")

    while tema not in ["1", "2", "3"]:
        errou.play()
        print("Escolha 1, 2 ou 3.")
        tema = input("Qual tema você escolhe? [1/2/3]: ")

    if tema == "1":
        arquivo = open(file="lista_animais.txt", mode="r", encoding="UTF-8")
        lista_tema = []
        for line in arquivo:
            line = line.strip()
            lista_tema.append(line)
        print("\nO tema é ANIMAIS!")
    elif tema == "2":
        arquivo = open(file="lista_carros.txt", mode="r", encoding="UTF-8")
        lista_tema = []
        for line in arquivo:
            line = line.strip()
            lista_tema.append(line)
        print("\nO tema é MARCAS DE CARROS!")
    elif tema == "3":
        arquivo = open(file="lista_paises.txt", mode="r", encoding="UTF-8")
        lista_tema = []
        for line in arquivo:
            line = line.strip()
            lista_tema.append(line)
        print("\nO tema é PAÍSES!")

    acertou.play()

    palavra = random.choice(lista_tema).upper()
    resposta = ["_"] * len(palavra)
    letras_escolhidas = []

    tentativas = 0
    chances = 6

    print("__________")
    print("| /      |")
    print("|/")
    print("|")
    print("|")
    print("|__")
    print("Qual é a palavra?", "".join(resposta))
    print(f"Você pode errar {chances} vezes")

    # Apenas permite digitar letras. Não são permitidos números, mais de um caractere por vez ou repetir letras.
    while tentativas < chances and "".join(resposta) != palavra:
        letra = str(input("\nEscolha uma letra: ").upper())
        if letra in letras_escolhidas:
            errou.play()
            print("\033[0;31mVocê já escolheu essa letra!\033[0;0m")
            continue
        elif len(letra) > 1:
            errou.play()
            print("\033[0;31mVocê só pode digitar um caractere por vez!\033[0;0m")
            continue
        elif not letra.isalpha():
            errou.play()
            print("\033[0;31mVocê só pode digitar letras!\033[0;0m")
            continue

        letras_escolhidas.append(letra)

        if letra in palavra:
            print("\033[0;32mAcertou!\033[0;0m")
            acertou.play()
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    resposta[i] = letra
        else:
            print("\033[0;31mErrou!\033[0;0m")
            errou.play()
            tentativas += 1

        forca()

        print("As letras que você já tentou são:")
        for item in letras_escolhidas:
            print(item, end=" ")

    # Uma vez encerradas as tentativas, printa o resultado e qual era a palavra.
    if tentativas > 0 and tentativas == chances:
        print("\n\n\033[0;31mQue pena! Você perdeu!\033[0;0m")
        pygame.mixer.music.stop()
        derrota.play()
    else:
        print("\n\n\033[0;32mVocê ganhou! Parabéns!\033[0;0m")
        pygame.mixer.music.stop()
        vitoria.play()

    print("A palavra era", palavra.upper()+"!")

    # Configura para reiniciar ou encerrar o jogo
    jogardenovo = str(input("\nJogar mais uma partida? (\033[0;32mS\033[0;0m/\033[0;31mN\033[0;0m): ").upper())

    while jogardenovo not in ["S", "N"]:
        errou.play()
        print("Escolha S ou N.")
        jogardenovo = str(input("\nJogar mais uma partida? (\033[0;32mS\033[0;0m/\033[0;31mN\033[0;0m): ").upper())

    # Escolher S mantém o "while True" do jogo e reinicia; escolher N quebra o loop e printa a mensagem de despedida
    if jogardenovo == "S":
        acertou.play()
        pygame.mixer.music.play(-1)
        continue
    if jogardenovo == "N":
        break

gameover.play()
print("GAME OVER")
sleep (2.5)
