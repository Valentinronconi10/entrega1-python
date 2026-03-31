playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

duracion_total = 0

sumaMinutos = 0
sumaSegundos = 0
max = -1
min = 99999
for i in range(len(playlist)):
    minutos,segundos = (playlist[i]["duration"].split(":"))
    minutos = int(minutos)
    segundos = int(segundos)
    sumaMinutos += minutos
    sumaSegundos += segundos
    if (minutos > max):
        max = minutos
        max_segundos = segundos
        cancion_max = playlist[i]["title"]
    else:
        if (minutos < min):
            min = minutos
            min_segundos = segundos
            cancion_min = playlist[i]["title"]

minutos_extra = sumaSegundos // 60
sumaMinutos += minutos_extra
sumaSegundos = sumaSegundos % 60
print(f"Minutos: {sumaMinutos}")
print(f"Segundos: {sumaSegundos}")
print(f"La cancion mas larga es: '{cancion_max}' - {max} : {max_segundos:02d}")
print(f"La cancion mas corta es: '{cancion_min}' - {min} : {min_segundos:02d} ")
 