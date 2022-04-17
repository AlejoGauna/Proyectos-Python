#Ingresar las notas de los parciales de un alumno e indicar si promociono, aprobo
#o si debe recuperar. 
#Informar un error si el valor de alguna nota no esta entre 0 y 10.
    # . Se promociona cuando las notas de ambos parciales son mayores o iguales a 7
    # . Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4
    # . Se debe recuperar cuando al menos una de las dos notas es mayor a 4


promocion = 7
aprobado = 4

#ingreso los valores
nota_uno = int(input("El alumno saco en el Pirmer Parcial : "))
nota_dos = int(input("El alumno saco en el Segundo Parcial : "))
print("--------------------------------------------------------------")
#en caso de que ingrese valores menores que 0 y mayores a 10
if nota_uno < 0:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
if nota_dos < 0:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
if nota_uno > 10:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
if nota_dos > 10:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
print("--------------------------------------------------------------")
#si las notas agregadas son mayores a 10
if nota_uno > 10 and nota_dos > 10:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
#si se saca una nota mayor a 7 en ambos parciales
elif nota_uno >= promocion and nota_dos >= promocion:
    print("El alumno promociona la asignatura")
print("--------------------------------------------------------------")


#-----------------------------PROMOCION--------------------------------
#si se saca una nota menor a 7 en el primer pacial
if nota_uno < promocion:
    print("El alumno no promociono porque no llego a 7 en el primer pacial")
print("--------------------------------------------------------------")
#si se scaca una nota menor a 7 en el segundo parcial
if nota_dos < promocion:
    print("El alumno no promociona por que no llego a 7 en el segundo parcial")
    print("--------------------------------------------------------------")
#si se saca una nota menor a 7 en ambos parciales al mismo tiempo
else:
    if nota_uno < promocion and nota_dos < promocion:
        print("El alumno no promociona la asignatura")
print("--------------------------------------------------------------")


#-----------------------------APROBADO--------------------------------
#si ingresa valores mayores a 10
if nota_uno > 10 and nota_dos > 10:
    print("ERROR, NO SE EVALUA CON ESTA NOTA")
#si se saca una nota mayor o igual a 4 en ambos parciales al mismo tiempo
elif nota_uno >= aprobado and nota_dos >= aprobado:
    print("El alumno aprobo los dos parciales")
    print("--------------------------------------------------------------")
#si se sca una nota menor o igual a 4 en ambos parciales
else:
    if nota_uno <= aprobado and nota_dos <= aprobado:
        print("El alumno no aprobo los dos parciales")
print("--------------------------------------------------------------")

#-----------------------------RECUPERATORIO--------------------------------
#para recuperar
if nota_uno < aprobado and nota_dos > aprobado:
    print("El aluno saco ", nota_uno, " en el primer pacial y ", nota_dos, " en el segundo parcial entonces debe recuperar el primer pacial")
    print("--------------------------------------------------------------")
else:
    if nota_uno > aprobado and nota_dos < aprobado:
        print("El aluno saco ", nota_uno, " en el primer pacial y ", nota_dos, " en el segundo parcial entonces debe recuperar el segundo pacial")
        print("--------------------------------------------------------------")

