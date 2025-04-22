# Example of a standard while loop
counter = 0
while counter < 5:
    print(f"While loop: Counter is {counter}")
    counter += 1

# Example of a simulated do-while loop
counter = 0
while True:
    print(f"Do-while loop: Counter is {counter}")
    counter += 1
    if counter >= 5:
        break

# Em Python, não existe uma estrutura nativa de do-while como em outras linguagens, mas você pode simular o comportamento de um do-while 
# usando um while True com uma condição de saída (break), como já está no seu código.

# Simulação de um do-while loop
counter = 0
while True:
    print(f"Do-while loop: Counter is {counter}")
    counter += 1
    if counter >= 5:  # Condição de saída
        break