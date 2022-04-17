#Desarrollar un programa que imprima la suma de los numeros impares correspondidos 
#entre 42 y 176.

#43,45,47,43,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,83,91,93,95,
# 97,99,101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,
# 139,141,143,145,147,149,151,153,155,157,159,161,163,165,167,169,171,173,175

acumulador = 0

numero = int(input("Ingrese un numero entre 42 y 176 o -1 para terminar el programa : "))

impar = numero
par = numero

if numero < 42 and numero > 176:
    print("No se pueden sumar los numeros porque salen del rango especificado.")

while numero != -1:
    acumulador = acumulador + numero
    numero = int(input("Ingrese un numero entre 42 y 176 o -1 para terminar el programa : "))

if par % 2 == 0:
    print("No se pueden sumar los numeros porque hay numeros pares y que no estan en el rango especificado")

if impar % 2 != 0:
    print("La sumatoria de todos los numeros impares es de : ",acumulador)





cant = 0
numero = int(input("Ingresar un numero entre 42 y 176 :"))
nuevo_numero = numero
while numero > 42 and numero < 176:
    cant = cant + 1
    numero = int(input("Ingresar un numero entre 42 y 176 : "))
    if numero % 2 != 0:
        suma_numeros_impares = numero + nuevo_numero
        print("hola",suma_numeros_impares)
    
#si ingreso dos numeros impares los suma, pero si ingreso un tercer valor, entonces suma es
#valor + el primer numero ingresado impar.

    
