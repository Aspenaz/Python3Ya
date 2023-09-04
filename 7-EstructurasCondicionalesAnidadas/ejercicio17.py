# Confeccionar un programa que permita cargar un número entero positivo 
# de hasta tres cifras y muestre un mensaje indicando si 
# tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si 
# el número de cifras es mayor.

num = int(input("Ingrese valor (hasta 3 dígitos, positivo): "))

if num < 10: 
    print("Tiene 1 dígito")
else:
    if num < 100:
        print("Tiene 2 dígitos")
    else: 
        if num < 1000:
            print("Tiene 3 dígitos")
        else:
            print("Error en la entrada de datos")