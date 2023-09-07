"""
Mostrar la tabla de 5 con las estructuras repetitivas:
  while
  y
  for
"""

# utilizando el while
print("Tabla del 5 empleando while")
x = 5 
while x <= 50:
    print(x)
    x += 5

print()

# utilizando el for
print("Tabla del 5 empleando el for")
for x in range(5, 51, 5): 
    print(x)