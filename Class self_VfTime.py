class pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf= cpf
        self.email = email

p1 = pessoa("Pedro", "12345", "pedro@gmail.com")
p2 = pessoa("Joao", "123456", "joao@gmail.com")

print(p1.nome, p1.cpf, p1.email)

