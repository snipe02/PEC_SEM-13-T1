A = []
B = []
C = []

for c in range(25):
    A.append(int(input()))

for i in range(25):
    B.append(int(input()))

for p in range(25):
    C.append(A[p])
    C.append(B[p])

print(f'{A}\n{B}\n{C}')