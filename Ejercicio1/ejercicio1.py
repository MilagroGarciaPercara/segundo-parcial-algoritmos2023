"""1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero."""

from arbol_binario import BinaryTree, NodeTree

arbolnombre = BinaryTree ()
arbolnumero = BinaryTree ()
arboltipo = BinaryTree () 

listaPokemones = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
    {"nombre": "Totodile", "numero": 158, "tipo": ["Agua"]},
    {"nombre": "Breloom", "numero": 286, "tipo": ["Planta", "Lucha"]},
    {"nombre": "Lucario", "numero": 448, "tipo": ["Lucha", "Acero"]},
    {"nombre": "Axew", "numero": 610, "tipo": ["Dragón"]},
    {"nombre": "Froakie", "numero": 656, "tipo": ["Agua"]},
    {"nombre": "Rockruff", "numero": 744, "tipo": ["Roca"]},
    {"nombre": "Sobble", "numero": 816, "tipo": ["Agua"]},
    {"nombre": "Yamper", "numero": 835, "tipo": ["Eléctrico"]},
    {"nombre": "Wooloo", "numero": 831, "tipo": ["Normal"]},
    { 'nombre': 'jolteon', 'numero': 135, 'tipo': ['Eléctrico'] },
    { 'nombre': 'lycanroc', 'numero': 745, 'tipo': ['Roca'] },
    { 'nombre': 'tyrantrum', 'numero': 697, 'tipo': ['Roca', 'Dragón'] }
]

#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
for pokemon in listaPokemones:
    nombre = pokemon ['nombre']
    numero = pokemon ['numero']
    tipo = pokemon['tipo']

    arbolnombre.insert_node (nombre, pokemon)
    arbolnumero.insert_node (numero,pokemon)
    arboltipo.insert_node (tipo, pokemon)

#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
def busquedaProximidad(node: NodeTree):
    if node.value.find('bul'.lower()) != -1:
        print(node.other_values)
arbolnombre.inorden(busquedaProximidad)
print('Pokemones que contienen "bul"')
print(arbolnumero.search(135).other_values)

#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; 
def busquedaTipos(node: NodeTree):
    if 'roca' in node.value:
        print(node.other_values.get('nombre')) 
arboltipo.inorden(busquedaTipos)

#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

def imprimirPokemon(node:NodeTree):
    print(node.other_values)
print('arbol ascendente por número')    
arbolnumero.inorden(imprimirPokemon)
print('arbol ascendente por nombre')
arbolnombre.inorden(imprimirPokemon)
print('arbol por nivel por nombre')
arbolnombre.by_level(imprimirPokemon)

#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;

print('Pokemones buscados')
print(arbolnombre.search('lycanroc').other_values)
print(arbolnombre.search('tyrantrum').other_values)
print(arbolnombre.search('jolteon').other_values)

#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

def countTipo(node: NodeTree, value):
    if value in node.value:
        return 1
    else:
        return 0

print(arboltipo.count('acero', countTipo))


