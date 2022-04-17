#Desarrollar un programa que imprimia los numeros naturlaes comprendidos entre 1 y N. El valor de N se ingresa desde 
#el teclado.


contador = 1
valor_n = int(input("Ingrese el numero que se va a usar como rango : "))


while contador <= valor_n:
    print(contador)
    contador = contador + 1


