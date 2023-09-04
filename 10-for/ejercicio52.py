# Escribir un programa que pida ingresar coordenadas (x,y) que 
# representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, 
# tercer y cuarto cuadrante. Al comenzar el programa se pide que 
# se ingrese la cantidad de puntos a procesar.

countCuadrante1 = 0
countCuadrante2 = 0
countCuadrante3 = 0
countCuadrante4 = 0

n = int(input("Ingrese cantidad de puntos a procesar: "))

for i in range(n):
    x = int(input("\nIngrese x: "))
    y = int(input("Ingrese y: "))


    if x == 0 and y == 0:
        print("X y Y pertenecen al centro de coordenadas")
    else:
        if x > 0 and y > 0:
            countCuadrante1 += 1
        else: 
            if x < 0 and y > 0:
                countCuadrante2 += 1
            else:
                if x < 0 and y < 0:
                    countCuadrante3 += 1
                else:
                    countCuadrante4 += 1

print()
print(f"1° Cuadrante: {countCuadrante1}")
print(f"2° Cuandrante: {countCuadrante2}")
print(f"3° Cuadrante: {countCuadrante3}")
print(f"4° Cuadrante {countCuadrante4}")