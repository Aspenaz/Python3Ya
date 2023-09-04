# Se cargan por teclado tres números distintos. 
# Mostrar por pantalla el mayor de ellos.

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
num3 = int(input("Ingrese tercer valor: "))

if num1 > num2: 
    if num1 > num3: 
        print("Mayor: " + str(num1))
    else:
        print(num3)
else:
    if num2 > num3:
        print("mayor: " + str(num2))
    else:
        print("Mayor: " + str(num3))