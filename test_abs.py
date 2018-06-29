"""
Public.

Mondule.
"""


class Instrumento:
    """Instrumento."""

    def __init__(self, precio):
        """Instrumento."""
        self.precio = precio

    def tocar(self):
        """Instrumento."""
        print("Estamos tocando musica")

    def romper(self):
        """Instrumento."""
        print("Eso lo pagas tu")
        print("Son", self.precio, "$$$")


class Bateria(Instrumento):
    """Instrumento."""

    def tocar(self):
        """Instrumento."""
        super().tocar()
        print("Estamos tocando bateria")

    def tronar(self):
        """Instrumento."""
        print("Estamos tronando")


class Guitarra(Instrumento):
    """Instrumento."""

    pass


bat = Bateria(2222)
bat.tocar()
bat.romper()
bat.tronar()
bat.tronar()
