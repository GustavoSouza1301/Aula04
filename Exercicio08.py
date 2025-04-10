soma = 0
quant = int(input("Digite quantidade de notas: "))
for x in range(quant):
    nota = float(input("Digite um número: "))
    soma += nota
media = soma / quant
print("A média é: ",media)
