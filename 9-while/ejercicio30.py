# Desarrollar un programa que permita la carga de 10 valores 
# por teclado y nos muestre posteriormente la suma de los 
# valores ingresados y su promedio.

x = 1 
suma = 0 
promedio = 0

while(x<=10):
    valor = int(input(f"Ingrese valor {x}: "))
    suma += valor
    x += 1
promedio = suma/(x-1)
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")