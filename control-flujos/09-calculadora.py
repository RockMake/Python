nombre = input("cual es tu nombre: ")
print(f"Hola {nombre} bienvenido a la calculadora")

while True:
    print("""
    ___________ elija una operacion ________
    1. sumar
    2. restar
    3. multiplicar
    4. dividir
    0. salir """)
    op = input("opcion: ").lower()
    if op == "salir":
        break

    try:  # EL bloque try es el bloque con las sentencias que quieres ejecutar. Sin embargo, podrían llegar a haber errores de ejecución y el bloque se dejará de ejecutarse. El bloque except se ejecutará cuando el bloque try falle debido a un error.
        n = int(input("ingrese un numero "))
        n2 = int(input("ingrese otro numero "))
    except ValueError:
        print("elije una opcion valida")
        continue  # hace que un while se vuelva a ejecutar omitiendo el codigo de abajo

    if op == "sumar":
        resultado = n + n2
        print(f"""{n} Mas {n2}, el resultado es: {resultado}""")

    elif op == "restar":
        resultado = n - n2
        print(f"""{n} menos {n2}, el resultado es: {resultado}""")

    elif op == "multiplicar":
        resultado = n * n2
        print(f"""{n} por {n2}, el resultado es: {resultado}""")

    elif op == "dividir":
        try:
            resultado = n / n2
            print(f"""{n} entre {n2}, el resultado es: {resultado}""")
        except ZeroDivisionError:
            print("no se puede dividir entre 0")
    else:
        print("opcion incorrecta.")

    fin = input("desea realizar otra operacion? (s/n) ").lower()
    if fin == "n":
        break

print(f"chao {nombre}")
