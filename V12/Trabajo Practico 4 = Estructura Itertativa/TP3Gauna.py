#Realizar un programa para ingresar desde el teclado un conjunto de numeros y mostrar por
#pantalla el menor y el mayor de ellos. Finalizar la lectura de datos con el valor -1.

numero = int(input("Ingresar un numero o ingresar un -1 para que el programa termine : "))
numero_mayor = numero
numero_menor = numero
while numero != -1:
    if numero > numero_mayor:
        numero_mayor = numero
    if numero < numero_menor:
        numero_menor = numero
    numero = int(input("Ingresar un numero o ingresar -1 para que el programa termine : "))
print("El mayor numero ingresado es, ",numero_mayor)
print("El menor numero ingresado es, ",numero_menor)








