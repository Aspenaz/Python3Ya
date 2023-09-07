'''
Confeccionar un programa que solicite la carga de 10 valores 
reales por teclado. Mostrar al final su suma. Definir varias 
líneas de comentarios indicando el nombre del programa, el 
programador y la fecha de la última modificación. Utilizar 
el caracter # para los comentarios.
'''

suma = 0
for i in range(10):
    valor = float(input(f"Ingrese valor {i+1}: "))
    suma += valor

print(f"Suma: {suma}")

