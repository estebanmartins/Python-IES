#Ejercicio 1
"""
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
else :
    print("Usted es menor de edad")
""" 
#Ejercicio 2
""" 
pw = 'password'
password_user = input("Ingrese contraseña: ").lower()

if password_user == pw :
    print("La contraseña es valida")
else:
    print("La contraseña ingresada es Invalida")
"""
#Ejercicio 3
""" 
num1 = int(input("ingrese numero 1 : "))
num2 = int(input("  ingrese numero 2 :  "))
division= num1 // num2

if num2 > 0:
    print(f"El resultado es igual a {division}")
"""
#Ejercicio 4
"""
num_entero = int(input("ingrese un numero entero : "))
resto = num_entero % 2
if resto == 0:
    print('es par')
else:
    print('es inpar')
""" 
#Ejercicio 5
"""
nombre = input("ingrese su nombre: ")
sexo = input("ingrese su sexo: ")

if (nombre < 'h' and sexo == 'mujer') or (nombre > 'm' and sexo == 'hombre'):
    print('perteneces al grupo A')
else:
    print('perteneces al grupo B')
    
""" 
#Ejercicio 6
"""
edad_cliente = int(input('Ingrese su edad en numeros: '))
precio_entrada = 0

if edad_cliente < 4 :
    print('Entrada gratuita')
elif edad_cliente >= 4 and edad_cliente <= 18 :
    print('El precio de la entrada es $400')
else:
    print('El precio de la entrada es $900')
""" 
#Ejercicio 7
""" 
print("Bienvenido/a a la Pizzería Bella Napoli")
print("¿Desea una pizza vegetariana o no vegetariana?")
opcion = input("Ingrese 'V' para vegetariana o 'NV' para no vegetariana: ")

# Mostrar opciones de ingredientes según la elección del usuario
if opcion.upper() == "V":
    print("Ingredientes disponibles para pizzas vegetarianas:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes disponibles para pizzas no vegetarianas:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

# Solicitar al usuario que elija un ingrediente
eleccion = input("Seleccione un ingrediente (ingrese el número correspondiente): ")

# Determinar el tipo de pizza y los ingredientes seleccionados
if opcion.upper() == "V":
    tipo_pizza = "Vegetariana"
    if eleccion == "1":
        ingrediente = "Pimiento"
    elif eleccion == "2":
        ingrediente = "Tofu"
else:
    tipo_pizza = "No vegetariana"
    if eleccion == "1":
        ingrediente = "Peperoni"
    elif eleccion == "2":
        ingrediente = "Jamón"
    elif eleccion == "3":
        ingrediente = "Salmón"

# Mostrar la pizza seleccionada y los ingredientes
print("Ha elegido una pizza", tipo_pizza)
print("Ingredientes: Mozzarella, Tomate, ", ingrediente)
"""
#Ejercicio 8
""" 
año = int(input('Ingrese un año en numeros: '))
if año % 4 == 0 and año % 100 != 0:
    print('El año es bisiesto')
else:
    print('El año es normal')
"""
#Ejercicio 9
""" 
persona1  = input('Persona 1 Elije entre:  piedra-papel-tijera: ').lower()
persona2  = input('Persona 2 Elije entre:  piedra-papel-tijera: ').lower()

opciones = ['tijera','piedra','papel']

if persona1 == opciones[1] and persona2 == opciones[0]:
    print('Piedra le gana a tijera GANA PERSONA 1')
elif persona2 == opciones[1] and persona1 == opciones[1]:
    print('Piedra le gana a tijera GANA PERSONA 2')
elif persona1 == opciones[2] and persona2 == opciones[1]:
    print('Papel le gana a piedra GANA PERSONA 1')
elif persona2 == opciones[2] and persona1 == opciones[1]:
    print('Papel le gana a piedra GANA PERSONA 2')
elif persona1 == opciones[0] and persona2 == opciones[2]:
    print('Tijera le gana a papel GANA PERSONA 1')
elif persona2 == opciones[0] and persona1 == opciones[2]:
    print('Tijera le gana a papel GANA PERSONA 2')
elif persona1 != opciones:
    print('Ingrese una opcion valida entre piedra papel o tijera')
else:
    print('Empate')
    
"""
#Ejercicio 10
""" 
numero1 = int(input('Ingrese numero 1: '))
numero2 = int(input('Ingrese numero 2: '))
numero3 = int(input('Ingrese numero 3: '))

lista = [numero1, numero2, numero3]
max = max(lista)
min = min(lista)
avg = round((numero1 + numero2 + numero3) / len(lista),2)

print(f"El numero maximo es:{max}")
print(f"El numero minimo es:{min}" )
print(f"El promedio  es: {avg}")
"""
#Ejercicio 11
""" 
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su PESO en kg: "))
pulsaciones = int(input("Ingrese sus pulsaciones: "))
tension_baja = int(input("Ingrese tension baja: "))
tension_alta = int(input("Ingrese tension alta: "))
plaquetas = float(input("Ingrese numero de plaquetas: "))


if (edad >= 18 and edad <=65) and (peso >= 50 and pulsaciones >= 50 and pulsaciones<=100 ) and (tension_baja >= 50 and tension_baja <=100) and (tension_alta >= 90 and tension_alta <=180) and (plaquetas >=150000):
    print("Paciente Apto")
else:
    print("Paciente no apto")
"""  







