#recebe idade do nadador e exibe a categoria
# desse nadador de acordo com a tabela
# consertar o < e >=

def CategoriaDoNad(idade):
    if (idade => 5 and idade <=7):
        print("infantil A")
    elif (idade => 8 and idade <= 10):
        print("Infantil B")
    elif (idade =>11 and idade <= 13):
        print("Juvenil A")
    elif (idade =>14 and idade <= 17):
        print("Juvenil B")
    elif (idade => 18):
        print("Adulto")
    else:
        print("Valor invalido")
IdadeDoNadador = input("Qual a idade? ")
CategoriaDoNad(IdadeDoNadador)                    

