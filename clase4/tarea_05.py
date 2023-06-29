#Ejercicio 1
"""     
cadena = input("Ingrese su cadena: ")

es_heterograma = True

for i in range(len(cadena)):
    for j in range(i+1, len(cadena)):
        if cadena[i] == cadena[j]:
            es_heterograma = False
            break

if es_heterograma:
    print("Es un heterograma")
else:
    print("No es un heterograma")
"""


#Ejercicio 2

""" 
fecha_cadena = '3/30/20'

# Dividir la cadena en día, mes y año
mes, dia, anio = fecha_cadena.split('/')

# Ajustar el formato del día
if len(dia) == 1:
    dia = '0' + dia

# Ajustar el formato del mes
if len(mes) == 1:
    mes = '0' + mes

# Ajustar el formato del año
if len(anio) == 2:
    anio = '20' + anio

# Construir la nueva cadena de fecha
fecha_nueva_cadena = f'{dia}-{mes}-{anio}'

print(fecha_nueva_cadena)
"""


#Ejercicio 3
""" 
numeros_loteria = input('Ingrese los 6 numeros del boleto ganador :')

lista_ordenada = sorted(numeros_loteria)

print(lista_ordenada)
"""

#Ejercicio 4
""" 
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(f"Lista original: {lista1}")

lista1.reverse()

print(f"Lista ordenada de mayor a menor: {lista1}")
"""


#Ejercicio 5

"""
palabra= input('Ingrese una palabra: ').lower()

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for i in palabra:
    if i == 'a':
        contador_a +=1
    elif i == 'e':
        contador_e +=1
    elif i == 'i':
        contador_i +=1
    elif  i == 'o':
        contador_o +=1
    elif  i == 'u':
        contador_u +=1

print(f"Cantidad de letras a : {contador_a}")
print(f"Cantidad de letras e : {contador_e}")
print(f"Cantidad de letras i : {contador_i}")
print(f"Cantidad de letras o : {contador_o}")
print(f"Cantidad de letras u : {contador_u}")

""" 



#Ejercicio 6

""" 
numeros = []

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    
    if num == 0:
        break
    
    numeros.append(num)

numeros.sort(reverse=True)

print("Números ingresados en orden descendente:")

print(numeros)
"""

#Ejercicio 7

""" 

lista_frase = input("Ingrese una oracion: ").lower().split()

print(f"Su frase se almaceno en la lista de esta forma: {lista_frase}")

cant_caracteres = int(input("Cuantos caracteres tiene la palabra buscada ? ingrese num del 1-10: "))

lista2 = []

for i in lista_frase:
    
    if cant_caracteres == len(i):
        lista2.append(i)

print(lista2)

"""


#Ejercicio 8


"""
# Lista de asignaturas
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

diciembre = []
marzo = []
aprobadas = []

# Crear una copia de la lista de materias
materias_copia = materias[:]

# Solicitar notas y eliminar materias aprobadas
for materia in list(materias_copia):
    nota = float(input(f"Ingrese la nota para {materia}: "))
    
    if nota <= 4:
        marzo.append(materia)
    elif nota < 6:
        diciembre.append(materia)
    else:
        aprobadas.append(materia) 
        materias.remove(materia)

print("Asignaturas aprobadas:")
print(materias)

# Mostrar las asignaturas a rendir en diciembre
print("Asignaturas a rendir en diciembre:")
print(diciembre)

# Mostrar las asignaturas a rendir en marzo
print("Asignaturas a rendir en marzo:")
print(marzo)
""" 


#Ejercicio 9
"""
palabras = []

for i in range(5):
    palabra = input("Ingrese una palabra en minúsculas: ").lower()
    palabras.append(palabra)
    
print(f"Lista original: {palabras}")

# Creo otra lista con las palabras en mayúsculas usando lista de comprensión
palabras_mayusculas = [palabra.upper() for palabra in palabras]

print(f"Lista en mayusculas: {palabras_mayusculas}")
""" 
# palabras_mayusculas = []
# for palabra in palabras:
#     palabras_mayusculas.append(palabra.upper())


#Ejercicio 10
# Pedir al usuario que ingrese los vectores separados por comas
vector1_str = input("Ingrese vector 1 (4 elementos separados por comas): ").split(",")
vector2_str = input("Ingrese vector 2 (4 elementos separados por comas): ").split(",")

# Convertir los elementos de las listas en enteros
vector1 = [int(elemento) for elemento in vector1_str]
vector2 = [int(elemento) for elemento in vector2_str]

# Realizar el producto escalar 
producto_escalar = sum(vector1[i] * vector2[i] for i in range(len(vector1)))

print(f"El producto escalar es: {producto_escalar}")
