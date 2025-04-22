# Exemplo de lista e seus métodos

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva", 325, True, False]

# Adicionando um item à lista
frutas.append("manga")
print("Após append:", frutas)

# Inserindo um item em uma posição específica
frutas.insert(2, "abacaxi")
print("Após insert:", frutas)

# Removendo um item da lista
frutas.remove("banana")
print("Após remove:", frutas)

# Removendo o último item da lista
ultimo = frutas.pop()
print("Após pop:", frutas)
print("Item removido:", ultimo)

# Encontrando o índice de um item
indice = frutas.index("laranja")
print("Índice de 'laranja':", indice)

# Ordenando a lista
frutas.sort()
print("Após sort:", frutas)

# Revertendo a ordem da lista
frutas.reverse()
print("Após reverse:", frutas)

# Contando a ocorrência de um item
frutas.append("maçã")
contagem = frutas.count("maçã")
print("Contagem de 'maçã':", contagem)

# Copiando a lista
copia_frutas = frutas.copy()
print("Cópia da lista:", copia_frutas)

# Limpando a lista
frutas.clear()
print("Após clear:", frutas)

# Fatiando a lista por posição do array
copia_frutas = ["maçã", "banana", "laranja", "uva", "manga"]
fatia = copia_frutas[1:4]  # Obtendo itens da posição 1 até 3 (4 não é incluído)
print("Fatia da lista:", fatia)
print(copia_frutas[1:3])  # Obtendo itens da posição 1 até 3 (4 não é incluído)