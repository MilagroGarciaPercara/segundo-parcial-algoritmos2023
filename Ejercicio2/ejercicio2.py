"""2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8."""

from grafo import Graph

grafo = Graph(False)
datos = [
    {"Personaje A": "Luke Skywalker", "Personaje B": "Han Solo", "Episodios Juntos": 3},
    {"Personaje A": "Han Solo", "Personaje B": "Chewbacca", "Episodios Juntos": 4},
    {"Personaje A": "Princess Leia", "Personaje B": "Han Solo", "Episodios Juntos": 3},
    {"Personaje A": "Obi-Wan Kenobi", "Personaje B": "Yoda", "Episodios Juntos": 2},
    {"Personaje A": "Anakin Skywalker", "Personaje B": "Obi-Wan Kenobi", "Episodios Juntos": 3},
    {"Personaje A": "Darth Vader", "Personaje B": "Emperor Palpatine", "Episodios Juntos": 2},
    {"Personaje A": "Padmé Amidala", "Personaje B": "Anakin Skywalker", "Episodios Juntos": 3},
    {"Personaje A": "Rey", "Personaje B": "Finn", "Episodios Juntos": 2},
    {"Personaje A": "Poe Dameron", "Personaje B": "BB-8", "Episodios Juntos": 2},
    {"Personaje A": "Mace Windu", "Personaje B": "Qui-Gon Jinn", "Episodios Juntos": 1},
    {"Personaje A": "Luke Skywalker", "Personaje B": "Darth Vader", "Episodios Juntos": 3},
    {"Personaje A": "Yoda", "Personaje B": "Obi-Wan Kenobi", "Episodios Juntos": 2},
    {"Personaje A": "Boba Fett", "Personaje B": "Darth Vader", "Episodios Juntos": 1},
    {"Personaje A": "C-3PO", "Personaje B": "Princess Leia", "Episodios Juntos": 1},
    {"Personaje A": "Rey", "Personaje B": "Kylo Ren", "Episodios Juntos": 2},
    {"Personaje A": "Chewbacca", "Personaje B": "Han Solo", "Episodios Juntos": 4},
    {"Personaje A": "R2-D2", "Personaje B": "C-3PO", "Episodios Juntos": 2},
    {"Personaje A": "BB-8", "Personaje B": "Poe Dameron", "Episodios Juntos": 2}
]

vertices = [
    "Luke Skywalker", "Han Solo", "Chewbacca", "Princess Leia", "Obi-Wan Kenobi", "Yoda", "Anakin Skywalker", "Darth Vader","Emperor Palpatine", "Padmé Amidala", "Rey", "Finn", "Poe Dameron", "Mace Windu", "Qui-Gon Jinn", "Boba Fett", "C-3PO", "Kylo Ren", "R2-D2", "BB-8"
]

for vertice in vertices:
    grafo.insert_vertice(vertice)

#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
# y d)*

for arista in datos: 
    grafo.insert_arist(arista.get("Personaje A"), arista.get("Personaje B"), arista.get("Episodios Juntos"))

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

bosque=grafo.kruskal()

print(bosque)

kruskal = bosque[0]

if kruskal.find("Yoda") != -1:
    print("El arbol contiene a Yoda")
else:
    print("El arbol no contiene a Yoda")

#c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.


