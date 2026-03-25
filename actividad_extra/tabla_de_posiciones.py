menu = {1 : "Agregar Equipo", 2 : "Registrar Resultado", 3: "Mostrar Tabla", 
        4 : "Eliminar Equipo", 5: "Salir"}

tabla_posiciones = {}
while True:
    for clave,valor in menu.items():
        print(clave, ":", valor )
    opcion = int(input("Elija una opcion: "))

    if (opcion == 1):
        nombre_equipo = str(input("Ingrese el nombre del equipo: "))
        while (nombre_equipo in tabla_posiciones):
            print("Equipo ya existente, agregue otro equipo!")
            nombre_equipo = str(input("Ingrese el nombre del equipo: "))
        tabla_posiciones[nombre_equipo] = {"pj" : 0, "puntos" : 0}

    elif (opcion == 2):
        local = str(input("Ingrese el equipo local: "))
        visitante = str(input("Ingrese el equipo visitante: "))

        while (local not in tabla_posiciones):
            print("El equipo local no existe")
            local = str(input("Ingrese el equipo local: "))
            
        while visitante not in tabla_posiciones or visitante == local:
            print("El equipo visitante no existe o es el mismo equipo.")
            visitante = str(input("Ingrese el equipo visitante: "))

        resultado = input("Marcador  (ej: 4 - 2): ")
        if "-" not in resultado:
            print("Formato incorrecto")
        else:
            goles_local, goles_visitante = resultado.split("-")
            goles_local = int(goles_local.strip())
            goles_visitante = int(goles_visitante.strip())

            tabla_posiciones[local]["pj"] += 1
            tabla_posiciones[visitante]["pj"] += 1

            if (goles_local > goles_visitante):
                tabla_posiciones[local]["puntos"] += 3
            elif (goles_visitante > goles_local):
                tabla_posiciones[visitante]["puntos"] += 3
            else:
                tabla_posiciones[local]["puntos"] += 1
                tabla_posiciones[visitante]["puntos"] += 1

    elif (opcion == 3):
        for equipo, datos in tabla_posiciones.items():
            print(equipo, "- PJ:", datos["pj"], "- Puntos:", datos["puntos"])

    elif (opcion == 4):
        eliminar = str(input("Equipo a eliminar: "))
        while (eliminar not in tabla_posiciones):
            print("El equipo ingresado no se encuentra en la tabla ")
            eliminar = str(input("Equipo a eliminar: "))
        tabla_posiciones.pop(eliminar, None)

    else:
        print("Programa finalizado")
        break
