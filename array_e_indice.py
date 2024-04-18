# 1. Crie uma função que declara um array com 4 nomes diferentes e imprime cada um deles um embaixo do outro. Ao final faça um commit no GitHub.

# Exemplo de entrada: Nenhuma Exemplo de saída:

# 1-João 2-Maria 3-Fulano 4-Ciclano
def mostra_nomes():
    nomes = ["João", "Maria", "Fulano", "Ciclano"]
    
    print("1 -", nomes[0])
    print("2 -", nomes[1])
    print("3 -", nomes[2])
    print("4 -", nomes[3])

mostra_nomes()

# 2. Crie uma função que declara um array com 4 nomes diferentes e imprime o primeiro e último nome do array. Ao final faça um commit no GitHub.

# Exemplo de entrada : Nenhuma Exemplo de saída: 1-João 4-Beltrano

def mostra_nome_especifico():
    nomes = ["Tatiana", "Lorane", "Otávio", "Gabriel"]

    print("1 -> ", nomes[0])
    print("4 -> ", nomes[3])

mostra_nome_especifico()

# 3. Crie uma função que declara um array com 4 nomes diferentes e imprime o conteúdo do segundo e terceiro índice do array. Ao final faça um commit no GitHub.

# Exemplo de entrada: Nenhuma Exemplo de saída: 2-Maria 3-Fulano

def mostra_nomes_2_e_3():
    nomes = ["Gabriela", "Marta", "Guilherme", "Mario"]

    print("2 => ", nomes[1])
    print("3 => ", nomes[3])

mostra_nomes_2_e_3()

# 4. Crie uma função que pede 3 nomes de alimentos digitado pelo usuário e substitui os elementos do array [“Macarrão”, “Pepino”, “Batata”] com esses 3 alimentos. Imprima o nome dos alimentos um abaixo do outro. Ao final faça um commit no GitHub.

# array_inicial = [“Macarrão”, “Pepino”, “Batata”]

# Exemplo de entrada: Arroz, Feijão, Farinha Exemplo de saída: 1 – Arroz 2 - Feijão 3 – Farinha

def nomes_de_comida():
    comidas = ["Macarrão", "Pepino", "Batata"]

    comida1 = input("Digite o nome de uma comida: ")
    comidas[0] = comida1

    comida2 = input("Digite o nome de uma comida: ")
    comidas[1] = comida2

    comida3 = input("Digite o nome de uma comida: ")
    comidas[2] = comida3

    print("Comida 1: ", comidas[0])
    print("Comida 2: ", comidas[1])
    print("Comida 3: ", comidas[2])

nomes_de_comida()