def quadro(numero: int | float) -> int | float:
    """
    Retorna o quadrado de um número.
    
    Args:
        numero (int ou float): O número a ser elevado ao quadrado.
    
    Returns:
        int ou float: O quadrado do número fornecido.
    """
    return numero ** 2

# Exemplo de uso
if __name__ == "__main__":
    num = 5
    print(f"O quadrado de {num} é {quadro(num)}")