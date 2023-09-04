# En una empresa trabajan n empleados cuyos sueldos oscilan 
# entre $100 y $500, realizar un programa que lea los sueldos 
# que cobra cada empleado e informe cuántos empleados cobran 
# entre $100 y $300 y cuántos cobran más de $300. Además el 
# programa deberá informar el importe que gasta la empresa en 
# sueldos al personal.

x = 1
count1 = 0
count2 = 0
totalSueldo = 0

cantidadEmpleados = int(input("Ingrese cantidad de empleados: "))

while (x <= cantidadEmpleados):
    sueldo = float(input(f"Ingrese sueldo empleado {x}: "))
    totalSueldo += sueldo
    if (sueldo >= 100 and sueldo <= 300):
        count1 += 1
    else: 
        if sueldo > 300:
            count2 += 1

    x += 1

print(f"Empleados que cobran entre 100 y 300: {count1}")
print(f"Empleados que cobran más de 300: {count2}")
print(f"Total sueldos: {totalSueldo}")