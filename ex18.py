import random

# Exemplo 11: Gerando um número aleatório com random.randint
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatório entre 1 e 10: {numero_aleatorio}")

# Exemplo 12: Escolhendo um elemento aleatório de uma lista com random.choice
frutas = ["maçã", "banana", "laranja", "uva"]
fruta_aleatoria = random.choice(frutas)
print(f"Fruta aleatória: {fruta_aleatoria}")

# Exemplo 13: Embaralhando uma lista com random.shuffle
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista embaralhada: {numeros}")

# Exemplo 14: Gerando um número de ponto flutuante aleatório com random.uniform
numero_float = random.uniform(1.5, 5.5)
print(f"Número float aleatório entre 1.5 e 5.5: {numero_float}")

# Exemplo 15: Gerando múltiplos números aleatórios com random.sample
numeros = list(range(1, 11))
amostra = random.sample(numeros, 3)
print(f"Três números aleatórios da lista: {amostra}")