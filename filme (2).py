def main():
  idade = int(input("Digite sua idade: "))
  
  if idade >= 18:
    print("Entrada liberada!")
  elif idade >= 16:
    acompanhante = input("Você está acompanhado de um adulto? (s/n): ")
    if acompanhante == "s" or acompanhante == "S":
      print("Entrada liberada!")
    else:
      print("Entrada não liberada.")
  else:
    print("Entrada não liberada.")

  return 0
main()    