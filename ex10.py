# Exemplos de métodos usados em strings no Python

texto = " Olá, Mundo! "

# Métodos de manipulação
print(texto.strip())         # Remove espaços no início e no fim
print(texto.lower())         # Converte para minúsculas
print(texto.upper())         # Converte para maiúsculas
print(texto.capitalize())    # Primeira letra maiúscula
print(texto.title())         # Primeira letra de cada palavra maiúscula
print(texto.swapcase())      # Inverte maiúsculas e minúsculas

# Métodos de consulta
print(texto.startswith(" Olá"))  # Verifica se começa com " Olá"
print(texto.endswith("! "))      # Verifica se termina com "! "
print(texto.find("Mundo"))       # Retorna o índice da primeira ocorrência
print(texto.rfind("o"))          # Retorna o índice da última ocorrência
print(texto.count("o"))          # Conta quantas vezes "o" aparece
print("Mundo" in texto)          # Verifica se "Mundo" está na string

# Métodos de substituição
print(texto.replace("Mundo", "Python"))  # Substitui "Mundo" por "Python"

# Métodos de divisão e junção
print(texto.split())             # Divide a string em uma lista
print("-".join(["Olá", "Mundo"]))  # Junta uma lista em uma string com "-"

# Métodos de alinhamento
print(texto.center(20, "*"))     # Centraliza com preenchimento
print(texto.ljust(20, "-"))      # Alinha à esquerda com preenchimento
print(texto.rjust(20, "-"))      # Alinha à direita com preenchimento

# Métodos de verificaçlsão
print(texto.isalpha())           # Verifica se contém apenas letras
print(texto.isdigit())           # Verifica se contém apenas dígitos
print(texto.isalnum())           # Verifica se contém apenas letras e números
print(texto.isspace())           # Verifica se contém apenas espaços
print(texto.istitle())           # Verifica se está no formato de título
print(texto.islower())           # Verifica se está em minúsculas
print(texto.isupper())           # Verifica se está em maiúsculas

# Métodos de codificação e decodificação
texto_codificado = texto.encode("utf-8")  # Codifica a string para bytes usando UTF-8
print(texto_codificado)

texto_decodificado = texto_codificado.decode("utf-8")  # Decodifica os bytes de volta para string
print(texto_decodificado)

# Explicação:
# - encode(): Converte a string em uma sequência de bytes usando a codificação especificada (ex: UTF-8).
# - decode(): Converte a sequência de bytes de volta para string usando a mesma codificação.