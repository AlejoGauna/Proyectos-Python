#Escribir un programa para convertir un numero binario de 4 cifras en un numero
#decimal. 
#El numero binario se ingresa como un solo numero entero de cuatro digitos.

#PROCEDIMIENTO : Para convertir un numero binario a decimal es necesario multiplicar
#el valor de cada digito por el numero 2 elevado a un exponente.
#Este exponente se obtiene de la posicion que ocupa el digito dentro del numero,
#comenzando desde la derecha con la posicion 0. Todos estos resultados se suman para
#obtener el valor final. Ejemplo : Convertir 1011 a decimal:
    #1(posicion tres)0(posicion dos)2(posicion uno)1(posicion cero) = 
    #= 1 * 2 ^ 3 + 0 * 2 ^ 2 + 1 * 2  ^ 1 + 1 * 2  ^ 0 = 11.


valor_final = int(input("--Ingresar valores entre 1 y 0--"))


#---------------------------------------------------------------------------------
#valor_uno = int(input("Ingrese el valor de la primera pocision : "))
#valor_dos = int(input("Ingrese el valor de la segunda pocision : "))
#valor_tres = int(input("Ingrese el valor de la tercera pocision : "))
#valor_cuatro = int(input("Ingrese el valor de la cuarta pocision : "))
#---------------------------------------------------------------------------------



valor_uno = 0000
valor_dos = 000;1
valor_tres = 00;10
valor_cuatro = 00;11
valor_cinco = 0;100
valor_seis = 0;101
valor_siete = 0;110
valor_ocho = 0;111
valor_nueve = 1000
valor_diez = 1010
valor_once = 1011
valor_doce = 1100
valor_trece = 1110
valor_cartoce = 1111


#0000
valor_final = (0 * 8) + (0 * 4) + (0 * 2) + (0 * 1)
print("el valor binario ",valor_uno," transformado a decimal es :", valor_final)

#0001
valor_final = (0 * 8) + (0 * 4) + (0 * 2) + (1 * 1)
print("el valor binario ",valor_dos," transformado a decimal es :", valor_final)

#0010
valor_final = (0 * 8) + (0 * 4) + (1 * 2) + (0 * 1)
print("el valor binario ",valor_tres," transformado a decimal es :", valor_final)

#0011
valor_final = (0 * 8) + (0 * 4) + (1 * 2) + (1 * 1)
print("el valor binario ",valor_cuatro," transformado a decimal es :", valor_final)

#0100
valor_final = (0 * 8) + (1 * 4) + (0 * 2) + (0 * 1)
print("el valor binario ",valor_cinco," transformado a decimal es :", valor_final)

#0101
valor_final = (0 * 8) + (1 * 4) + (0 * 2) + (1 * 1)
print("el valor binario ",valor_seis," transformado a decimal es :", valor_final)

#0110
valor_final = (0 * 8) + (1 * 4) + (1 * 2) + (0 * 1)
print("el valor binario ",valor_siete," transformado a decimal es :", valor_final)

#0111
valor_final = (0 * 8) + (1 * 4) + (1 * 2) + (1 * 1)
print("el valor binario ",valor_ocho," transformado a decimal es :", valor_final)

#1000
valor_final = (1 * 8) + (0 * 4) + (0 * 2) + (0 * 1)
print("el valor binario ",valor_nueve," transformado a decimal es :", valor_final)

#1010
valor_final = (1 * 8) + (0 * 4) + (1 * 2) + (0 * 1)
print("el valor binario ",valor_diez," transformado a decimal es :", valor_final)

#1011
valor_final = (1 * 8) + (0 * 4) + (1 * 2) + (1 * 1)
print("el valor binario ",valor_once," transformado a decimal es :", valor_final)

#1100
valor_final = (1 * 8) + (1 * 4) + (0 * 2) + (0 * 1)
print("el valor binario ",valor_doce," transformado a decimal es :", valor_final)

#1110
valor_final = (1 * 8) + (1 * 4) + (1 * 2) + (0 * 1)
print("el valor binario ",valor_trece," transformado a decimal es :", valor_final)

#1111
valor_final = (1 * 8) + (1 * 4) + (1 * 2) + (1 * 1)
print("el valor binario ",valor_cartoce," transformado a decimal es :", valor_final)




#---------------------------------------------------------------------------------
#valor_final = (valor_uno * 8) + (valor_dos * 4) + (valor_tres * 2) + (valor_cuatro * 1)
#print("El valor", valor_uno, valor_dos, valor_tres, valor_cuatro, " transformado en decimal es : ", valor_final)
#---------------------------------------------------------------------------------