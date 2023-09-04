# Escribir un programa que lea 10 números enteros y luego muestre 
# cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. 
# Debemos tener en cuenta que hay números que son múltiplos 
# de 3 y de 5 a la vez.

multiplo3 = 0
multiplo5 = 0
multiplo3y5 = 0
for i in range(10):
    numero = int(input(F"Ingrese valor entero {i+1}: "))
    if numero%3 == 0:
        multiplo3 += 1
    if numero%5 == 0:
        multiplo5 += 1
    if numero%3 == 0 and numero%5 == 0:
        multiplo3y5 += 1

print(f"Multiplos de 3: {multiplo3}")
print(f"Multiplos de 5: {multiplo5}")
print(f"Multiplos de 3 y 5: {multiplo3y5}")