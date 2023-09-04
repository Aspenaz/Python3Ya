# Desarrollar un programa que permita la carga de 10 valores por 
# teclado y nos muestre posteriormente la suma de los valores 
# ingresados y su promedio. Este problema ya lo desarrollamos, 
# lo resolveremos empleando la estructura for para repetir la 
# carga de los diez valores por teclado.

suma = 0

for f in range(10):
    valor = int(input(f"Ingrese valor {f+1}: "))
    suma += valor
promedio = suma/10
print(f"Total: {suma}")
print(f"Promedio: {promedio}")
