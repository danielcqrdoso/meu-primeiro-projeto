#Sou o Daniel Bernardes Cardoso
import random
from os import system

c = 1
while c == 1:
    print("----------------------------")
    print("|escolha uma alternativa   |")
    print("|1- papel                  |")
    print("|2- tesoura                |")
    print("|3- pedra                  |")
    print("----------------------------")
    d = int(input("escreva sua escolha: "))
    if d < 1 or d > 3:
        print("peço que coloque um dos numeros acima")
    else:
        a = random.randint(1, 3)
        print(a)
        if d == a:
            print("empate")
        elif d == 1 and a == 2:
            print("o computador ganhou")
        elif d == 2 and a == 1:
            print("tu ganhou")
        elif d == 3 and a == 2:
            print("tu ganhou")
        elif d == 2 and a == 3:
            print("o computador ganhou")
        elif d == 1 and a == 3:
            print("tu ganhou")
        elif d == 3 and a == 1:
            print("o computador ganhou")
    c = int(input("digite 1 se quer repetir: "))
    system("cls")
