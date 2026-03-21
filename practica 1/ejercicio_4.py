numero = int(input("Ingrese un número N: "))
for i in range(1,numero + 1):
    if i % 5 == 0:
        continue
    print(f"Numero : {i}")
