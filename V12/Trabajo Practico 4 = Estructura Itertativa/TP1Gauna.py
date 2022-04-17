#Realizar un programa para ingresar desde el teclado un conjunto de numeros.
#Al finalizar mostrar por pantalla el primer y ultimo elemento ingresado.
#Finalizar la lectura con el valor -1.



contador = 0

conjunto_numeros = int(input("Ingrese un conjunto de numeros o ingrrese -1 para terminar el programa : "))
print("El primer numero ingresado es : ",conjunto_numeros)

while conjunto_numeros != -1:
    contador = contador + 1
    conjunto_numeros = int(input("Ingrese un conjunto de numeros o ingrese -1 para terminar el programa : "))
    if conjunto_numeros != -1:
        primer_numero = conjunto_numeros


print("Finaliza el programa, el ultimo numero ingresado es : ",primer_numero)







c = 0
numero = int(input("Ingrese un número o ingrese -1 para terminar el programa : "))
nuevo_numero = numero
if numero != 0:
    print("El primer número ingresado es , ",numero)

while numero != -1:
    c = c + numero
    numero = int(input("Ingrese un numero o ingrese -1 para terminar el programa : "))
if numero == numero:
    print("El ultimo número ingresado es , ",nuevo_numero)


#Solo me muestra el primer numero ingresado.

