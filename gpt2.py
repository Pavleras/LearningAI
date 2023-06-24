'''
Imagina que estás manejando un sistema para una librería. Tienes libros en diferentes estanterías. Cada estantería tiene un número y cada libro tiene un título y un número de estantería.

Estás recibiendo una serie de consultas que te piden encontrar en qué estantería está un libro por su título.

Para este desafío, debes crear un programa que haga lo siguiente:

Crea un diccionario para representar los libros y sus ubicaciones. Puedes usar cualquier número de libros y estanterías que desees.
Toma una consulta de título de libro como entrada del usuario.
Imprime el número de la estantería donde se encuentra el libro.
Por ejemplo, si tu diccionario es {'El Gran Gatsby': 1, '1984': 2, 'Moby Dick': 3, 'Don Quijote': 1}, y el usuario consulta por '1984', tu programa debe imprimir '2'.
'''
book1 = {'Name': '1984','Publication year':1984,'aisle':1}
book2 = {'Name': 'Un Mundo feliz','Publication year':1990,'aisle':2}
bookStore = [book1, book2]
 
bookName = input('Escribe el nombre del libro que deseas buscar')
found = False

for book in bookStore:
    name = book['Name']
    if (name.lower() == bookName.lower()):
        print('El libro está en el pasillo: ' + str(book['aisle'])) 
        found = True
        break   

if not found:
        print('El libro no se encuentra en la tienda')

