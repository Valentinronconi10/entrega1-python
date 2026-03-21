segundos = int(input("·Ingrese una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
