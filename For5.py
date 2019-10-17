#10 produtos e precos reajustados em 15%

def reajustar(lista):
    for item in lista:
        reajuste = item + item * 0.15
        print(reajuste)

produtos = [10, 20, 30, 40, 50, 60, 70 , 80, 90, 100]

reajustar(produtos)
