#Ingrese dos numeros enteros e indica si son iguales o distintos.

#ingreso numeros enteros
numero = int(input("Ingrese cualquier valor : "))
numero_dos = int(input("Ingrese caulquier valor : "))

#condicion: si son iguales
if numero == numero_dos:
    print("El valor ", numero, " es igual a ", numero_dos)

#condicion: si son distintos
elif numero != numero_dos:
    print("El valor ", numero, " es distinto a ", numero_dos)
