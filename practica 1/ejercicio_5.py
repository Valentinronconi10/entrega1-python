total = 0
while True:
    precio = float(input("Ingrese el precio del producto : "))
    if precio == 0:
        break
    total  += precio

print(f"El precio total acumulado es : {total}")
