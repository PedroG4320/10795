n = int(input("Número: "))
ops = 0
for i in range(1, n):
    _ = n + i
    _ = n - i
    _ = n * i
    _ = n / i
    ops += 4
print("Operações:", ops)