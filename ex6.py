# Exemplo de conversão de tipos em Python

# Convertendo string para inteiro
numero_str = "42"
numero_int = int(numero_str)
print(f"String para inteiro: {numero_int} (tipo: {type(numero_int)})")

# Convertendo inteiro para string
numero = 100
numero_str = str(numero)
print(f"Inteiro para string: {numero_str} (tipo: {type(numero_str)})")

# Convertendo string para float
numero_float_str = "3.14"
numero_float = float(numero_float_str)
print(f"String para float: {numero_float} (tipo: {type(numero_float)})")

# Convertendo float para inteiro
numero_float = 9.99
numero_int = int(numero_float)
print(f"Float para inteiro: {numero_int} (tipo: {type(numero_int)})")

# Convertendo inteiro para float
numero = 7
numero_float = float(numero)
print(f"Inteiro para float: {numero_float} (tipo: {type(numero_float)})")

# Convertendo lista para string
lista = [1, 2, 3]
lista_str = str(lista)
print(f"Lista para string: {lista_str} (tipo: {type(lista_str)})")

# Convertendo string para lista
string_lista = "[1, 2, 3]"
lista_convertida = eval(string_lista)
print(f"String para lista: {lista_convertida} (tipo: {type(lista_convertida)})")