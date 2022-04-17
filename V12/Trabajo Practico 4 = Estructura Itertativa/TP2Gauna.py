#Realizar un programa para ingresar por el teclado, un conjunto de numeros e informar si la
#cantidad de elementos es impar o par, sin utilizar contadores. Finalizar la lectura 
#de datos con el valor -1.


n = 0
numero = int(input("Ingresar un número o ingresar -1 para terminar con el programa : "))
numero_nuevo = numero
while numero != -1:
    n = n + numero
    if numero % 2 == 0:
        print("El numero es par.")
    if numero % 2 != 0:
        print("El numero es impar.")
    numero = int(input("Ingresar un numero o ingresar -1 para terminar con el programa : "))

#Solo me muestra si el numero que ingrso es par o impar.