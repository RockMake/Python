from colorama import Fore, Style, Back, init
init(convert=True)

sw = 0
formula = ""

print(Style.BRIGHT + Fore.YELLOW + "elegir una opcion" + Style.RESET_ALL + Fore.GREEN + """
      
 (   )   raiz    i  
-------------------
 +   -    *      /  
-------------------
 p   v   enter  

   """)
while sw == 0:
    opc = input(" ")
    if (str(opc) == "("):
        formula = formula + " " + opc
    elif (str(opc) == ")"):
        formula = formula + opc + " "
    elif (str(opc) == "raiz"):
        radicando = int(input("ingrese radicando "))
        formula = formula + "raiz(" + str(radicando) + ")"
    elif (str(opc) == "i"):
        formula = formula + opc
    elif (str(opc) == "+"):
        formula = formula + opc
    elif (str(opc) == "-"):
        formula = formula + opc
    elif (str(opc) == "*"):
        formula = formula + opc
    elif (str(opc) == "/"):
        formula = formula + opc
    elif (str(opc) == "p"):
        base = int(input("escriba base "))
        potencia = int(input("escriba potencia "))
        formula = formula + str(base) + "^(" + str(potencia)+")"
    elif (opc == ""):
        sw = 1
    elif (int(opc) < 100000000000000):
        formula = formula + str(opc)
    print(formula)
    print("")
