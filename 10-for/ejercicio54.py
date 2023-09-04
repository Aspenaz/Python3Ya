# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios).
# b) Imprimir dichos promedios (promedio de cada turno).
# c) Mostrar por pantalla un mensaje que indique cual de los tres 
#    turnos tiene un promedio de edades mayor.


sumaEdadMañana = 0
sumaEdadTarde = 0
sumaEdadNoche = 0

print("Turno mañana")
for i in range(5): 
    edadMañana = int(input(f"Ingrese edad {i+1}: "))
    sumaEdadMañana += edadMañana

print("Turno tarde")
for i in range(6): 
    edadTarde = int(input(f"Ingrese edad {i+1}: "))
    sumaEdadTarde += edadTarde

print("Turno noche")
for i in range(11): 
    edadNoche = int(input(f"Ingrese edad {i+1}: "))
    sumaEdadNoche += edadNoche

promedioMañana = sumaEdadMañana/5
promedioTarde = sumaEdadTarde/6
promedioNoche = sumaEdadNoche/11

print(f"Promedio edades Mañana: {promedioMañana}")
print(f"Promedio edades Tarde: {promedioTarde}")
print(f"Promedio edades Noche: {promedioNoche}")

if promedioMañana > promedioTarde and promedioMañana > promedioNoche: 
    print(f"\nTurno mañana tiene mayor promedio ")
else:
    if promedioTarde > promedioNoche:
        print ("\nTurno tarde tiene mayor promedio")
    else: 
        print("\nTurno noche tiene mayor promedio")