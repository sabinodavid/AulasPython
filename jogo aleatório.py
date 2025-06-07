import random

def main():
  print("Bem-vindo ao jogo de adivinhação!")
  numAleatório = random.randint(1, 200)

  tentativas = 0
  numDigitado = 0

  while numDigitado != numAleatório:
    numDigitado = int(input("Digite um número: "))

    if numDigitado == numAleatório:
        print("Você acertou!")
        break
    elif numDigitado < numAleatório:
        print("O número digitado é menor que o número aleatório\n")
    else :
        print("O número digitado é maior que o número aleatório\n")
    tentativas += 1
  print("Você acertou o número em", tentativas, "tentativas!")
  return 0
main()    