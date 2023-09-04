# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.


countNegativo = 0
countPositivo = 0
countMultiplo15 = 0
acumuladoPares = 0

for i in range(10):
    valor = int(input(f"Ingrese valor {i+1}: "))

    if valor < 0:
        countNegativo += 1
    else: 
        if valor > 0:
            countPositivo += 1
    
    if valor%15 == 0:
        countMultiplo15 += 1

    if valor%2 == 0:
        acumuladoPares += valor

print(f"Negativos: {countNegativo}")
print(f"Positivos: {countPositivo}")
print(f"Múltiplos de 15: {countMultiplo15}")
print(f"Acumulado Pares: {acumuladoPares}")
