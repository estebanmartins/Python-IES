#Ejercicios con funcion lambda
#Ejercicio 1
""" 

import math

# Defino la función lambda para calcular la superficie de un círculo pasandole como argumento 'radio'
calcular_superficie = lambda radio: math.pi * radio ** 2

# Solicito al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Aca calculo la superficie utilizando la función lambda y muestro por pantalla
superficie = calcular_superficie(radio)

print(f"La superficie del círculo es: {superficie}")

#salida ingresando 30
#La superficie del círculo es: 2827.4333882308138

""" 

#Ejercicio 2

""" 
# Lista original de números enteros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Uso map y lambda para filtrar los números pares
#List para convertir en lista los resultados del mapeo
#Map para aplicar la funcion a cada elemento de la lista numeros
#La condicion , si es par devuelve num, si no devuelve None

numeros_pares = list(map(lambda num: num if num % 2 == 0 else None, numeros))

#Aca filtro y solo agrego los que no son None. e imprimo la lista con numeros pares
numeros_pares = [num for num in numeros_pares if num is not None]


print(numeros_pares)
#salida [2, 4, 6, 8, 10]

"""
#Ejercicio 3
""" 
tuplas = [(3, 5), (6, 2), (9, 7), (4, 1), (8, 6), (7, 3)]

# Ordeno la lista de tuplas en función del segundo elemento de cada tupla '[1]'
tuplas_ordenadas = sorted(tuplas, key=lambda tupla: tupla[1])

print(tuplas_ordenadas)

""" 

#Ejercicio 4
""" 
edades = {'Miguel': 20, 'Norma': 25, 'Elizabeth': 19, 'Esteban': 31, 'Jorge': 21}

# Utilizar una función lambda para incrementar las edades en 1
#La función lambda (lambda e: e + 1) recibe el valor de cada edad y le suma 1.
edades_incrementadas = {nombre: (lambda e: e + 1)(edad) for nombre, edad in edades.items()}

# Imprimir el diccionario con las edades incrementadas
print(edades_incrementadas)

"""

#Ejercicio 5
# Definir las funciones lambda para las operaciones
"""

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

# Función para mostrar el menú de opciones y solicitar la selección al usuario
def mostrar_menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para solicitar los números al usuario
def solicitar_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2

# Programa principal
while True:
    opcion = mostrar_menu()

    if opcion == '1':
        num1, num2 = solicitar_numeros()
        resultado = suma(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == '2':
        num1, num2 = solicitar_numeros()
        resultado = resta(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == '3':
        num1, num2 = solicitar_numeros()
        resultado = multiplicacion(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == '4':
        num1, num2 = solicitar_numeros()
        resultado = division(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == '5':
        print("Saliendo de la calculadora...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

""" 



#Ejercicio con modulos
#Ejercicio 1
""" 
import random                       #importo el modulo

def tirar_dados(): 
    dado1 = random.randint(1, 6)    #creo funcion para generar numeros random
    dado2 = random.randint(1, 6)    #randit genera un num entero en el rango especificado
    return dado1, dado2

while True:                        #bucle que solo sale al elegir el numero 2
    opcion = input("Seleccione una opción (para tirar presione 1/ para salir presione 2): ")
    
    if opcion == "1":
        resultado = tirar_dados()       #variable q guarda el resultado de la funcion al ser llamada
        print(f"Resultado de la tirada: {resultado}" )
    elif opcion == "2":
        print("El programa ha finalizado ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione 'tirar' o 'salir'.")

"""

#Ejercicio 2

""" 
import math

# Pido al usuario las medidas de la hipotenusa y el ángulo
hipotenusa = float(input("Ingrese la medida de la hipotenusa: "))
angulo = float(input("Ingrese el ángulo en grados (menor a 90): "))

#Aca calculo el cateto adyacente y el cateto opuesto usando math
cateto_adyacente = math.cos(math.radians(angulo)) * hipotenusa   #uso radians para convertir de grados a radianes
cateto_opuesto = math.sin(math.radians(angulo)) * hipotenusa

print(f"La medida del cateto adyacente es: {cateto_adyacente}")
print(f"La medida del cateto opuesto es: {cateto_opuesto}")

#salida
#La medida del cateto adyacente es: 17.320508075688775
#La medida del cateto opuesto es: 9.999999999999998
"""


