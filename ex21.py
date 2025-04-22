# Função simples que soma dois números
def soma(a, b):
    return a + b

# Função que verifica se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função que calcula o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Função que retorna uma saudação personalizada
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"


    # Função que imprime uma mensagem sem retornar nada
def mensagem_sem_retorno():
    print("Esta é uma função sem retorno.")

# Testando as funções
if __name__ == "__main__":
    print(soma(3, 5))  # Saída: 8
    print(eh_par(4))   # Saída: True
    print(fatorial(5)) # Saída: 120
    print(saudacao("Talil")) # Saída: Olá, Talil! Seja bem-vindo(a)!