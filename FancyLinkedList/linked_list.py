from exceptions import NotValidElementError


class LinkedList():
    def __init__(self, first_element=None):
        if first_element and not isinstance(first_element, Element):
            raise NotValidElementError("First element of the list have to be of class Element (and subclasses)")
        else:
            self.first_element = first_element
            # Not part of the canonical ListElement but hell, SO USEFUL!
            # Remember from university, this reduces adding to 0(1) when not ordered. Not it can help us knowing the max!
            # (And optimising when adding big numbers, which is the worst case)
            self.last_element = first_element

    def add_sorted(self, number):
        new_element = Element(number)
        if self.is_empty():
            self.first_element = new_element
            self.last_element = new_element
        else:
            element_to_check = self.first_element

            # Case this should be first
            if self.is_this_my_place(number, element_to_check):
                new_element.next_element = element_to_check
                self.first_element = new_element

            else:
                while True:
                    if self.am_i_the_last(number, element_to_check):
                        element_to_check.next_element = new_element
                        self.last_element = new_element
                    if self.is_the_next_my_place(number, element_to_check):
                        new_element.next_element = element_to_check.next_element
                        element_to_check.next_element = new_element

    def is_this_my_place(self, number, element):
        return number <= element.number

    def is_the_next_my_place(self, number, element):
        return number <= element.next_element.number

    def am_i_the_last(self, number, element):
        return not element.next_element

    def get_first(self):
        return self.first_element

    def get_last(self):
        return self.last_element


def is_empty(self):
    return not self.first_element and not self.last_element

class Element():
    def __init__(self, number=0, next=None):
        self.number = int(number)  # This will raise an Exception adding a non integer
        self.next_element = next

    def __str__(self):
        return str(self.number)
