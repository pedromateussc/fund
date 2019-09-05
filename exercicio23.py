print("=== Preco do produto ===")

preco = (float)(input("Qual o preco do produto? "))
opcao = (int)(input("Qual opcao deseja usar? "))

if  opcao == 1:
    total = preco - (preco*10/100)
    print("O valor a vista eh", total, "reais.")
elif opcao == 2:
    total = preco - (preco*5/100)
    print("O valor no cartao com 5% de desconto eh", total, "reais.")
elif opcao == 3:
    total = preco/2
    print("2x parcelas sem juros, no valor de", total, "reais cada.")
elif opcao == 4:
    total =  (preco/3) + (preco*10/100)
    print("3x parcelas, com o valor de", total, "reais cada")       
else:
    print("Opcao invalida, tente novamente")       

