# Desarrollar un programa que solicite la carga de 10 números e 
# imprima la suma de los últimos 5 valores ingresados.

suma = 0
for i in range(10):
    valor = float(input(f"Ingrese valor {i+1}: "))
    if i >= 5:
        suma += valor

print(f"Suma últimos 5: {suma}")