estudiante = {}
while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
        break
    except ValueError:
        print("Valor invalido, vuelva a intentar")
    except Exception as e:
        print("Ha ocurrido un error, vuelva a intentar")

for i in range(cantidad_estudiantes):
    while True:
        try:
            nombre = str(input("Ingrese el nombre del estudiante: "))
            if not nombre.strip():
                raise ValueError("El campo no puede estar vacio")
            cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))
            if cantidad_notas < 0:
                print("La cantidad de notas no puede ser negativa")
            else:
                estudiante[nombre] = {}
                break
        except TypeError:
            print("Valor invalido, vuelva a intentar")
        except ValueError:
            print("Valor invalido, vuelva a intentar")
        except Exception:
            print("Ha ocurrido un error, vuelva a intentar")
        else:
            break
    for j in range(cantidad_notas):
        while True:
            try:
                notas = int(input(f"Ingrese la nota: "))
                if notas < 0 and notas > 100:
                    print("Error. La nota debe ser entre 0 a 100")
                else:
                    estudiante[nombre][f'notas{j+1}'] = notas
                    break
            except ValueError:
                print("Valor invalido, vuelva a intentar")
            except Exception as e:
                print("Ha ocurrido un error, vuelva a intentar")

    suma = 0
    cantidad = 0
    for clave, valor in estudiante[nombre].items():
        if clave.startswith('notas'):
            suma += valor
            cantidad += 1
        if cantidad > 0:
            promedio = suma / cantidad
    print(f"El promedio es del estudiante es de: {promedio}")

