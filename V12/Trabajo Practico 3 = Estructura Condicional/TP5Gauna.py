#if condicion:
 #   ejecutar codigo si la condicion es True
#else:
 #    ejecutar codigo si la condicion es False

#if primera_condicion:
#     ejecutar sentencia
#elif segunda_condicion:
#     ejecutar sentencia
#else:
#    ejecutar sentencia alternativa si todas las condiciones previas son son evaluadas como False






#Una editorial determina el precio de un libro segun la cantidad de paginas que
#contiene. El costo basico del libro es de $500, mas $3,20 por pagina con 
#encuadernacion rustica.
#Si el numero de pagina supera las 300 la encuadernacion debe ser en tela, lo que
#incrementa el costo en $200. Ademas, si el numero de pagina sobrepasa las 600
#se hace necesario un prosedimiento especial de encuadernacion que incrementa
#el costo en $336.
#Determinar un programa que calcule el costo de un libro dado el numero 
# de paginas.

#costo de libro basico = $500 + $3.20 (encuadernacion rustica) aprox. mayor a 600 paginas

#costo de libro = $336 por mas de 600 paginas (procedimento especial)

#costo de libro = $200 por mas de 300 paginas (encuadernacion de tela)


#COSTOS
precio_basico = 500
precio_basico_plus = 3.20
precio_medio = 336
precio_barato = 200

#PAGINAS
libro_medio = 600
libro_barato = 300

cantidad_paginas = int(input("¿Qué cantidad de paginas de desea? : "))
precio = int(input("Ingrese su cantidad de precio : "))

if cantidad_paginas == 0 and precio > 0:
    print("No existe tal cantidad de paginas.")
if cantidad_paginas < 0 and precio > 0:
    print("No existe tal cantidad de paginas.")
if cantidad_paginas < 300 and precio > 0:
    print("No tenemos libros con esa cantidad de paginas")

if cantidad_paginas >= 300 and cantidad_paginas < 600:
    print("El precio por esa cantidad de paginas va a ser de $200")
    precio_final = precio - 200
    print("El vuelto sera de ", precio_final)

if cantidad_paginas == 600:
    print("El precio por esa cantidad de paginas va a ser de $336")
    precio_final_dos = precio - 336
    print("El vuelto sera de ", precio_final_dos)

if cantidad_paginas > 600 and precio == 500:
    precio_final_tres = precio + 3.20
    print("Coste de $500 por la cantidad de, ", precio_final_tres)

if cantidad_paginas > 600 and precio > 500:
    precio_final_cuatro = precio - 336
    print("El vuelto sera de ", precio_final_cuatro)

    











