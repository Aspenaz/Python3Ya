# Escribir un programa en el cual: dada una lista de tres valores numéricos 
# distintos se calcule e informe su rango de variación (debe mostrar el 
# mayor y el menor de ellos).

print("\nRango de valores\n")

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
num3 = int(input("Ingrese tercer valor: "))

if num1<num2 and num1<num3:
    print(num1)
else: 
    if num2<num3:
        print(num2)
    else:
        print(num3)



if num1>num2 and num1>num3:
    print(num1)
else: 
    if num2>num3:
        print(num2)
    else:
        print(num3)