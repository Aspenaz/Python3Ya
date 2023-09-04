# Codificar un programa que lea n números enteros y calcule la 
# cantidad de valores mayores o iguales a 1000 (n se carga por teclado).

count = 0
n = int(input("Valores a ingresar: "))
for i in range(n):
    valor = int(input("Ingrese valor: "))
    if valor >= 1000:
        count += 1

print(f"Cantidad >= a 1000: {count}")