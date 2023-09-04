# Realizar un programa que pida cargar una fecha cualquiera, luego 
# verificar si dicha fecha corresponde a Navidad.

dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))
if mes == 12 and dia == 25:
    print("la fecha ingresada corresponde a navidad...")