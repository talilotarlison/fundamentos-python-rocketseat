# Exemplo 1: Classe simples com atributos e métodos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Alice", 25)
print(pessoa1.apresentar())

# Exemplo 2: Herança em POO
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)  # Chama o construtor da classe base
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.cargo}."

# Criando um objeto da classe Funcionario
funcionario1 = Funcionario("Carlos", 30, "Engenheiro de Software")
print(funcionario1.apresentar())

# Exemplo 3: Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}"

# Criando um objeto da classe ContaBancaria
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(300)
print(conta.exibir_saldo())

# Exemplo 4: Polimorfismo
class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

# Criando objetos das classes derivadas
cachorro = Cachorro()
gato = Gato()
print(cachorro.emitir_som())
print(gato.emitir_som())
