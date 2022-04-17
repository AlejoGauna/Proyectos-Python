print("Tres personas invierten dinero para fundar una empresa")
print("Clacular que porcentaje invirtio cada una.")

#ingresar los valores

primera = int(input("Ingrese el valor que invierte la primera persona : ""$"))
segunda = int(input("Ingrese el valor que invierte la segunda persona : ""$"))
tercera = int(input("Ingrese el valor que invierte la tercera persona : ""$"))

total = primera + segunda + tercera

#imprimir por pantalla el porcentaje
print("El porcentaje invertido de la primera persona =", primera * 100 / total,"%")
print("El porcentaje invertido de la segunda persona =", segunda * 100 / total,"%")
print("El porcentaje invertido de la tercera persona =", tercera * 100 / total,"%")
