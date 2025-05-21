# pila.py
class Nodo:
    """Clase para representar un nodo en la pila."""

    def __init__(self, valor):
        """Inicializa un nodo con un valor y un puntero al siguiente nodo."""
        self.valor = valor
        self.siguiente = None

class Pila:
    """Clase para representar una estructura tipo pila (stack)."""

    def __init__(self):
        """Inicializa una pila vacía."""
        self.tope = None         
        self.contador = 0        
        

    def push(self, item):
        """Agrega un elemento al tope de la pila."""
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.contador += 1


    def pop(self):
        """
        Remueve y retorna el elemento del tope de la pila.
        Retorna None si la pila está vacía.
        """
        if self.tope is not None:
            valor = self.tope.valor
            self.tope = self.tope.siguiente
            return valor
        return None

    def peek(self):
        """
        Retorna el elemento en el tope de la pila sin removerlo.
        Retorna None si la pila está vacía.
        """
        if self.tope is not None:
            return self.tope.valor
        return None

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return self.tope is None

    def size(self):
        """Retorna el tamaño actual de la pila."""
        return self.contador
