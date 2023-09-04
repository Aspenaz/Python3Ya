# Realizar un programa que lea los lados de n triángulos, 
# e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: 
#    equilátero (tres lados iguales), isósceles (dos lados iguales), 
#    o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

countEquilatero = 0
countIsosceles = 0
countEscaleno = 0

n = int(input("Cantidad de triángulos: "))
print()

for i in range(n):
    l1 = int(input(f"Ingrese lado a: "))
    l2 = int(input(f"Ingrese lado b: "))
    l3 = int(input(f"Ingrese lado c: "))

    if l1 == l2 and l1 == l3:
        print("Triángulo equilátero\n")
        countEquilatero += 1
    else: 
        if l1 == l2 or l1 == l3 or l2 == l3:
            print("Triángulo isósceles\n")
            countIsosceles += 1
        else:
            print("Triángulo escaleno\n")
            countEscaleno += 1

print(f"Equiláteros: {countEquilatero}")
print(f"Isósceles: {countIsosceles}")
print(f"Escalenos: {countEscaleno}")



