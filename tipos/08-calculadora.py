numero1 = int(input("ingresas tu numero  "))
numero2 = int(input("inglesa tu segundo numero  "))

suma = numero1 + numero2
resta = numero1 - numero2
mult = numero1 * numero2
divi = numero1 / numero2

Resultado = f"""
_________ Resultados ___________
los resultado del {numero1} y {numero2} son: 

1 resultado de la suma = {suma}
2 resultado de la resta = {resta}
3 resultado de la multiplicacion = {mult}
4 resultado de la division = {divi}

"""
print(Resultado)
