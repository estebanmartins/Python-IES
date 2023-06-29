#Ejercicio 1
"""
frutas ={'Banana': 1.35,'Manzana': 0.80,'Pera':0.85,'Naranja':0.70}

input_fruta = input('ingrese fruta deseada: ').capitalize()
input_kilos = int(input('ingrese kilos: '))
if input_fruta in frutas:
    kilos_fruta_elegida = frutas[input_fruta]* input_kilos #le paso la clave y valor para ser multiplicado por los kilos
    print(f"La fruta elegida es {input_fruta} y su precio por {input_kilos} kg es: {kilos_fruta_elegida}")
    
else:
    print(f'No hay {input_fruta} en nuestro stock de frutas')
""" 


#Ejercicio 2
"""
persona1 = {'Nombre': 'Emilia',
            'Apellido': 'Cabrera',
            'Edad': 23,
            'Email': 'ecabrera@curso.com'
            }

persona2 = {'Nombre': 'Gustavo Andres',
            'Apellido': 'Peralta',
            'Edad': 26,
            'Email': 'gperalta@curso.com'
            }

persona3 = {}
persona3["Nombre"] = input("Ingrese el nombre de la persona: ")
persona3["Apellido"] = input("Ingrese el apellido de la persona: ")
persona3["Edad"] = int(input("Ingrese la edad de la persona: "))
persona3["Email"] = input("Ingrese el email de la persona: ")

# Datos de las tres personas
personas = [persona1, persona2, persona3]

# Imprimo los encabezados de la tabla
print(f"{'Nombre':<15} {'Apellido':<15} {'Edad':<15} {'Email':<15}") 
# :<15 para q sea de 15 caracteres o espacios

#Recorro la lista personas e imprimo sus datos en forma de tabla
for persona in personas:
    nombre = persona["Nombre"]
    apellido = persona["Apellido"]
    edad = persona["Edad"]
    email = persona["Email"]
    
    # Imprimo los datos de cada persona en la tabla
    print(f"{nombre:<15} {apellido:<15} {edad:<15} {email:<15}")
    
"""

#Ejercicio 3

""" 
directorio = "dni;nombre;email;teléfono;descuento\n01234567;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas = directorio.split("\n")
campos = lineas[0].split(";")

directorio_dict = {}

for linea in lineas[1:]:
    datos = linea.split(";")
    cliente_dict = {}
    for i in range(len(campos)):
        cliente_dict[campos[i]] = datos[i]
    dni = datos[0]
    directorio_dict[dni] = cliente_dict

print(directorio_dict)

"""
#Funciones
#Ejercicio 1
"""
input_nombre = input("Ingrese su nombre para ser saludado: ")
def saludar(nombre):
    saludo = f"Hola  {nombre}"
    return saludo

print(saludar(input_nombre))
""" 

#Ejercicio 2
""" 
def factorial(numero):
    if numero < 0:
        return "El número debe ser positivo."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado

numero = int(input("Ingrese un número entero positivo: "))

print(f"El factorial de {numero} es: {factorial(numero)}")

"""

#Ejercicio 3

"""
lista_pares = []
lista_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares(valores):
    for i in valores:                 #recorro con un for la lista de valores
        if i % 2 == 0:                #condicion para saber que numero es para.
            lista_pares.append(i)     #envio los pares hacia la lista_pares

pares(lista_valores)                  #le paso la lista por parametro hacia la funcion
print(f"Lista con valores originales {lista_valores}")
print(f"Lista con valores par {lista_pares}")

""" 

#Ejercicio 4
"""
lista_numeros = [2,4,8,10]   #Lista de numeros


def promedios(numeros):       #Defino funcion y hago dentro la operacion para calcular promedios
    suma = sum(numeros)
    cantidad_elementos = len(numeros)
    promedio = suma / cantidad_elementos
    return promedio           #Retorno la variable promedios que contiene el resultado.


#Hago un print, llamando a la funcion y pasando por parametro la lista de numeros
print(f"El promedio de la lista de numeros {lista_numeros} es {promedios(lista_numeros)}")
    
""" 

#Ejercicio 5
""" 
def calcular_area_circulo(radio):
    area = 3.14159 * radio**2
    return area

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen


radio_circulo = 2.5
altura_cilindro = 5.0

area_circulo = calcular_area_circulo(radio_circulo)
volumen_cilindro = calcular_volumen_cilindro(radio_circulo, altura_cilindro)

print("Área del círculo:", area_circulo)
print("Volumen del cilindro:", volumen_cilindro)
"""

#Ejercicio 6
""" 
def contador_palabras(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    frecuencia = {}  # Diccionario para almacenar la frecuencia de cada palabra

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1  # Si la palabra ya está en el diccionario, incrementa su frecuencia
        else:
            frecuencia[palabra] = 1  # Si la palabra no está en el diccionario, se agrega la palabra con frecuencia 1

    return frecuencia


cadena = input("Ingrese una cadena de texto: ")
resultado = contador_palabras(cadena)
print(resultado)
"""

#Ejercicio 7
""" 
def palabra_mas_repetida(diccionario):
    max_frecuencia = 0  # Variable para almacenar la frecuencia máxima
    palabra_mas_repetida = ''  # Variable para almacenar la palabra más repetida

    # Itera sobre cada par clave-valor en el diccionario
    for palabra, frecuencia in diccionario.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_mas_repetida = palabra

    return (palabra_mas_repetida, max_frecuencia)
diccionario = {'hola': 3, 'mundo': 5, 'programación': 2}

resultado = palabra_mas_repetida(diccionario)
print(resultado)
"""
#Ejercicio 9
"""
def obtener_palabras_comunes(oracion1, oracion2):
    # Divido las oraciones en palabras
    palabras1 = oracion1.split()
    palabras2 = oracion2.split()

    # Lista para almacenar las palabras comunes
    palabras_comunes = []

    # Recorro cada palabra de la primera oración
    for palabra in palabras1:
        # aca verifico si la palabra está presente en la segunda oración
        # y si no se ha agregado previamente a la lista de palabras comunes
        if palabra in palabras2 and palabra not in palabras_comunes:
            # Agregar la palabra a la lista de palabras comunes
            palabras_comunes.append(palabra)

    # Retornar la lista de palabras comunes
    return palabras_comunes

# Solicitar al usuario ingresar las oraciones
oracion1 = input("Ingrese oracion1: ") 
oracion2 = input("Ingrese oracion2: ") 

# Obtener el resultado de las palabras comunes
resultado = obtener_palabras_comunes(oracion1, oracion2)

# Imprimir el resultado
print(resultado)
""" 

""" 
cadena = "nombre=Juan,apellido=Pérez,edad=30"

# Dividir la cadena en pares clave-valor
pares = cadena.split(",")

# Crear un diccionario vacío
diccionario = {}

# Iterar sobre los pares clave-valor y agregarlos al diccionario
for par in pares:
    clave, valor = par.split("=")
    diccionario[clave] = valor

print(diccionario)
""" 
#Ejercicio 10
""" 
def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    inmuebles_en_presupuesto = []

    for inmueble in lista_inmuebles:
        zona = inmueble['zona']
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = inmueble['garaje']
        antiguedad = 2023 - inmueble['año']

        if zona == 'A':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
        elif zona == 'B':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5

        inmueble_con_precio = dict(inmueble)
        inmueble_con_precio['precio'] = precio

        if precio <= presupuesto:
            inmuebles_en_presupuesto.append(inmueble_con_precio)

    return inmuebles_en_presupuesto

"""
my_funcion = lambda x:x*3

print(my_funcion(2))