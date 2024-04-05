# 5. Crie uma função que imprime uma contagem de 0 a 20. Ao final faça um commit no GitHub.
def contador():
    contador = 0
    while (contador <= 20):
        print(contador)
        contador = contador + 1

# contador()

# 6. Crie uma função que imprime uma contagem de 0 até o número que o usuário digitou. Ao final faça um commit no GitHub.
#Solução while:
def contador_personalizado():
    numero_escolhido = int(input("Digite um número: "))

    cont = 0
    while (cont <= numero_escolhido):
        print(cont)
        cont = cont + 1

# contador_personalizado()

#Solução for:
def contador_personalizado():
    numero_escolhido = int(input("Digite um número: "))

    for i in range(numero_escolhido):
        print(i)

# contador_personalizado()

# 7. Crie uma função que imprime a tabuada de adição do número 2. Ao final faça um commit no GitHub.

# Entrada: Nenhuma Exemplo de saída:

# 2 + 1 = 3 2 + 2 = 4 2 + 3 = 5 2 + 4 = 6

#Solução while:

def tabuada_de_soma():
    numero_escolhido = 10

    cont = 0
    soma = 2
    while (cont <= numero_escolhido):
        resultado = cont + soma
        print(cont, "+", soma, "=", resultado)
        cont = cont + 1

# tabuada_de_soma()

# Solução for:

def tabuada_de_soma():

    for i in range(i = 0, i <= 10, i = 1):
        print(i)

# tabuada_de_soma()