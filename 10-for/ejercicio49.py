# Desarrollar un programa que muestre la tabla de 
# multiplicar del 5 (del 5 al 50)

x = 1
for i in range(5, 51, 5):
    print(f"{x} * 5 = {i}")
    x += 1
