# Escribir un programa que solicite por teclado 10 notas de 
# alumnos y nos informe cuántos tienen notas mayores o iguales 
# a 7 y cuántos menores.

count1 = 0
count2 = 0

for i in range(10):
    nota = float(input(f"Ingrese nota {i+1}: "))
    if nota >= 7:
        count1 += 1
    else: 
        count2 += 1

print(f"Notas >= 7: {count1} ")
print(f"Notas < 7: {count2}")