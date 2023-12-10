
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOD': 'Objective Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

#largo
print(len(diccionario))

#Acceder a un elemento (key) 
print(diccionario['IDE'])
print(diccionario.get('OOD'))

#Modificando un elemento 
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#recorrer los elementos
for termino, valor in diccionario.items(): 
    print(termino,valor)
#Solo termino
for termino in diccionario.keys():
    print(termino)
#Que nos regrese solo el valor
for valor in diccionario.values():
    print(valor)

#Comprobar si esta el elemento en el diccionario
print('IDE' in diccionario)

#Agregar elemento al diccionario
diccionario['PK'] = 'Primary Key'
print (diccionario)

#Elimar un elemento del diccionario 
diccionario.pop('DBMS')
print(diccionario)

#Limpiar diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario
print(diccionario)

