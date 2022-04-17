#Un cajero necesita para sus cajeros automaticos un programa que lea una cantidad de dinero e imprima a cuantos billetes 
#equivale, considerando que existen billetes de $1000, $500, $100, $50 y $10. 
#Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
#Mostrar un mensaje de error si no se pudiera entregar la cantidad solicitada

billete_diez = 10
billete_cincuenta = 50
billete_cien = 100
billete_quinientos = 500
billete_mil = 1000

valor = int(input("Ingresar valor que quiera retirar $ : "))

#calculo que me devuelva cauntos billetes de 1000
billetes_usados_mil = valor // billete_mil 
print("se usan :", billetes_usados_mil, " $ billetes de 1000 $")
#calculo para que me devuelva cuanto me queda 
valor_uno = valor % 1000 
print("me quedan :", valor, " $ billetes")


#calculo que me devuelva cauntos billetes de 500
billetes_usados_quinientos = valor // billete_quinientos
print("se usan :", billetes_usados_quinientos, " $ billetes de 500 $") 
#calculo para que me devuelva cuanto me queda 
valor = valor % 500 
print("me quedan :", valor, " $ billetes")


#calculo que me devuelva cauntos billetes de 100
billetes_usados_cien = valor // billete_cien
print("se usan :", billetes_usados_cien, " $ billetes de 100 $") 
#calculo para que me devuelva cuanto me queda 
valor = valor % 100 
print("me quedan :", valor, " $ billetes")


#calculo que me devuelva cauntos billetes de 50
billetes_usados_cincuenta = valor // billete_cincuenta
print("se usan :", billetes_usados_cincuenta, " $ billetes de 50 $") 
#calculo para que me devuelva cuanto me queda 
valor = valor % 100 
print("me quedan :", valor, " $ billetes")


#calculo que me devuelva cauntos billetes de 10
billetes_usados_diez = valor // billete_diez
print("se usan :", billetes_usados_diez, " $ billetes de 10 $") 
#calculo para que me devuelva cuanto me queda 
valor = valor % 100 
print("me quedan :", valor, " $ billetes")



