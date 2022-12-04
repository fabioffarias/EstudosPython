from math import sqrt, floor

num = int(input("Digite um número: "))

raiz = sqrt(num)

print(f"A raiz de {num} é {raiz:2f}")

print(f"A raiz de {num} é {floor(raiz)}")