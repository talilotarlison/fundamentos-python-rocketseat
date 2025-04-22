idade = 20
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")


# Exemplo de uso de True e False em Python com variáveis
# Definindo variáveis de texto

nome = "Alice"
if nome == "Alice":
    print("Olá, Alice!")
else:
    print("Olá, estranho!")

# Exemplo de if aninhado
idade = 20
nome = "Alice"

if idade >= 18:
    if nome == "Alice":
        print("Alice é maior de idade.")
    else:
        print("Você é maior de idade, mas não é Alice.")
else:
    if nome == "Alice":
        print("Alice é menor de idade.")
    else:
        print("Você é menor de idade e não é Alice.")

# Exemplo de uso de operador ternário para verificar se pode tirar carteira
idade = 20
pode_tirar_carteira = "Pode tirar carteira de motorista." if idade >= 18 else "Não pode tirar carteira de motorista."
print(pode_tirar_carteira)