rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            },
            'Camila': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Santiago': {
                'judge_1': 6,
                'judge_2': 7,
                'judge_3': 6
            },
            'Lucía': {
                'judge_1': 8,
                'judge_2': 8,
                'judge_3': 8
            }
        }
    },

    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Mateo': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Camila': {
                'judge_1': 7,
                'judge_2': 6,
                'judge_3': 7
            },
            'Santiago': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 8
            },
            'Lucía': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            }
        }
    },

    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            },
            'Mateo': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Camila': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Santiago': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 6
            },
            'Lucía': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 9
            }
        }
    },

    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 7,
                'judge_2': 6,
                'judge_3': 7
            },
            'Camila': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 8
            },
            'Santiago': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 7
            },
            'Lucía': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 8
            }
        }
    },

    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 8
            },
            'Camila': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 7
            },
            'Santiago': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 9
            },
            'Lucía': {
                'judge_1': 8,
                'judge_2': 8,
                'judge_3': 7
            }
        }
    }
]

tabla_posiciones = {}
totales = {}
cantidad_ganadas = 0
for ronda in rounds:
    print("\nRonda:", ronda["theme"])
    ganador = ""
    mejor_puntaje = 0
    for persona, datos in ronda["scores"].items():
        total = datos["judge_1"] + datos["judge_2"] + datos["judge_3"]

        if (total > mejor_puntaje):
            mejor_puntaje = total
            ganador = persona


    print(f"El ganador de esta ronda es: {persona}, con un puntaje de: {mejor_puntaje} puntos")

        
