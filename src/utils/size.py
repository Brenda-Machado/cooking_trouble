"""
Cooking Trouble.

Classe para gerenciar dimensões.

size.py
"""

class Size:
    def __init__(self, width: int, height: int):

        if width <= 0 or height <= 0:
            raise ValueError("Dimensões devem ser positivas")
        
        self._width = int(width)
        self._height = int(height)

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        if value <= 0:
            raise ValueError("Largura deve ser positiva")
        
        self._width = int(value)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        if value <= 0:
            raise ValueError("Altura deve ser positiva")
        
        self._height = int(value)

    def copy(self) -> 'Size':
        return Size(self._width, self._height)

    def scale(self, factor: float) -> 'Size':
        return Size(
            int(self._width * factor),
            int(self._height * factor)
        )

    def __repr__(self) -> str:
        return f"Size({self._width}, {self._height})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Size):
            return False
        
        return self._width == other.width and self._height == other.height

    def __hash__(self) -> int:
        return hash((self._width, self._height))

    def as_tuple(self):
        return (self._width, self._height)
