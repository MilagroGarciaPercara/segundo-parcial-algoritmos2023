class Cola():

    def __init__(self):
        self.__elementos = []

    """agrega elementos a la lista"""

    def arrive(self, value):
        self.__elementos.append(value)

    """devuelve el primer elemento y lo elimina de la cola"""

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    """devuelve el tamaño de la cola?"""

    def size(self):
        return len(self.__elementos)

    """si hay elementos en la cola devuelve el primer elemento de la cola sin eliminarlo/"""

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    """si la cola no esta vacia mueve el primer elemento al final"""

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux
