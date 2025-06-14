import random
def main() :
    notas = [0.0] * 4
    print(notas)

    i = 0
    media = 0
    while i < 4:
        notas[i] = random.uniform(0.0, 10.0)
        media += notas[i]
        i = i + 1
    media /= 4
    print(f"A priumeira nota é: {notas[0]:,.2} \nA segunda nota é: {notas[1]:,.2}")
    print(f"A terceira nota é: {notas[2]:,.2} \nE a quarta nota é: {notas[3]:,.2}")
    print(f"E a média é: {media:,.2}")

    if media >= 6.0:
        print("Aprovado")
    elif media >= 4.0:
        print("Recuperação")
    else:
        print("Reprovado")

    return 0
main()