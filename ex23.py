try:
    # Solicita a entrada de dados do usuário
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    # Trata o erro caso o usuário não digite um número inteiro
    print("Erro: Você deve digitar um número inteiro válido.")

    try:
        # Tenta abrir um arquivo que não existe
        with open("arquivo_inexistente.txt", "r") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        # Trata o erro caso o arquivo não seja encontrado
        print("Erro: O arquivo especificado não foi encontrado.")

try:
    # Tenta dividir por zero
    resultado = 10 / 0
except ZeroDivisionError:
    # Trata o erro de divisão por zero
    print("Erro: Não é possível dividir um número por zero.")

try:
    # Tenta acessar um índice inexistente em uma lista
    lista = [1, 2, 3]
    elemento = lista[5]
except IndexError:
    # Trata o erro de índice fora do intervalo
    print("Erro: O índice especificado está fora do intervalo da lista.")