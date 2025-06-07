def main():
  print("Lista da chamada")
  i = int(input(" digite a quantidade de alunos: "))
  vet = [""] * i
  j = 0

  for i in vet :
    vet[j] = input("Digite o nome do aluno: ")
    j = j + 1
    nome = "David Sabino"

  print("As 5 primeiras letras do seu nome são:", nome[0:5])
  print ("Alunos que vieram hoje \n", vet)
  return 0
main()    