#Utilizando o laco for, calcule e imprima
# a soma dos nums impares entre 1 e 100

print("Soma de impares: ")
soma = 0
total = 0

for i in range(100):
    if (i%2 != 0):
        total = total + 1 #total de operacoes feitas
        soma = soma + i
print(soma)
print(total)        
