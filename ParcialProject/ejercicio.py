# Conversión de Enteros, Decimales y Cadenas.
entero = 5
decimal = 3.14
cadena = "10"

# Convertir cadena a entero
cadena_a_entero = int(cadena)
# Convertir entero a cadena
entero_a_cadena = str(entero)
# Convertir decimal a entero
decimal_a_entero = int(decimal)

print(cadena_a_entero, entero_a_cadena, decimal_a_entero)

#Multilíneas de cadenas.
multilinea = """Esto es una cadena
que ocupa varias líneas
en Python."""
print(multilinea)

#Función len().
cadena = "Hola Mundo"
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)

#Sub cadenas

#Obtener los primeros n caracteres de una cadena.
primeros_n = cadena[:5]  # Primeros 5 caracteres
print("Primeros 5 caracteres:", primeros_n)

#Obtener los caracteres de en medio de una cadena.
en_medio = cadena[1:4]  # Caracteres del índice 1 al 4
print("Caracteres en medio:", en_medio)

#Obtener los últimos n caracteres de una cadena.
ultimos_n = cadena[-5:]  # Últimos 5 caracteres
print("Últimos 5 caracteres:", ultimos_n)

#Funciones
texto = "Hola Mundo"
#Funciónes upper().
print("Texto en mayúsculas:", texto.upper())
#Función lower().
print("Texto en minúsculas:", texto.lower())

#Multilíneas de cadenas de caracteres.
cadena_multilinea = """Esta es otra cadena
que también es multilínea.
¡Genial!"""
print(cadena_multilinea)

#Función strip().
cadena_con_espacios = "   Hola Mundo   "
print("Cadena sin espacios:", cadena_con_espacios.strip())

#Función replace().
cadena_reemplazo = "Hola Mundo"
nueva_cadena = cadena_reemplazo.replace("Mundo", "Python")
print("Cadena reemplazada:", nueva_cadena)

#Función split().
cadena_split = "Hola, Mundo, Python"
lista = cadena_split.split(", ")
print("Lista después de split:", lista)

#Formato de cadenas F-String.
nombre = "David"
edad = 23
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
