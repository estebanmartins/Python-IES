#Ejercicio 1
"""
nombre = input('Ingrese su nombre: ')
repetir = int(input('Ingrese la cantidad de veces que desea repetir el nombre: '))
resultado = (nombre + '\n') * repetir
print(f"El resultado  es:\n{resultado}", end="")
""" 
#Ejercicio 2
"""
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
resultado = f"{apellido}, { nombre}"
print(f"Nombre completo: {resultado}")
""" 
#Ejercicio 3
""" 
ruta = input("Ingrese ruta: ").replace(" ", "").strip()   #'//1.1.1.1/eoi/python'
indice = ruta.index('1/') + 1

parte1 = 'Host=' + ruta[2:indice]
parte2 =';Path='  + ruta[indice:]
salida= parte1 + parte2

print(f"La salida es: {salida} ")
"""


#Ejercicio 4
""" 
email = input("Ingrese su email :")
antes_arroba = email.index('@')
username = email[:antes_arroba]
correo_modificado = username + "@educ.ar"
print(f"Correo original: {email}")
print(f"Correo Modificado: {correo_modificado}")
"""

#Ejercicio 5
""" 
nif = input("Ingrese los 8 dígitos del NIF: ")

if len(nif) != 8:
    print("El NIF debe tener exactamente 8 dígitos.")
else:
    digitos = "TRWAGMYFPDXBNJZSQVHLCKE"  # Dígitos de control correspondientes a los números del NIF
    numeros = "0123456789"  # Números del NIF

    suma = int(nif[0]) * 128 + int(nif[1]) * 64 + int(nif[2]) * 32 + int(nif[3]) * 16 + int(nif[4]) * 8 + int(nif[5]) * 4 + int(nif[6]) * 2 + int(nif[7]) * 1
    resto = suma % 23
    digito_control = digitos[resto]

    nif_completo = nif + digito_control
    print("NIF con dígito de control:", nif_completo)
"""
#Ejercicio 6
""" 
num = input("Ingrese nro: ")
operacion1 =num
operacion2 =num+num
operacion3 =num+num+num

salida = int(operacion1) + int(operacion2) + int(operacion3)
print(f"{salida} ({operacion1} + {operacion2} + {operacion3})")
"""
#Ejercicio 7
""" 
fecha = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").replace('/',  ',')
fecha_dividida = fecha.split(",")
dia = fecha_dividida[0]
mes = fecha_dividida[1]
anio = fecha_dividida[2]

dia = int(dia)
mes = int(mes)
anio = int(anio)

print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)
""" 
#Ejercicio 8
"""

nombre_producto = input("Ingrese Nombre de Producto: ")
precio_producto = int(input("Ingrese precio del Producto: "))
num_unidades = int(input("Ingrese numero de unidades: "))   

precio_producto = float(num_unidades,4)
print(f"El nombre del producto es {nombre_producto}, el precio es : {precio_producto}, el num de unidades es : {num_unidades}")
""" 
#Ejercicio 9
""" 
productos = input("Ingrese 3 productos y su cantidad: ") #6:huevos, 1:azúcar, 4:latas de pescado
lista_productos = productos.split(",")

producto1 = lista_productos[0]
producto2 = lista_productos[1]
producto3 = lista_productos[2]
print(producto1.replace(":", " "))
print(producto2.replace(":", " "))
print(producto3.replace(":", " "))
"""

#Ejercicio 10
"""
palabra = input("Ingrese una palabra en castellano: ")
vocales = palabra.count('a') + palabra.count('e') + palabra.count('i') + palabra.count('o')+ palabra.count('u') 
operacion = len(palabra) * vocales
print(operacion)

""" 