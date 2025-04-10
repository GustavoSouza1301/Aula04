num = int(input("Digite um número: "))
if num <= 0:
    print("Número inválido")
else:
    for N in range(1, num + 1, 1):
        print(N, end= " ")