L = []
soma = 0
multiplicacao = 1

for i in range(10):
    L.append(int(input()))
    soma += L[i]
    multiplicacao *= L[i]

print(f'{L}\n{soma}\n{multiplicacao}')