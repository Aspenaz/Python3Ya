# Desarrollar un programa que permita cargar n números enteros y 
# luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura 
# condicional (este operador retorna el resto de la división 
# de dos valores, por ejemplo 11%2 retorna un 1):

x = 1
countPares = 0
countImpares = 0

n = int(input("Ingrese cantidad de números enteros: "))

while x <= n:
    valor = int(input(f"Ingrese valor {x}: "))
    if valor%2 == 0:
        countPares += 1
    else: 
        countImpares += 1
    x += 1

print(f"Pares: {countPares}")
print(f"Impares: {countImpares}")