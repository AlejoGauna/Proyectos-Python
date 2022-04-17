#Leer tres numeros correspondientes al dia, mes y año de una fecha e imprimir un mensaje indicando
#si la fecha es valida o no.




dia = int(input("Ingrese el día : ")) 
mes = int(input("Ingrese el mes : "))
año = int(input("Ingrese el año : "))

if año < 0:
    print("Este año no existe.")
elif mes > 13:
    print("Este mes no existe")
elif dia > 31:
    print("Este dia no existe")
else:
    print("El dia ", dia, " / ", mes, " / ", año, " existe.")

