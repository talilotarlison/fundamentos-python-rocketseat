# Exemplo de tuplas em Python

# Criando uma tupla
frutas = ("maçã", "banana", "cereja")

# Acessando elementos da tupla
print(frutas[0])  # Saída: maçã
print(frutas[1])  # Saída: banana

# Tentativa de modificar um elemento (isso causará um erro, pois tuplas são imutáveis)
# frutas[0] = "laranja"  # TypeError: 'tuple' object does not support item assignment

# Diferenciais das tuplas:
# 1. Imutabilidade: Tuplas não podem ser alteradas após sua criação.
# 2. Desempenho: São mais rápidas que listas para operações de leitura.
# 3. Uso como chave em dicionários: Tuplas podem ser usadas como chaves, pois são imutáveis.

# Exemplo de uso como chave em um dicionário
coordenadas = {(10, 20): "Ponto A", (30, 40): "Ponto B"}
print(coordenadas[(10, 20)])  # Saída: Ponto A

# Desempacotamento de tuplas
x, y, z = frutas
print(x)  # Saída: maçã
print(y)  # Saída: banana
print(z)  # Saída: cereja

# Métodos das tuplas

# count(): Retorna o número de vezes que um valor aparece na tupla
numeros = (1, 2, 3, 1, 2, 1)
print(numeros.count(1))  # Saída: 3

# index(): Retorna o índice da primeira ocorrência de um valor na tupla
print(numeros.index(3))  # Saída: 2

# Nota: Tuplas possuem apenas esses dois métodos, pois são imutáveis.