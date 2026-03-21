lista_palabras = []
oracion = ""

while True:
    palabra = input("Ingrese una palabra (0 para terminar): ")

    if palabra == "0":
        break

    lista_palabras.append(palabra)

for elem in lista_palabras:
    if len(elem) > 3:
        oracion += elem + " "

print("La oración formada es:")
print(oracion)

        

