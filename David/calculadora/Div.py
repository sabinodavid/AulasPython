from  VerificarZero import VerificarZero
def div(num1, num2):
    if VerificarZero(num2):
        div= "Divisão por zero é impossível"
    else:
        div = num1/num2
    return div