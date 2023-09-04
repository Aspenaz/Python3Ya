# Confeccionar un programa que lea n pares de datos, cada par de 
# datos corresponde a la medida de la base y la altura de un triángulo.
# El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

count = 0
n = int(input("Ingrese cantidad: "))
for i in range(n):
    base = int(input(f"\nIngrese base {i+1}: "))
    altura = int(input(f"Ingrese altura {i+1}: "))

    superficie = (base*altura)/2
    print(f"Superficie: {superficie}")

    if superficie > 12:
        count += 1

print(f"\nSuperficies mayores a 12: {count}")
