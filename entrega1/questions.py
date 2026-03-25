import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
]
words2 = [
    "bucle",
    "cadena",
    "entero",
    "lista",
]
diccionario = {"categoria_1" : words,
                "categoria_2" : words2}



print("¡Bienvenido al Ahorcado!")
print()


print("CATEGORIAS: ")
for clave,valor in diccionario.items():
    print(clave, ":", valor)
cat = int(input("Elija una categoria: \n"))

if (cat == 1):
    categoria_elegida = words
else:
    categoria_elegida = words2

lista_mezclada = random.sample(categoria_elegida, len(categoria_elegida))




for word in lista_mezclada:

    guessed = []
    attempts = 6
    puntaje = 6

    while attempts > 0:

        progress = ""

        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            print(f"tu puntaje es: {puntaje} puntos")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if not letter.isalpha() or len(letter) != 1:
            print("entrada no valida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")

        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")

        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
            print(f"tu puntaje es: {puntaje} puntos")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        print(f"tu puntaje fue: {puntaje} puntos")