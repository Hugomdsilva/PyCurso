class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self._nome = novo_nome
        else:
            print("Nome inválido")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Idade inválida")

pessoa = Pessoa("João", 30)
print(pessoa.nome) # João
print(pessoa.idade) # 30

pessoa.nome = "Maria"
pessoa.idade = 25
print(pessoa.nome) # Maria
print(pessoa.idade) # 25

pessoa.nome = ""
pessoa.idade = -1
# Nome inválido
# Idade inválida