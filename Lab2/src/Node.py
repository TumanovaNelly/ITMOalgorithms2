from typing import Optional


class Node:
    # ______ неизменяемые снаружи поля ______ #
    @property
    def value(self): return self.__value

    @property
    def size(self): return self.__size

    # _______ изменяемые снаружи поля _______ #
    right: Optional['Node'] = None
    left: Optional['Node'] = None
    parent: Optional['Node'] = None

    # _______________ методы ________________ #
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__size = 1

    def update_size(self):
        self.__size = (self.left.size if self.left is not None else 0) + \
                      (self.right.size if self.right is not None else 0) + 1
