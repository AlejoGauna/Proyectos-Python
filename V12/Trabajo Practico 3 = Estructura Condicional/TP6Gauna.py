#Una remiseria requiere un programa que calcule el precio de un viaje a partir de la cantidad de
#kilometros que desea recorrer el usuario. Para eso cuenta la siguiente tarifa:
#   Viaje minimo $150
#   Si recorre entre 0 y 10 km: $20 por km
#   Si recorre 10km o mas: $15 por km

cantidad_usuario = int(input("Ingrese la cantidad de km que quiera recorrer : "))


if cantidad_usuario > 0 and cantidad_usuario < 10:
    print("Son $20 por km.")
    #20 * cantidad de kilometros = precio final
elif cantidad_usuario >= 10:
    print("Son $15 por km.")
    #15 * cantidad de kilometros = precio final


#si recorre entre 0 y 10 km
if cantidad_usuario == 9:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 8:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 7:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 6:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 5:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 4:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 3:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 2:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
elif cantidad_usuario == 1:
    print("Son $20 por km, es decir que son, ", cantidad_usuario * 20)
else:
    #si ingresa un cero en km
    if cantidad_usuario >= 0:
        print("No puedo llevarlo.")

#si recorre mas de 10 km
if cantidad_usuario == 11:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 1)
if cantidad_usuario == 12:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 2)
if cantidad_usuario == 13:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 3)
if cantidad_usuario == 14:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 4)
if cantidad_usuario == 15:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 5)
if cantidad_usuario == 16:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 6)
if cantidad_usuario == 17:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 7)
if cantidad_usuario == 18:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 8)
if cantidad_usuario == 19:
    print("Son $15 por km, es decir que son, ", cantidad_usuario * 9)
if cantidad_usuario == 20:
    print("Viaje minimo, son $150.")
    #si sobre pasa el limite del viaje minimo
if cantidad_usuario > 20:
    print("La tarifa del taxi paso a mas de $150.")

