# Importando um módulo padrão inteiro
import math  # O módulo math fornece funções matemáticas como sqrt, sin, cos, etc.

# Importando funções específicas de um módulo
from datetime import datetime  # datetime permite trabalhar com datas e horas

# Importando um módulo com um alias (apelido)
import numpy as np  # numpy é uma biblioteca para computação numérica, aqui usamos 'np' como apelido

# Importando várias funções específicas de um módulo
from os import path, mkdir  # path e mkdir são funções úteis para manipulação de arquivos e diretórios

# Importando tudo de um módulo (não recomendado, pode causar conflitos de nomes)
from random import *  # random fornece funções para geração de números aleatórios

# Calculando a raiz quadrada de um número usando o módulo math
numero = 16
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")