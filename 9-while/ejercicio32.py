# Escribir un programa que solicite ingresar 10 notas de alumnos 
# y nos informe cuántos tienen notas mayores o iguales a 7 y 
#  cuántos menores.

x = 1
count1 = 0
count2 = 0
while (x <= 10):
    nota = float(input(f"Ingrese nota {x}: "))

    if nota >= 7:
        count1 += 1
    else:
        count2 += 1

    x += 1

print(f"Cantidad >= 7: {count1}")
print(f"Cantidad < 7: {count2}")