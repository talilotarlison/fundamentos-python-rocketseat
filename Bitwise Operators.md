### Bitwise Operators (Operadores Bit a Bit)

Bitwise operators são operadores que realizam operações diretamente nos **bits individuais** dos operandos. Em linguagens como C, Java, Python, PHP etc., eles são amplamente usados em manipulações de baixo nível, como controle de hardware, criptografia, compressão de dados, etc.

Abaixo está uma visão geral dos **principais operadores bit a bit**:

---

### 📋 **Tabela de Operadores Bit a Bit:**

| Operador | Nome                    | Descrição                                                 | Exemplo (`a = 5, b = 3`)                           | Resultado                                |         |       |           |
| -------- | ----------------------- | --------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------- | ------- | ----- | --------- |
| `&`      | AND bit a bit           | Compara os bits e retorna 1 se ambos forem 1              | `5 & 3` → `101 & 011`                              | `001` = 1                                |         |       |           |
| \`       | \`                      | OR bit a bit                                              | Compara os bits e retorna 1 se pelo menos um for 1 | \`5                                      | 3`→`101 | 011\` | `111` = 7 |
| `^`      | XOR bit a bit           | Compara os bits e retorna 1 se os bits forem diferentes   | `5 ^ 3` → `101 ^ 011`                              | `110` = 6                                |         |       |           |
| `~`      | NOT bit a bit           | Inverte todos os bits (complemento de 1)                  | `~5` → `~00000101`                                 | `11111010` = -6 (em complemento de dois) |         |       |           |
| `<<`     | Deslocamento à esquerda | Desloca todos os bits para a esquerda (multiplica por 2ⁿ) | `5 << 1` → `1010`                                  | `10`                                     |         |       |           |
| `>>`     | Deslocamento à direita  | Desloca todos os bits para a direita (divide por 2ⁿ)      | `5 >> 1` → `10`                                    | `2`                                      |         |       |           |

---

### 🔍 **Exemplo em Python:**

```python
a = 5      # 101
b = 3      # 011

print("a & b =", a & b)   # 1
print("a | b =", a | b)   # 7
print("a ^ b =", a ^ b)   # 6
print("~a =", ~a)         # -6
print("a << 1 =", a << 1) # 10
print("a >> 1 =", a >> 1) # 2
```

---

### **Curiosidade:**

Bitwise operations são extremamente rápidos, pois operam diretamente no nível de hardware. São muito utilizados em:

* Criptografia
* Compactação de dados
* Manipulação de bandeiras (flags)
* Sistemas embarcados

---

Se quiser exemplos práticos em uma linguagem específica (como C, Python, Java, etc.), posso mostrar também! Deseja ver isso em alguma linguagem?
