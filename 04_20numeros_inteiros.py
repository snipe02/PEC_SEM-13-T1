numeros = []
par = []
impar = []

for i in range(20):
  numeros.append(int(input()))

  if numeros[i] % 2 ==0:
    par.append(numeros[i])
  else:
    impar.append(numeros[i])

print(f'{numeros}\n{par}\n{impar}')