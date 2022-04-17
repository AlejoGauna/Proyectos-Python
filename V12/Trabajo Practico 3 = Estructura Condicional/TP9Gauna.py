#Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo 
# basico y su antiguedad en años. Si es soltero se le incrementa el sueldo un 5% del salario 
# bruto por cada año de antiguedad, mientras que si es casado se le incrementa el sueldo a 7% 
# del bruto por cada año de antiguedad.
#Tambien se le realiza los siguientes descuentos:
#   Jubilacion: 11%
#   Obra Social: 3%
#   Sidicato: 3%

#Como datos de entrada se ingresa por teclado el sueldo basico, antiguedad y estado civil 
#(1 es soltero o 2 si es casado).
#Se debe informar:(Remplazar los 9 por valores que correspondan)

#   Estado Cibil: Soltero/Casado
#   Sueldo basico   |   Antiguedad  |   Descuentos  | Importe
#   $999.99             99 años                       +999.99
#                       Jubilacion      -999,99 
#                       Obra Social     -999,99
#                       Sindicato       -999,99       
#                                                      --------
#                       Sueldo Neto                    999,99

incremento_soltero = 5
incremento_casado = 7
descuento_jubilacion = 11
descuento_obra_social = 3
descuento_sindicato = 3


sueldo_basico = int(input("Ingrese el Sueldo Basico del Empleado : "))
antiguedad = int(input("Ingrese la Antiguedad del Usuario : "))
estado_civil = input("1 es soltero 2 si es casado : ")

#El salario neto es la diferencia entre el salario bruto y las cotizaciones 
# y retenciones de la seguridad social. Es decir, el trabajador realmente percibe el neto

#El salario bruto es el dinero que recibe un trabajador por el trabajo que desempeña en 
# la empresa, pero que está sujeto a retenciones fiscales en cada nómina que serán descontadas, 
# obteniendo como resultado el salario neto

#restricciones
if sueldo_basico <= 0:
    print("No existe tal cantidad.")
if antiguedad <= 0:
    print("No existe tal Año.")
#if estado_civil < 1 and estado_civil > 2:
#    print("Por favor ingrese las opcciones correspondientes.")



if estado_civil == "1":
    #toma el sueldo y lo aumenta un 5% 
    #1 año = 5%, 2 años = %10, etc.
    print("El Empleado es soltero asi que se le aumenta un %5 el sueldo basico.")
    años_antiguedad = incremento_soltero * antiguedad
    incremento_porcentaje = 100 + incremento_soltero#%105
    incremento_porcentaje_pesos = incremento_porcentaje * sueldo_basico / 100#$
    sueldo_basico_final = sueldo_basico * incremento_porcentaje_pesos + años_antiguedad#$
    descuento_jubilacion_final = 100 - descuento_jubilacion#89%
    jubilacion_pesos = descuento_jubilacion_final * sueldo_basico / 100#$
    descuento_obra_social_final = 100 - descuento_obra_social#%97
    obra_social_pesos = descuento_obra_social_final * sueldo_basico / 100#$
    descuento_sindicato_final = 100 - descuento_sindicato#%97
    sindicato_pesos = descuento_sindicato_final * sueldo_basico / 100#$
    sueldo_final = jubilacion_pesos + obra_social_pesos + sindicato_pesos#$
    print("El Estado Civil es, Soltero",)
    print("El sueldo Basico del Empleado es , ", sueldo_basico, " $ ")
    print("La Antiguedad del Empleaddo es de, ", antiguedad, " Años ")
    print("El Descuento por la Jubulacion es de , -", jubilacion_pesos)
    print("El Descuento por la Obra Social es de , -", obra_social_pesos)
    print("El Descuento por el Sindicato es de , -", sindicato_pesos)
    print("El Importe del Empleado es de, +",sueldo_final - incremento_porcentaje_pesos, " $ ")
    print("El Salario Neto del Empleado es de, ",sueldo_final - incremento_porcentaje_pesos, " $ ")



else:
    if estado_civil == "2":
        #toma el sueldo y lo aumenta un 7%
        #1 año = 7%, 2 años = 14%, etc
        print("El Empleado es casaddo asi que se le aumenta un %7 el sueldo basico")
        años_antiguedad = incremento_casado * antiguedad
        incremento_porcentaje = 100 + incremento_casado
        sueldo_basico_final = sueldo_basico * incremento_porcentaje + años_antiguedad
        descuento_jubilacion_final = 100 - descuento_jubilacion
        descuento_obra_social_final = 100 - descuento_obra_social
        descuento_sindicato_final = 100 - descuento_sindicato
        sueldo_final = sueldo_basico_final - descuento_jubilacion_final - descuento_obra_social_final - descuento_sindicato_final
        print("El Estado Civil es, ", estado_civil)
        print("El sueldo Basico del Empleado es , ", sueldo_basico)
        print("La Antiguedad del Empleaddo es de, ", antiguedad, " Años ")
        print("El Descuento por la Jubulacion es de , -",sueldo_basico_final - descuento_jubilacion_final, " $ ")
        print("El Descuento por la Obra Social es de , -",sueldo_basico_final - descuento_jubilacion_final - descuento_obra_social_final, " $ ")
        print("El Descuento por el Sindicato es de , -",sueldo_final)
        print("El Importe del Empleado es de, +", descuento_jubilacion_final + descuento_obra_social_final + descuento_sindicato_final, " $ ")
        print("El Salario Neto del Empleado es de, ",sueldo_basico - (descuento_jubilacion_final + descuento_obra_social_final +descuento_sindicato_final), " $ ")





