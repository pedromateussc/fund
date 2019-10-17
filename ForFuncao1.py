#escreva uma func q receba uma lista de inteiros
# de 16 posicoes e que retorne a soma dos quadrados
#dos numeros impares contidos na lista
#teste

def somadosQ(inteiros):
    total = 0
    for valor in inteiros:
        if (valor % 2 != 0):
            total = total + valor**2
    return total

numero = [10, 20, 30, 40]
numero2 = [3, 4, 7]
numero3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]

total1 =somadosQ(numero)
total2 =somadosQ(numero2)
print(somadosQ(numero3))

print(total1)
print(total2) 

       





numeros = [1, 2, 3, 4 ,5 ,6 , 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  
