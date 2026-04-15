count = 0
num = 2
while count < 10:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        print(num)
        count += 1
    num += 1