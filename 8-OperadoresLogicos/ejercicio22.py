# Se ingresan por teclado tres números, si todos los valores ingresados 
# son menores a 10, imprimir en pantalla la leyenda 
# "Todos los números son menores a diez".

uno = int(input("Ingrese primer valor: "))
dos = int(input("Ingrese segundo valor: "))
tres = int(input("Ingrese trecer valor: "))

if uno < 10 and dos < 10 and tres < 10:
    print("Todos los números son menores a diez")