#Leer una medida en metros e imprimir esta medida expresada en centimetros
#, pulgadas, pies y yardas. Los factores de conversion son:
    # 1 pie = 12 pulgadas
    # 1 yarda = 3 pies 
    # 1 pulgada = 2.54 cm
    # 1 metro = 100 cm

#ingresar una medida en metros

metro = 1
centimetros = 100

pulgada = 1
centimetros_pulgadas = 2.54

pies = 1
pies_pulgadas = 12

yardas = 1
yardas_pies = 3

#ingresar medida
primera_medida = int(input("Ingrese primera medida en metros : "))
#convercion de medida de m a cm
centimetros_obtenidos = primera_medida * centimetros / metro
#imprimir por pantalla el resultado
print(primera_medida, "metros a centimetros es : ", centimetros_obtenidos, "cm")

print("---------------------------------------------------------------")

#conversion de medida de cm a pulgada
pulgadas_obtenidas = centimetros_pulgadas * pulgada / centimetros_pulgadas
#imprimir por pantalla el resultado
print(centimetros_obtenidos, "centimetros a pulgadas es : ", pulgadas_obtenidas, "pulgadas")

print("---------------------------------------------------------------")

#conversion de medida de pulgada a pies
pies_obtenidas = pulgadas_obtenidas * pies / pies_pulgadas
#imprimir por pantalla el resultado
print(pulgadas_obtenidas, "pulgadas a pies es : ", pies_obtenidas, "pies")

print("---------------------------------------------------------------")

#conversion de medida de pies a yardas
yardas_obtenidas = pies_obtenidas * yardas / yardas_pies
#imprimir por pantalla el resultado
print(pies_obtenidas, "pies a yardas es : ", yardas_obtenidas, "yatdas")







