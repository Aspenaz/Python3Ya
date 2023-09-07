"""
Realizar un programa que solicite la carga de valores enteros 
por teclado y los sume. Finalizar la carga al ingresar el 
valor -1. Dejar como comentario dentro del código fuente 
el enunciado del problema.
"""

suma = 0
valor = int(input("Ingrese valor(-1 finaliza): "))
while(valor != -1):
    suma += valor 
    valor = int(input("Ingrese valor(-1 finaliza): "))

print(f"Total: {suma}")
