review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""


spoilers = input("Ingrese las palabras spoiler (separadas por coma): ")

lista_spoilers = spoilers.split(",")


for i in range(len(lista_spoilers)):
    lista_spoilers[i] = lista_spoilers[i].strip().lower()



texto_resultado = review
for palabra in lista_spoilers:
    reemplazo = "*" * len(palabra)

    texto_resultado = texto_resultado.replace(palabra,reemplazo)
    texto_resultado = texto_resultado.replace(palabra.capitalize(), reemplazo)
    texto_resultado = texto_resultado.replace(palabra.upper(), reemplazo)
print(texto_resultado)