#funcao que recebe um n
#valor inteiro e dizer se é negtivo ou positivo

def PosiOuNeg(valor):
    if (valor > 0):
        print(valor, "eh positivo")
    elif(valor < 0):
        print(valor, "eh negativo")
    else: 
        print("Zero é nulo")

PosiOuNeg(10)
PosiOuNeg(20)
PosiOuNeg(-12)
PosiOuNeg(-6)
