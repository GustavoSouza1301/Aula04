fora = 0
for x in range(10):
    num = int(input("Digite um número: "))
    if num <10 or num >20:
        fora += 1
dentro = 10 - fora
print(f"Quantidade de valor dentro do intervalo: {dentro}\nQuantidade fora: {fora}")