# Exemplo de dicionários e seus métodos em Python

# Criando um dicionário
dados_pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores
print(dados_pessoa["nome"])  # Saída: João

# Adicionando um novo par chave-valor
dados_pessoa["profissao"] = "Engenheiro"
print(dados_pessoa)

# Atualizando um valor
dados_pessoa["idade"] = 26
print(dados_pessoa)

# Removendo um item
dados_pessoa.pop("cidade")
print(dados_pessoa)

# Verificando se uma chave existe
if "nome" in dados_pessoa:
    print("A chave 'nome' está presente no dicionário.")

# Iterando sobre as chaves
for chave in dados_pessoa:
    print(chave)

# Iterando sobre os valores
for valor in dados_pessoa.values():
    print(valor)

# Iterando sobre os itens (chave e valor)
for chave, valor in dados_pessoa.items():
    print(f"{chave}: {valor}")

# Obtendo todas as chaves
chaves = dados_pessoa.keys()
print(chaves)

# Obtendo todos os valores
valores = dados_pessoa.values()
print(valores)

# Limpando o dicionário
dados_pessoa.clear()
print(dados_pessoa)  # Saída: {}

# Removendo um item usando 'del'
dados_pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

del dados_pessoa["cidade"]
print(dados_pessoa)  # Saída: {'nome': 'João', 'idade': 25}