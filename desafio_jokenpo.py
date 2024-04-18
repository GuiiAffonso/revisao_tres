# Desafio: Pedra, Papel, Tesoura
import random

def jogar():
    # try:

    opcao = str

    while(opcao != "N"):
        opcao = True

        print("Escolha a sua opção:\n","[0] - Pedra\n","[1] - Papel\n","[2] - Tesoura")
        computador = int(random.randint(0,2))
        player = int(input())
        opcao = str

        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("JO...\n""KEN...\n""PO!\n")

        print(f'O computador escolheu:{computador}\nO jogador escolheu:{player}')
        
        if (player == 0 and computador == 2):
            print("Jogador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
            
        elif(player == 0 and computador == 1):
            print("Computador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
            
        elif(player == 1 and computador == 2):
            print("Jogador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
        
        elif(player == 1 and computador == 0):
            print("Computador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
        
        elif(player == 2 and computador == 1):
            print("Jogador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
        
        elif(player == 2 and computador == 0):
            print("Computador venceu")
            opcao = str(input("Deseja continuar?\n "))
            resultado = (computador, player)
           
        else:
            print("Empate!")
            opcao = str(input("Deseja continuar?\n "))
        return resultado

jogar()