#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 

# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


# Problema:
# Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
# Si el promedio es >=7 mostrar "Promocionado".
# Si el promedio es >=4 y <7 mostrar "Regular".
# Si el promedio es <4 mostrar "Reprobado".

nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 7:
    print("Promocionado")
else: 
    if promedio >= 4:
        print("Regular")
    else:
        print("Reprobado")


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================
