#Ejercicio 1
"""
nombre= input('Ingrese su nombre :')
edad = int(input('Ingrese su edad :'))
print(f"Hola, {nombre}. Tienes {edad} años.")
"""
#Ejercicio 2
"""
num1 = input('Ingrese primer numero : ')
num2 = int(input('Ingrese segundo numero :'))
print(f"Numero 1 es : {num1} , y su tipo es  {type(num1)}")
print(f"Numero 2 es : {num2} , y su tipo es  {type(num2)}")
"""
#Ejercicio 3
""" 
numero = float(input('Ingrese segundo numero :'))
print(numero)
"""
#Ejercicio 4
""" 
num1= int(input('Ingrese primer numero :'))
num2= int(input('Ingrese  segundo numero :'))
suma = num1+num2
resta = num1 - num2
multi = num1 * num2
division_flotante = num1 / num2
div_entera = num1 // num2
modulo = num1 % num2
potencia =num1 ** num2

print(f"La suma es igual a : {suma:.4g}")
print(f"La resta es igual a : {resta:.4g}")
print(f"La multi es igual a : {multi:.4g}")
print(f"La division_flotante es igual a : {division_flotante:.4g}")
print(f"La div entera  es igual a : {div_entera:.4g}")
print(f"el modulo es igual a : {modulo:.4g}")
print(f"El valor 1 potenciado al valor 2 es igual a : {potencia:.4g}")
""" 
#Ejercicio 5
""" 
numero = int(input('ingrese un numero : '))
raiz_cuadrada = numero ** 0.5

print(f"La raiz cuadra de {numero}, es : {raiz_cuadrada}")
""" 
#Ejercicio 6
""" 
numero = int(input('ingrese un numero : '))
residuo = numero % 2
if residuo == 0:
    print(f"El numero ingresado es {numero} y es un valor par")
else:
    print(f'El numero ingresado es {numero} y es un valor INPAR')
"""
#Ejercicio 7
"""
altura_mts = float(input('Ingrese su altura en metros : '))
peso_kgs = int(input('Ingrese su peso en kgs : '))
calculo_imc = peso_kgs / (altura_mts**2)
print(f"Su calculo de IMC es igual a  {calculo_imc}")
""" 
#Ejercicio 8
""" 
base = int(input("Ingrese la base del triangulo :"))
altura = int(input("Ingrese la altura del triangulo :"))
calculo = base * altura / 2
print(f"La superficie su triangulo es igual a {calculo}")
"""
#Ejercicio 9
"""
inversion = int(input("Ingrese su inversion deseada :"))
interes_anual = float(input("Ingrese el interes anual :"))
interes = interes_anual / 100
numero_anios = int(input("Ingrese el numero de años : "))
capital_obtenido =  inversion *(1+interes_anual/100)**numero_anios

print(f"Su capital obtenido es : {capital_obtenido}")
""" 
#Ejercicio 10
""" 
valor1 = int(input("Cuantos payasos se quieren enviar? :"))
valor2 = int(input("Cuantas muñecas se quieren enviar : "))
peso_payasos = valor1 * (250/1000)
peso_muniecas = valor2 * (120/1000)
peso_total = peso_payasos + peso_muniecas
print(f"El peso total del pedido es : {peso_total} kg")
"""
#Ejercicio 11
"""
# Coeficientes de la ecuación cuadrática
a = 2
b = 3
c = -5

# Cálculo del discriminante
discriminante = b**2 - 4*a*c

# Cálculo de las raíces
raiz_1 = (-b + (discriminante ** 0.5)) / (2*a)
raiz_2 = (-b - (discriminante ** 0.5)) / (2*a)

# Impresión de las raíces
print("Las raíces son:", raiz_1, "y", raiz_2)
""" 
#Ejercicio 12

""" 
# Coeficientes de la ecuación cuadrática
a = 2
b = 3
c = -5

# Cálculo del discriminante
discriminante = b**2 - 4*a*c

# Cálculo de las raíces
raiz_1 = (-b + (discriminante ** 0.5)) / (2*a)
raiz_2 = (-b - (discriminante ** 0.5)) / (2*a)

# Verificación de las raíces
ecuacion_1 = a*(raiz_1**2) + b*raiz_1 + c
ecuacion_2 = a*(raiz_2**2) + b*raiz_2 + c

# Impresión de los resultados
print("Ecuación 1:", ecuacion_1)
print("Ecuación 2:", ecuacion_2)
#Son igual a 0
""" 
#Ejercicio 13
"""
entero =200
flotante =200.10
booleano =True
print(f"Tipo : {type(entero)}, ID : {id(entero)}, Valor : {entero}")
print(f"Tipo : {type(flotante)}, ID : {id(flotante)}, Valor : {flotante}")
print(f"Tipo : {type(booleano)}, ID : {id(booleano)}, Valor : {booleano}")
""" 
#Ejercicio 14
""" 
#Variables dadas    #a convertir en
valor1 = 4.2        #int
valor2 = 4.2        #bool
valor3 = True       #int
valor4 = True       #float
valor5 = 6          #float
valor6 = 6          #bool

nuevo_valor1 = int(valor1) 
nuevo_valor2 = bool(valor2)
nuevo_valor3 = int(valor3)
nuevo_valor4 = float(valor4)
nuevo_valor5 = float(valor5)
nuevo_valor6 = bool(valor6)
print('----------------------------------------')
print(f"Valor antiguo 1: {valor1}, Tipo antiguo: {type(valor1)}, valor actualizado {nuevo_valor1}, Tipo actualizado {type(nuevo_valor1)}")
print('----------------------------------------')
print(f"Valor antiguo 2: {valor2}, Tipo antiguo: {type(valor2)}, Valor actualizado {nuevo_valor2}, Tipo actualizado {type(nuevo_valor2)}")
print('----------------------------------------')
print(f"Valor antiguo 3: {valor3}, Tipo antiguo: {type(valor3)}, Valor actualizado {nuevo_valor3}, Tipo actualizado {type(nuevo_valor3)}")
print('----------------------------------------')
print(f"Valor antiguo 4: {valor4}, Tipo antiguo: {type(valor4)}, Valor actualizado {nuevo_valor4}, Tipo actualizado {type(nuevo_valor4)}")
print('----------------------------------------')
print(f"Valor antiguo 5: {valor5}, Tipo antiguo: {type(valor5)}, Valor actualizado {nuevo_valor5}, Tipo actualizado {type(nuevo_valor5)}")
print('----------------------------------------')
print(f"Valor antiguo 6: {valor6}, Tipo antiguo: {type(valor6)}, Valor actualizado {nuevo_valor6}, Tipo actualizado {type(nuevo_valor6)}")
print('----------------------------------------')

"""
"""
Ejercicios
""" 

                  
                  