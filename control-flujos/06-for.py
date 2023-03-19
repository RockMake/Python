# for numero in range(5):
#     print(numero, numero * "hola mundo")

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # detiene una ejecucion del codigo
else:
    print("no se encontro el numero")


for char in "ultimate python":
    print(char)
