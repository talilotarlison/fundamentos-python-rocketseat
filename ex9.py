# Exemplos de concatenação em Python

# Concatenando strings com o operador +
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

# Concatenando strings com f-strings (Python 3.6+)
idade = 25
mensagem = f"Meu nome é {nome} {sobrenome} e eu tenho {idade} anos."
print(mensagem)

# Concatenando strings com o método format()
cidade = "São Paulo"
estado = "SP"
endereco = "Cidade: {}, Estado: {}".format(cidade, estado)
print(endereco)

# Concatenando strings com join()
palavras = ["Python", "é", "muito", "legal"]
frase = " ".join(palavras)
print(frase)

# Concatenando strings com o operador %
nome = "Ana"
idade = 30
mensagem = "Meu nome é %s e eu tenho %d anos." % (nome, idade)
print(mensagem)