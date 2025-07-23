"""
ingrese numero si cero es neutro, y determine si es positivo o negativo
"""
numero=int(input("Ingrese numero :"))
if numero==0:
    print(f" El {numero} es nuetro ")
elif numero>0:
    print(f" El {numero} es positivo ")
else:
    print(f" El {numero} es negativo ")

if numero%2==0:
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")
