#Una inmobiliaria paga a sus vendedores un salario de $50.000, mas una comision de $5000 por cada 
#venta realizada, mas el 5% del valor de las ventas. Realizar un programa que imprima el numero 
#del vendedor y el salario que le corresponde en un determinado mes. Se leen el numero del
#vendedor, la cantidada de ventas que realizo y el valor total de las mismas.

#-------------------------------------------

#El pago por comisión se refiere a la ganancia de un porcentaje del total de la venta de 
# productos o servicios a la que es acreedor un trabajador; son los trabajadores en los rubros 
# de ventas quienes suelen ganar comisiones por sus resultados.

#salario($50000) + comision($5000) + porcentaje de valor de las ventas(5%)

#el 5% de la venta = algo

#--------------------------------------------
salario_vendedores = 50000
comision_vendedores = 5000
porcentaje_valor_venta = 5

print("--Lista de propiedades que vendio el PRIMER VENDEDOR:--")

#ingreso el precio del producto uno
producto_uno = int(input("El PRIMER VENDEDOR vendio la propiedad uno a : "))
#calculo el valor de la venta del 5%
valor_venta_porcentaje_uno = porcentaje_valor_venta * producto_uno / 100
#imprimo por pantalla en resultado 
print("--------------------------------------------------------------------------------------")
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_uno, "/ 100  = ", valor_venta_porcentaje_uno)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_uno = comision_vendedores + valor_venta_porcentaje_uno
print("El valor total resibido de la primera propiedad vendida es : ", comision_vendedores, " + ",valor_venta_porcentaje_uno, " = ", total_resivido_uno)


print("-------------------------SEGUNDA PROPIEDAD-----------------------------------------------")
#ingreso el precio del producto dos
producto_dos = int(input("El PRIMER VENDEDOR vendio la propiedad dos a : "))
print("--------------------------------------------------------------------------------------")
#calculo el valor de la venta del 5%
valor_venta_porcentaje_dos = porcentaje_valor_venta * producto_dos / 100
#imprimo por pantalla en resultado 
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_dos, "/ 100  = ", valor_venta_porcentaje_dos)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_dos = comision_vendedores + valor_venta_porcentaje_dos
print("El valor total resibido de la segunda propiedad vendida es : ", comision_vendedores, " + ",valor_venta_porcentaje_dos, " = ", total_resivido_dos)



print("-------------------------TERCER PROPIEDAD-----------------------------------------------")
#ingreso el precio del producto tres
producto_tres = int(input("El PRIMER VENDEDOR vendio la propiedad tres a : "))
print("--------------------------------------------------------------------------------------")
#calculo el valor de la venta del 5%
valor_venta_porcentaje_tres = porcentaje_valor_venta * producto_tres / 100
#imprimo por pantalla en resultado 
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_tres, "/ 100  = ", valor_venta_porcentaje_tres)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_tres = comision_vendedores + valor_venta_porcentaje_tres
print("El valor total resibido de la tercera propiedad vendida es : ", comision_vendedores, " + ", valor_venta_porcentaje_tres, " = ", total_resivido_tres)



print("-------------------------RECIBO DEL MES-----------------------------------------------")
#calculo de cuanto seria la comision ganada en un mes
total_comision_mes_uno = comision_vendedores + comision_vendedores + comision_vendedores
print("El valor de la comision en el primer mes sera de 5.000 + 5.000 + 5.000 : ", total_comision_mes_uno, "$")
print("--------------------------------------------------------------------------------------")

#calculo de cuanto seria el porcentaje total en pesos del mes
valor_total_porcentaje_venta_mes_uno = valor_venta_porcentaje_uno + valor_venta_porcentaje_dos + valor_venta_porcentaje_tres
print("El valor del prosentaje en pesos em el primer mes sera de : ", valor_venta_porcentaje_uno, " + ", valor_venta_porcentaje_dos, " + ", valor_venta_porcentaje_tres, " = ", valor_total_porcentaje_venta_mes_uno)
print("--------------------------------------------------------------------------------------")

#calculo del total en pesos resibido en el mes del primer vendedor [50000 + (5000 + 5000 + 5000) + precio 5%]
recibo_mes = salario_vendedores + total_comision_mes_uno + valor_total_porcentaje_venta_mes_uno
print("El salario total resibido en un mes del PRIMER VENDEDOR sera de : ", salario_vendedores, " + ", total_comision_mes_uno, " + ", valor_total_porcentaje_venta_mes_uno, " = ", recibo_mes)
print("--------------------------------------------------------------------------------------")
print("")
print("")
print("")
print("--------------------------------------------------------------------------------------")
print("--Lista de productos que vendio el SEGUNDO VENDEDOR:--")
#ingreso el precio del producto uno
producto_uno_vendedor_dos = int(input("El segundo vendedor vendio la propiedad uno a : "))
#calculo el valor de la venta del 5%
valor_venta_porcentaje_uno_vendedor_dos = porcentaje_valor_venta * producto_uno_vendedor_dos/ 100
#imprimo por pantalla en resultado 
print("--------------------------------------------------------------------------------------")
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_uno_vendedor_dos, "/ 100  = ", valor_venta_porcentaje_uno_vendedor_dos)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_uno_vendedor_dos = comision_vendedores + valor_venta_porcentaje_uno_vendedor_dos
print("El valor total resibido de la tercera propiedad vendida es : ", comision_vendedores, " + ", valor_venta_porcentaje_uno_vendedor_dos, " = ", total_resivido_uno_vendedor_dos)



print("-------------------------SEGUNDA PROPIEDAD-----------------------------------------------")
#ingreso el precio del producto dos
producto_dos_vendedor_dos = int(input("El SEGUNDO VENDEDOR vendio el porducto dos a : "))
print("--------------------------------------------------------------------------------------")
#calculo el valor de la venta del 5%
valor_venta_porcentaje_dos_vendedor_dos = porcentaje_valor_venta * producto_dos_vendedor_dos / 100
#imprimo por pantalla en resultado 
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_dos_vendedor_dos, "/ 100  = ", valor_venta_porcentaje_dos_vendedor_dos)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_dos_vendedor_dos = comision_vendedores + valor_venta_porcentaje_dos_vendedor_dos
print("El valor total resibido de la tercera propiedad vendida es : ", comision_vendedores, " + ", valor_venta_porcentaje_dos_vendedor_dos, " = ", total_resivido_dos_vendedor_dos)



print("-------------------------TERCERA PORPIEDAD-----------------------------------------------")
#ingreso el precio del producto tres
producto_tres_vendedor_dos = int(input("El SEGUNDO VENDEDOR vendio la propiedad tres a : "))
print("--------------------------------------------------------------------------------------")
#calculo el valor de la venta del 5%
valor_venta_porcentaje_tres_vendedor_dos = porcentaje_valor_venta * producto_tres_vendedor_dos / 100
#imprimo por pantalla en resultado 
print("El cinco porciento resivido del valor de la venta es : ", porcentaje_valor_venta, "% * ", producto_tres_vendedor_dos, "/ 100  = ", valor_venta_porcentaje_tres_vendedor_dos)
print("--------------------------------------------------------------------------------------")
#calculo cuanto ganaria con el primero producto vendido
total_resivido_tres_vendedor_dos = comision_vendedores + valor_venta_porcentaje_tres_vendedor_dos
print("El valor total resibido de la tercera propiedad vendida es : ", comision_vendedores, " + ", valor_venta_porcentaje_tres_vendedor_dos, " = ", total_resivido_tres_vendedor_dos)
print("-------------------------RECIBO DEL MES-----------------------------------------------")



#calculo de cuanto seria la comision ganada en un mes
total_comision_mes_uno_vendedor_dos = comision_vendedores + comision_vendedores + comision_vendedores
print("El valor de la comision en el primer mes sera de 5000 + 5000 + 5000 : ", total_comision_mes_uno_vendedor_dos, "$")
print("--------------------------------------------------------------------------------------")

#calculo de cuanto seria el porcentaje total en pesos del mes
valor_total_porcentaje_venta_mes_uno_vendedor_dos = valor_venta_porcentaje_uno_vendedor_dos + valor_venta_porcentaje_dos_vendedor_dos + valor_venta_porcentaje_tres_vendedor_dos
print("El valor del prosentaje en pesos em el primer mes sera de : ", valor_venta_porcentaje_uno_vendedor_dos , " + ", valor_venta_porcentaje_dos_vendedor_dos, " + ", valor_venta_porcentaje_tres_vendedor_dos, " = ", valor_total_porcentaje_venta_mes_uno_vendedor_dos)
print("--------------------------------------------------------------------------------------")

#calculo del total en pesos resivido en el mes del primer vendedor [50000 + (5000 + 5000 + 5000) + precio 5%]
recibo_mes_vendedor_dos = salario_vendedores + total_comision_mes_uno_vendedor_dos + valor_total_porcentaje_venta_mes_uno_vendedor_dos
print("El salario total resibido en un mes del PRIMER VENDEDOR sera de : ", salario_vendedores, " + ", total_comision_mes_uno_vendedor_dos, " + ", valor_total_porcentaje_venta_mes_uno_vendedor_dos, " = ", recibo_mes_vendedor_dos)
print("--------------------------------------------------------------------------------------")
