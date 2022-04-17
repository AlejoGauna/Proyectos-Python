#Una persona invierte su capital en un banco y desea saber cuanto dinero ganara
#en un mes, teniendo en cuneta que el banco paga el 2% mesnual.
#¿Cuanto ganara en seis meses si deja su dinero invertido?



primer_porcentaje_mensual = 2
segundo_porcentaje_mensual = 6

#ingreso cantidad invertida.
dinero = int(input("Ingreser valor invertido : ""$"))
#calculo para saber cuanto gana en un mes.
dinero_ganancia = primer_porcentaje_mensual * dinero / 100
#imprimir el resultado(dinero) gando en un mes
print("El dinero ganado en un mes es de : ", dinero_ganancia, "$ (interes)")


#calculo para saber cuanto porcentaje obtengo en seis meses 
porcentaje_seis_meses = segundo_porcentaje_mensual * primer_porcentaje_mensual / 1
#imprimir porsentaje obtenido en seis meses
print("El porcentaje obtenido de interes en seis mese sera : ", porcentaje_seis_meses, "%")

#calcular cuato vale el porcentaje
total_seis_meses = 12 * dinero / 100
#imprimir el resultado total obtennido en esis meses en pesos
print("El dinero ganado en sies meses es de : ", total_seis_meses, "$ (interes)")

print("--------------------------------------------------------------------------------------")

#INTERES COMPUESTO(si el usuario nunca retira el dinero)
#dinero del primer mes
dinero_primere_mes = dinero + dinero_ganancia
print("El usario ganara al cabo de un mes si no retira el dinero, un total de ", dinero_primere_mes, "$")

#dinero del segundo mes
dinero_ganancia_segundo_mes = primer_porcentaje_mensual * dinero_primere_mes / 100
dinero_segundo_mes = dinero_primere_mes + dinero_ganancia_segundo_mes 
print("El usario ganara al cabo de dos meses si no retira el dinero, un total de ", dinero_segundo_mes, "$")

#dinero del tercer mes
dinero_ganancia_tercer_mes = primer_porcentaje_mensual * dinero_segundo_mes / 100
dinero_tercer_mes = dinero_segundo_mes + dinero_ganancia_tercer_mes
print("El usario ganara al cabo de tres meses si no retira el dinero, un total de ", dinero_tercer_mes, "$")

#dinero del cuarto mes
dinero_ganancia_cuarto_mes = primer_porcentaje_mensual * dinero_tercer_mes / 100
dinero_cuarto_mes = dinero_tercer_mes + dinero_ganancia_cuarto_mes
print("El usario ganara al cabo de cuatro meses si no retira el dinero, un total de ", dinero_cuarto_mes, "$")

#dinero del quiento mes
dinero_ganancia_quinto_mes = primer_porcentaje_mensual * dinero_cuarto_mes / 100
dinero_quinto_mes = dinero_cuarto_mes + dinero_ganancia_quinto_mes
print("El usario ganara al cabo de sinco meses si no retira el dinero, un total de ", dinero_quinto_mes, "$")

#dinero del sexto mes
dinero_ganancia_sexto_mes = primer_porcentaje_mensual * dinero_quinto_mes / 100
dinero_sexto_mes = dinero_quinto_mes + dinero_ganancia_sexto_mes

#imprimir cuanto se ganan en el sexto mes en dinero
print("El usario ganara al cabo de seis meses si no retira el dinero, un total de ", dinero_sexto_mes, "$")
