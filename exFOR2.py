#Faca um prog que le os primeiros numeros inteiros
#e ao final mostre qual foi o maior e menor numero lido
import math

menor = math.inf
maior =  - math.inf
print("Numeros inteiros:")

for i in range(10):
    numero = (int) (input("digite um numero: "))

    if (numero> maior):
        maior = numero
    if (numero < menor):
        menor = numero
print("O maior valor  eh: ", maior) 
print("O menor valor  eh: ", menor)            
    
       
