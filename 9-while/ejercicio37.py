# Realizar un programa que permita cargar dos listas de 15 valores 
# cada una. Informar con un mensaje cual de las dos listas tiene un 
# valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", 
#"Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.


acumulado1 = 0
acumulado2 = 0

x = 1
print("Lista 1\n")
while x <= 5:
    valor = int(input(f"Ingrese valor {x}: "))
    acumulado1 += valor
    x += 1

print()

x = 1
print("Lista 2\n")
while x <= 5:
    valor = int(input(f"Ingrese valor {x}: "))
    acumulado2 += valor
    x += 1

print(f"Acumulado 1: {acumulado1}")
print(f"Acumulado 2: {acumulado2}")

if acumulado1 > acumulado2:
    print(f"Lista 1 es mayor: {acumulado1} ")
else:
    if acumulado1 < acumulado2:
        print(f"Lista 2 es mayor: {acumulado2}")
    else:
        print("Listas iguales")
