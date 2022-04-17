#Leer un numero entero e imprimir un mensaje indicando si es par o impar


numero = int(input("Ingresa un número: "))
#calculo para saber si es par (si el reciduo es igual a 0)
if numero % 2 == 0:
    print("El número es par")
else:
#imprime por pantalla que es impar (si el reciduo es distinto a 0)
    print("El número es impar")