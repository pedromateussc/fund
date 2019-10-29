#prog q le 20 n inteiros e os armazena em um vetor de 20 posi
#funcao que recebe o valor lido e q calcula e retorna a media dos
#elementos do vetorr

def MedDaLista(lista):
    total = 0
    for i in lista:
        total = total + i
    total = total/20
    return total    

numeros = []

for i in range(0,20):
    numero = (int)(input("Dig um numero: "))
    numeros.append(numero)

print("Media dos valores eh", MedDaLista(numeros))    
