# Se ingresan tres valores por teclado, si todos son iguales se imprime 
# la suma del primero con el segundo y a este resultado se lo multiplica 
# por el tercero.

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
num3 = int(input("Ingrese trecer valor: "))

if num1 == num2 == num3: 
    suma = num1 + num2 
    multi = suma * num3 
    print(f"Suma: {suma}")
    print(f"Multiplicación: {multi}")