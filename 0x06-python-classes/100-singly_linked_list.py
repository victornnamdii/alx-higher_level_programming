#!/usr/bin/python3
""" defines a class node and singlylinkedlist"""


class Node:
    """defines the node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """gets the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ets the next node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts node in the correct order"""
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data
                    < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """defines the print representation of the list"""
        tmp = self.__head
        values = []
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
