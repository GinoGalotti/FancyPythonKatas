from exceptions import NotValidElementError

class LinkedList():
    def __init__(self, firstElement=None):
        if not isinstance(firstElement, Element):
            raise NotValidElementError("First element of the list have to be of class Element (and subclasses)")
        else:
            self.firstElement = firstElement
            self.number_elements = 1 if firstElement else 0
            # Not part of the canonical ListElement but hell, SO USEFUL!
            # Although, if you need it, probably LinkedList is not your structure

    def add(self, number):
        element = Element(number)
        

    def add_element(self, element):



class Element():
    def __init__(self, number=0, next=None):
        self.number = number
        self.next = next

    def __str__(self):
        return str(self.number)

    def add_next(self, element):
        if isinstance(element, Element):
            self.next = element
        else:
            raise NotValidElementError("This linked list only accept elements of class Element (and subclasses)")

