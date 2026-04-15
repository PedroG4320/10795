n = int(input("Número: "))
primo = True
if n < 2:
    primo = False
for i in range(2, n):
    if n % i == 0:
        primo = False
print("Primo" if primo else "Não primo")