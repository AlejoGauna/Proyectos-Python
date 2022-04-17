#ejercicio 1: Calcular el valor de las siguientes expresiones,
#respetando el orden de operaciones establecidos.
#A_12*4+4*5

print("Ejercicio 1: Calcular el valor de las siguientes expreciones,\n representando el orden de las operaciones establecidas")

print("--------------------------------------------------------")
print("A_12 *4 + 4 * 5")
a = 12
b = 4
c = 5
producto = a * b
productodos = b * c

#imprime por pantalla el prodcto de 12*4
print("El resultado de 12 * 4 =", producto)
#imprime por pantalla el prodcto de 4*5
print("El resultado de 4 * 5 =", productodos)
#imprime por pantalla el resultado final de todo
print("El resultado final =", producto + productodos)
print("--------------------------------------------------------")

print("B_(12 * (1 - 5) + 4) * 3")
a = 1
b = 5
c = 12
resta = a - b
producto = c * -4

#imprimir por pantalla a-b
print("El resultado de 1 - 5 =", resta)
#imprimir por pantalla c*-4
print("El resultado de 12 * (-4) =", producto)
#imprimir por pantalla producto+4
print("El resultado de -48 + 4 =", producto + 4)
#imprimir por pantalla -44*3
print("El resultado de -44 * 3 =", -44 * 3)
#imprimir el resultado final de todo
print("El resultado final de 12 * (1 - 5) + 4) * 3 =", (c * resta + 4) * 3)
print("--------------------------------------------------------")

print("C_12 * 1 -5 +4 *3")
a = 12
b = 1
c = 4
d = 3
productouno = a * b
productodos = c * d

#imprimir por pantalla producto de 12*1
print("El resultado de 12 * 1 =", productouno)
#imprimir por pantalla producto de 4*3
print("El resultado de 4 * 3 =", productodos)
#imprimir producto -5+ producto
print("El resultado final de 2 * 1 -5 +4 *3 =", productouno -5+ productodos)
print("--------------------------------------------------------")

print("D_(17 - 2) / 5")
a = 17
b  = 2
resta = a - b

#imprimir por pantalla 17 - 2
print("El resultado de 17 - 2 =", resta)
#imprimir por patalla resta / 5
print("El resultado final de (17 - 2) / 7 =", resta / 5)
print("--------------------------------------------------------")

print("E_3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3")
a = 2
b = 8
productouno = a * 2
productodos = b * productouno
c = 1
d = 2.0
division = c / d
sumadeproductos = productodos + division

#imprimir por patalla el producto de 2 * 2
print("El resultado de 2 * 2 =", productouno)
#imprimir por pantalla el producto de 8 * 4
print("El resultado de 8 * 4 =", b * productouno)
#imprimir por pantalla la division de 1 / 2.0
print("El resultado de 1 / 2.0 =", division)
#imprimir por pantalla (8 * 4 + 1 / 2.0) * 3
print("El resultado de 8 * 4 + 1 / 2.0 =", sumadeproductos * 3)
#imprimir por pantalla 3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3
print("El resultado final de 3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3 =", 3 + productouno - sumadeproductos * 3)
print("--------------------------------------------------------")

print("F_5 * 4 / 2")
a = 5
b = 4
producto = a * b

#imprimir por pantalla el producto de 5 * 4
print("El resultado de 5 * 4 =", producto)
#imprmir por pantalla la division de producto / 2
print("El resultado final de 5 * 4 / 2 =", producto / 2)
print("--------------------------------------------------------")

print("G_5 * (4 / 2)")
a = 5
b = 4
c = 2
division = b / c
producto = a * division
#imprimir por pantalla la division de 4 / 2
print("El resultado de 4 / 5 =", division)
#imprimir por pantalla el producto de 5 * producto
print("El resultado final de 5 * 4 / 2 =", producto)
print("--------------------------------------------------------")

print("H_24 / 2 ** 2")
a = 24
b = 2
potencia = b * 2
division = a / potencia

#imprmir por pantalla la el producto de potencia
print("El resultado de 2 ** 2 =", potencia)
#imprimir por pantalla la division de 24 / 2 ** 2
print("El resultado final de 24 / 2 ** 2 =", division)
print("--------------------------------------------------------")

print("I_(24 / 2) ** 2")
a = 24
b = 2
division = a / b
potencia = division * division

#imprimir por pantalla la division de 24 / 2
print("El resultado de 24 / 2 =", division)
#imprimir por pantalla la potencia de la division
print("El resultado final de (24 / 2) ** 2 =" ,potencia)
print("--------------------------------------------------------")

print("J_3 + 4 * 6 / 2 - 5")
a = 2
b = 4
c = 6
producto = b * c
division = producto / a

#imprimir por pantalla porducto de 4 * 6
print("El resultado de 4 * 6 =", producto)
#imprimir por pantalla division de producto / 2
print("El resultado de 4 * 6 / 2 =", division)
#imprimir por pantalla 3 + 4 * 6 / 2 - 5
print("El resultado final de 3 + 3 * 6 / 2 - 5 =", 3 + division - 5)
print("--------------------------------------------------------")

print("K_3 + 4 * 6 / (2 - 5)")
a = 2
b = 5
resta = a - b
c = 4
d = 6
division = c * d / resta

#imprimir por pantalla la resta de 2 - 5
print("El resultado de 2 - 5 =", resta)
#imprimir por pantalla el producto de 4 * 6
print("El resultado de 4 * 6 =", producto)
#imprimir  por pantalla la division de producto / resta
print("El resultado de 4 * 6 / (2 - 5) =", division)
#imprimir por pantalla 3 + 4 * 6 / (2 - 5)
print("El resultado final de 3 + 4 * 6 / (2 - 5)=", 3 + division)
print("--------------------------------------------------------")

print("L_(- 0.1) * 3")
a = -0.1

#imprimr el producto de (- 0.1) * 3
print("El resultado final de (- 0.1) * 3 =", a * 3)
print("--------------------------------------------------------")

print("M_- 9 ** 2")
a = -9
b = 9

#imprimir por pantalla la potencia de - 9 ** 2
print("El resultado final de - 9 ** 2 =" ,a * b)
print("--------------------------------------------------------")

print("N_(- 9) ** 2")
a = -9

#imprimir por pantalla la potencia de - 9 ** 2
print("El resultado final de - 9 ** 2 =" ,a * a)
print("--------------------------------------------------------")

print("O_10 / 3")
a = 10
b = 3
division = a / b

#imprimr por pantalla la division de 10 / 3
print(" El resultado final de 10 / 3 =", division)
print("--------------------------------------------------------")

print("P_10 // 3")
a = 10
b = 3
divisionentera = a // b

#imprimri pot pantalla la division entera de 10 // 3
print("El resultado final de 10 // 3 =", divisionentera)
print("--------------------------------------------------------")

print("Q_12 % 5")
a = 12
b = 5
modulo = a % b

#imprimir por pantalla el modulo o resto de 12 % 5
print("El resultado final de 12 % 5 =", modulo)
