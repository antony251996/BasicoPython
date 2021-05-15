nombre = input('¿Cual es tu nombre? : ')

#Colocar el texto en mayusculas
print(nombre.upper())

#Quita los espacios en blanco al inicio y al final
print(nombre.strip())

#Colocar la primera letra en mayusculas
print(nombre.capitalize())

#Colocar el texto en minusculas
print(nombre.lower())

#Reemplazar un caracter por otro
print(nombre.replace('o','a'))

#Indices: primer caracter siempre empieza en cero
print(nombre[0])

#Indices
print(nombre[0:3])

print(nombre[::2])

#Cantidad de caracteres
print(len(nombre))