secret_number = 777

print(
    """
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
n = 0
while n != secret_number:
    n = int(input("adivina el numero secreto "))
    if n != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

print("¡Bien hecho, muggle! Eres libre ahora.")
