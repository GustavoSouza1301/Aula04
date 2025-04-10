neg = 0
for valor in range(1,11):
    num = int(input("Digite um número: "))
    if num <0:
        neg += 1
print("A quantidade de números negativos são: ",neg)
