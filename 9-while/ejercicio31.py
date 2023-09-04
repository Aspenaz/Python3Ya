# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad 
# de piezas a procesar y luego ingrese la longitud de cada perfil; 
# sabiendo que la pieza cuya longitud esté comprendida en el rango 
# de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de 
# piezas aptas que hay en el lote.

x = 1
count = 0
cantidadDePiezas = int(input("Ingrese cantidad de piezas: "))
print()

while(x <= cantidadDePiezas):
    longitudDePerfil = float (input(f"Ingrese longitud de perfil {x}: "))
    if longitudDePerfil >= 1.20 and longitudDePerfil <= 1.30:
        count += 1
    x += 1

print(f"Cantidad: {count}")