#Crear un programa que pida un numero del mes (por ejemplo 4) y escriba el nombre 
#del mes en letras("abril").
#Verificar que el mes sea valido y mostrar un mensaje de error en caso que no lo
#sea.

enero = 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8 
septiembre = 9
octubre = 10
nobiembre = 11 
diciembre = 12

#ingreso valor 
numero_mes = int(input("Ingrese un numero del mes : "))


#condiciones
if numero_mes == 1:
    print("enero")
else:
    if numero_mes == 2:
        print("febrero")


if numero_mes == 3:
    print("marzo")
else:
    if numero_mes == 4:
        print("abril")


if numero_mes == 5:
    print("mayo")
else:
    if numero_mes == 6:
        print("junio")


if numero_mes == 7:
    print("julio")
else: 
    if numero_mes == 8:
        print("agosto")


if numero_mes == 9:
    print("septiembre")
else:
    if numero_mes == 10:
        print("octubre")


if numero_mes == 11:
    print("noviembre")
else:
    if numero_mes == 12:
        print("diciembre")

#en caso de que no se cumplan
if numero_mes > 12:
    print("ERROR, MES INSEXISTENTE")

if numero_mes <= 0:
    print("ERROR, MES INSEXISTENTE")


