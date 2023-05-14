beatles = []
print("Paso 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("JGeorge Harrison")

print("Paso 2:", beatles)

n = int(input("cuantos miembros quieres ingresar "))
for i in range(n):
    beatles.append(input(f"ingrese el miembro # {i} "))
print("Paso 3:", beatles)


del beatles[3]
del beatles[2]

print("Paso 4:", beatles)

beatles.insert("Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
