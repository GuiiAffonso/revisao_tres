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