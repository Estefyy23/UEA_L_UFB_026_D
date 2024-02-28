# Inicio de programa

import random

# Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
# En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana
# (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.

ciudad =['Latacunga', 'Quito', 'Ambato']

Diasdelasemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

Semanas = ['Semana1', 'Semana2', 'Semana3']

# Almacenamiento de matriz de temperaturas

temperaturasdiarias = [[[random.randint(0,45)for _ in Diasdelasemana]for _ in Semanas] for _ in ciudad]

# vamos a calcular el promedio por ciudades y semanas y

for ciudad, tems_ciudad in zip(ciudad,  temperaturasdiarias):
    print(f"Promedio de temperaturas para {ciudad}:")
    for Semana, temperaturaSemana in zip( Semanas, tems_ciudad):
        promedio = sum(temperaturadia for temperaturadia in temperaturaSemana) / len (temperaturaSemana)
        print (f"{Semana}: {promedio:.2f} grados celsius")
    print()















