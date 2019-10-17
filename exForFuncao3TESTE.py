#Cria uma func que recebe um texto 
#e retorne verdadeiro caso ele seja palindromo
# ou falso, caso n seja palindromo
#teste no fim
def ehpalindromo() :
    textoaocontrario = " "

    for letra in reversed(texto):
        textoaocontrario = textoaocontrario + letra
    
    if texto == textoaocontrario:
        return True
    else:
         return False
print(ehpalindromo("omo"))       
