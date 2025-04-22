
# Exemplo 1: Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Exemplo 2: Usando range para iterar por números
for i in range(5):
    print(f"Número: {i}")

# Exemplo 3: Iterando sobre uma string
palavra = "Python"
for letra in palavra:
    print(letra)

# Exemplo 4: Iterando com índice e valor usando enumerate
animais = ["gato", "cachorro", "pássaro"]
for indice, animal in enumerate(animais):
    print(f"Índice {indice}: {animal}")

# Exemplo 5: Iterando sobre um dicionário
idades = {"Alice": 25, "Bob": 30, "Carol": 22}
for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos")

# Exemplo 6: Usando for com condição
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")

# Exemplo 7: Usando for para criar uma lista com list comprehension
quadrados = [x**2 for x in range(10)]
print(quadrados)

# Exemplo 8: Iterando sobre duas listas ao mesmo tempo com zip
nomes = ["Ana", "Bruno", "Carlos"]
idades = [20, 25, 30]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")


# Exemplo 9: Usando for com break e continue
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        print("Número 3 encontrado, saindo do loop.")
        break  # Sai do loop quando encontra o número 3
    print(numero)

# Exemplo 10: Usando for com continue
for numero in numeros:
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(f"Número ímpar: {numero}")



# Exemplo 11: Usando range com início, fim e passo
for i in range(1, 10, 2):  # Inicia em 1, vai até 9, incrementando de 2 em 2
    print(f"Valor com passo: {i}")

# Exemplo 12: Usando range para iterar em ordem decrescente
for i in range(10, 0, -1):  # Inicia em 10, vai até 1, decrementando de 1 em 1
    print(f"Decrescente: {i}")

# Exemplo 13: Criando uma lista com range
lista_numeros = list(range(5, 15))  # Cria uma lista de números de 5 a 14
print(f"Lista criada com range: {lista_numeros}")

# Exemplo 14: Usando enumerate para iterar sobre uma lista com índice personalizado
cores = ["vermelho", "azul", "verde"]
for indice, cor in enumerate(cores, start=1):  # O índice começa em 1
    print(f"Cor {indice}: {cor}")



# Exemplo 15: Usando for com len(lista)
numeros = [10, 20, 30, 40, 50]
for i in range(len(numeros)):
    print(f"Índice {i}: Valor {numeros[i]}")