from typing import Tuple, Optional

from Lab2.src.Node import Node


class Rope:
    # ___________ публичные методы __________ #
    def __init__(self, root: Node = None):
        self.__root = root

    def build(self, word: str):
        """ Построение дерева """
        self.__root = self.__build_recursive(word, 0, len(word))

    def cut_n_paste(self, from_indexes: Tuple[int, int], to_index: int):
        """ Вырезание поддерева и его вставка в другое место """
        self.__root = self.__paste(to_index, self.__cut(*from_indexes))

    def __str__(self):
        result = []
        self.__to_string(self.__root, result)
        return ''.join(result)

    def __getitem__(self, index: int):
        return self.__getitem(self.__root, index).value

    # ___________ приватные методы __________ #
    def __build_recursive(self, word: str, start: int, end: int) -> Optional[Node]:
        if start == end: return None
        mid = (start + end) // 2
        result = Node(word[mid])

        result.left = self.__build_recursive(word, start, mid)
        if result.left is not None: result.left.parent = result

        result.right = self.__build_recursive(word, mid + 1, end)
        if result.right is not None: result.right.parent = result

        result.update_size()
        return result

    def __to_string(self, node, result):
        if node is None: return
        self.__to_string(node.left, result)
        result.append(node.value)
        self.__to_string(node.right, result)

    def __paste(self, start: int, node: Node) -> Node:
        """ Вставка поддерева в дерево """
        if self.__root is None:
            if start == 0:
                self.__root = node
                return node
            else: raise IndexError("Index out of range")

        left_part, right_part = self.__split(self.__root, start)
        return self.__merge(self.__merge(left_part, node), right_part)

    def __cut(self, start: int, end: int) -> Node:
        """ Вырезание поддерева из дерева """
        other, right_part = self.__split(self.__root, end + 1)
        left_part, mid_part = self.__split(other, start)
        self.__root = self.__merge(left_part, right_part)
        return mid_part

    def __getitem(self, node: Node, index: int) -> Node:
        cur_node = node
        cur_index = cur_node.left.size if cur_node.left else 0
        while cur_index != index:
            if cur_index > index:
                cur_node = cur_node.left
                if cur_node is None: raise IndexError("Index out of range")
                cur_index -= (cur_node.right.size if cur_node.right is not None else 0) + 1
            elif cur_index < index:
                cur_node = cur_node.right
                if cur_node is None: raise IndexError("Index out of range")
                cur_index += (cur_node.left.size if cur_node.left is not None else 0) + 1

        self.__splay(cur_node)
        return cur_node

    def __split(self, node: Node, index: int) -> Tuple[Optional[Node], Optional[Node]]:
        """ Разбитие поддерева на поддеревья """
        if index == node.size: return node, None

        cur_node = self.__getitem(node, index)

        left_part = cur_node.left
        cur_node.left = None
        if left_part is not None: left_part.parent = None

        cur_node.update_size()
        return left_part, cur_node

    def __merge(self, left_part: Node, right_part: Node) -> Node:
        """ Слияние двух поддеревьев """
        if left_part is None: return right_part
        if right_part is None: return left_part

        right_part.left = left_part
        left_part.parent = right_part
        right_part.update_size()
        return right_part

    def __splay(self, node: Node):
        """ 'Выворачивание' node наверх в root """
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:  # Zig
                self.__rotate(node)
            elif ((grandparent.right == parent) + (parent.right == node)) % 2 == 0:  # ZigZig
                self.__rotate(parent)
                self.__rotate(node)
            else:  # ZigZag
                self.__rotate(node)
                self.__rotate(node)

        self.__root = node
        return node

    def __rotate(self, node: Node):
        """ Вращение узлов (совмещенное правое и левое) """
        node_old_parent = node.parent
        if node_old_parent is None: return
        node_old_grandparent = node_old_parent.parent

        if node_old_parent.right == node:  # если node - правый сын parent
            node_old_parent.right = node.left
            if node_old_parent.right is not None:
                node_old_parent.right.parent = node_old_parent

            node.left = node_old_parent
        else:  # если node - левый сын parent
            node_old_parent.left = node.right
            if node_old_parent.left is not None:
                node_old_parent.left.parent = node_old_parent

            node.right = node_old_parent
        node_old_parent.parent = node

        node.parent = node_old_grandparent
        if node_old_grandparent is not None:
            if node_old_grandparent.right == node_old_parent:
                node_old_grandparent.right = node
            else:
                node_old_grandparent.left = node

        node_old_parent.update_size()
        node.update_size()
