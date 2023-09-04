# Escribir un programa que pida ingresar la coordenada de un punto 
# en el plano, es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

print("Coordenada de un punto \n")

x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))

if x == 0 and y == 0:
    print("X y Y pertenecen al centro de coordenadas")
else:
    if x > 0 and y > 0:
        print("1° Cuadrante")
    else: 
        if x < 0 and y > 0:
            print("2° Cuadrante")
        else:
            if x < 0 and y < 0:
                print("3° Cuadrante")
            else:
                print("4° Cuadrante")