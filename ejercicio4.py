#4)	 Elabore un programa para un Hospital que determine, y muestre el nivel de Leucemia de 803 pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia; si esta entre 11 y 40, nivel bajo de Leucemia; si esta entre 40 y 69, nivel moderado de Leucemia, si esta entre 70 y 100, nivel grave de Leucemia.

import random

for i in range(803):
    puntaje = random.randint(1, 100)
    if puntaje < 10:
        print(f"El paciente {i+1} ,tiene un puntaje de {puntaje}, lo que significa que no tiene Leucemia")
    elif puntaje >= 11 and puntaje <= 40:
        print(f"El paciente {i+1} tiene un puntaje de {puntaje}, lo que significa que tiene un nivel bajo de Leucemia")
    elif puntaje >= 41 and puntaje <= 69:
        print(f"El paciente {i+1} tiene un puntaje de {puntaje}, lo que significa que tiene un nivel moderado de Leucemia")
    else:
        print(f"El paciente {i+1} tiene un puntaje de {puntaje}, lo que significa que tiene un nivel grave de Leucemia")

