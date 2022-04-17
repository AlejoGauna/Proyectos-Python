
#Ciclo While:

#a = 1
#while a <= 100:
#    print(a)
 #   a = a + 1

#El siguiente ejemplo pide un numero positivo al usuario una y otra vez hasta que el usuario lo haga correctamente.

#numero = int(input("Escriba un numero positivo : "))
#while numero < 0:
 #   print("Has escrito un numero negativo, intentelo de nuevo : ")
#    numero = int(input("Escriba un numero positivo : "))
#print("Gracias por su colaboracion...")

#si ingresa un numero positivo, el codigo ignora el while y pasa directamente al ultimo print.
#si ingrsa un numero negativo, el codigo hace lo siguiente:
#                                                            mientras que numero sea 0 entonces carga todo el codigo
#                                                            adentro del while.
#                                                            true adentro del codigo.
#                                                            false fuera del codigo.

#Leer un congunto de enteros e imprimir su promedio. El fin de los datos se indica ingresando el valor -1.

#suma = 0
#cant = 0
#n = int(input("Ingrese un numero o -1 para terminar : "))
#while n != -1:#mientras que n sea distinto de -1.
 #   suma = suma + n #acumulador
  #  cant = cant + 1 #contador
  #  n = int(input("Ingrese un numero o -1 para terminar : "))
#if cant != 0:
  #  promedio = suma / cant
  #  print("El promedio es : ", promedio)
#else:
    #print("No se ingresaron valores...")

#si ingreso un numero en el wiele va a decir, mientras n sea distinto de -1 a la variable suma sumale ese mismo
#numero, y a la variable cant sumale 1, y almacena el numero nuevo ingresado en la misma pirmera variable.
#si ingresa un -1 el programa ignora el while y pasa al if(si la variable cant es distinto de suma, imprimir
# el promedio de todos los numeros ingresados) si no entonces imprimir que no se ingrersaron valores.

#Leer un conjunto de enteros e imprimir el mayor. El fin de los datos se indica con -1.

#numero = int(input("Ingrese un numero o ingrese -1 para terminar el programa : "))
#numero_mayor = numero
#while numero != -1:
  #  if numero > numero_mayor:
  #      numero_mayor = numero
  #  numero = int(input("Ingrese un numero o -1 para terminar el programa : "))
#print("El mayor numero ingresado es, ",numero_mayor)

#x = 5

#while x > 0:
 #   print(x)
  #  x = x -1


contador = 0#el contador como su nombre lo indica, es para contar las veces que se ingresa un numero o valor.
carta = int(input("Ingrese un numero de una carta o ingrese -1 para termianr el programa : "))

while carta != -1:
    print("")
    contador = contador + 1
    carta = int(input("Ingrese un numero de una carta o ingrese -1 para terminar el programa : "))
print("el total de cartas que ingreso es de : ",contador)


acumulador = 0#el acumuladro, acumula los datos que ingreso y los suma con la primera variable.
carta = int(input("Ingrese un numero de una carta o ingrese -1 para termianr el programa : "))

while carta != -1:
    print("")
    acumulador = acumulador + carta
    carta = int(input("Ingrese un numero de una carta o ingrese -1 para terminar el programa : "))
print("el total de cartas que ingreso es de : ",acumulador)





contador = 1
acumulador = 0
numero = int(input("Ingrese hasta 10 un numeros : "))


while contador < 10:
    contador = contador + 1
    acumulador = acumulador + numero 
    print(acumulador)
    print(contador)
    numero = int(input("Ingrese hasta un total de 10 numeros : "))
    if contador == 10:
        promedio = acumulador / 10
        print(promedio)



contador = 0
numero = 1
numero_dos = 2
while contador < 2:
    contador = contador + 1
    suma = numero + numero_dos
    promedio = suma / contador
    print(promedio)  