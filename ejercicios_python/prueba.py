# inicializamos las variables
entero = 0
imaginario = 0
esci = False
signo = 1
formula = ""

# mostramos el menú
print("Menu")
print("| ( |  ) |  raiz |  i  |  ")
print("------------------------")
print("| + |  - |   *   |  /  |  ")
print("------------------------")
print("| p |       enter      | ")
print("Digite la opción:")

# bucle para leer la entrada del usuario hasta que se presione enter
while True:
    # leemos la opción
    opcion = input(": ")
    
    if opcion == "": # el usuario presionó enter
        break
        
    elif opcion in ["(", ")", "raiz", "i", "+", "-", "*", "/", "p"]:
        # si es una opción válida, la agregamos a la fórmula
        formula += " " + opcion
        
        if opcion == "i":
            esci = True # marcamos que el próximo número es imaginario
            signo = 1 # el signo por defecto del siguiente número es positivo
            
        elif opcion == "-":
            signo = -1 # el signo por defecto del siguiente número es negativo
            
        elif opcion == "raiz":
            radicando = int(input("Ingrese el radicando: "))
            formula += "(" + str(radicando) + ")"
            numero_raiz = (radicando, 0) # inicializamos el número que se obtendrá de la raíz
            
            if esci: # si el número anterior era imaginario, agregamos la parte imaginaria
                imaginario += signo * numero_raiz[1]
                esci = False # ya no estamos en modo imaginario
            
            else: # si no era imaginario, agregamos la parte real
                entero += signo * numero_raiz[0]
                
            signo = 1 # el signo por defecto del siguiente número es positivo
            
        elif opcion == "p":
            base = int(input("Escriba la base: "))
            potencia = int(input("Escriba la potencia: "))
            formula += str(base) + "^(" + str(potencia)+")"
            numero_potencia = (base ** potencia, 0) # inicializamos el número que se obtendrá de la potencia
            
            if esci: # si el número anterior era imaginario, agregamos la parte imaginaria
                imaginario += signo * numero_potencia[1]
                esci = False # ya no estamos en modo imaginario
            
            else: # si no era imaginario, agregamos la parte real
                entero += signo * numero_potencia[0]
                
            signo = 1 # el signo por defecto del siguiente número es positivo
            
    elif opcion.isnumeric():
        # si es un número, lo convertimos a entero
        numero = int(opcion)
        
        if esci: # si el número anterior era imaginario, agregamos la parte imaginaria
            imaginario += signo * numero
            esci = False # ya no estamos en modo imaginario
            
        else: # si no era imaginario, agregamos la parte real
            entero = entero + entero
