#Leer un numero correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no.
#Un año es bisiesto si es divisible por 4. Sin embargo, aquellos años que sean divisibles por
#4 y tambien por 100 no son bisiestos, a menos que tambien sean divisibles por 400. Por ejemplo,
#1900 no fue bisiesto pero si el 2000.

divisible = 4
divisible_uno = 100
divisible_dos = 400


año = int(input("Ingrese el año : "))

if año % divisible == 0 and año % divisible_uno == 0 and año % divisible_dos == 0:
    print("Este año es divisible por 4, 10 y 400, asi que es Bisiesto")
elif año % divisible == 0 and año % divisible_uno == 0:
    print("Este año es divisible por 4 y por 100, así que no es Bisiesto.")
elif año % divisible == 0:
    print("El año que ingreso es Bisiesto.")


else:
    print("No existe un año que sea negativo.")