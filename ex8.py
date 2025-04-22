# Exemplo de uso de texto em variáveis no Python

# Definindo variáveis de texto
nome = "João"
cidade = "São Paulo"
mensagem = f"Olá, meu nome é {nome} e eu moro em {cidade}."

# Exibindo a mensagem
print(f"""\
Olá, meu nome é {nome} e eu moro em {cidade}.
Meu nome tem {len(nome)} letras e minha cidade tem {len(cidade)} letras.
A soma do comprimento do meu nome e da minha cidade é {len(nome) + len(cidade)}.
""")