estudiante = {}

try:
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
    for i in range(cantidad_estudiantes):
        nombre = str(input("Ingrese el nombre del estudiante: "))
        cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))
        for j in range(cantidad_estudiantes):
            notas = (f"Ingrese la nota {j+1}: ")
    estudiante[nombre] = {"notas":notas}
except ValueError:
    print("Error, debes de ingresar números validos")
except TypeError:
    print("Error, no puedes combinar el tipo de dato")
except Exception as es:
    print("Ha ocurrido un error")
else:
    for nombre, variable in estudiante.items():
        print(f"Nombre: {nombre}")
        print(f"Promedio: {variable['notas'].sum}")