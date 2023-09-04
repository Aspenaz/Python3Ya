# Mostrar los múltiplos de 8 hasta el valor 500. 
# Debe aparecer en pantalla 8 - 16 - 24, etc.

x = 1
while(x <= 100):
    if(x % 8 == 0):
        print(x)
    x += 1

print()

x = 8
while x <= 100:
    print(x)
    x += 8
          