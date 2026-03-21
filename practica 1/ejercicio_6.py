
numeros_multi5 = []
numeros_nomulti = []
numero = int(input("Ingrese un número N: "))
for i in range(1,numero + 1):
    if i % 5 == 0:
        numeros_multi5.append(i)
    else:
        numeros_nomulti.append(i)

for i in range(len(numeros_multi5)):
    print(f'Los numeros multiplos de 5 son: {numeros_multi5[i]} ')


for i in range(len(numeros_nomulti)):
    print(f'Los numeros NO multiplos de 5 son: {numeros_nomulti[i]}' )