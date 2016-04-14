from exceptions import NotValidElementError, ElementIsNotANumber


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
        # Improving performance when adding big numbers
        elif number >= self.last_element.number:
            self.last_element.next_element = new_element
            self.last_element = new_element
        else:
            element_to_check = self.first_element

            # Case this should be first
            if self.is_this_my_place(number, element_to_check):
                new_element.next_element = element_to_check
                self.first_element = new_element

            else:
                while True:
                    if self.is_last_element(element_to_check):
                        element_to_check.next_element = new_element
                        self.last_element = new_element
                        break
                    if self.is_the_next_my_place(number, element_to_check):
                        new_element.next_element = element_to_check.next_element
                        element_to_check.next_element = new_element
                        break
                    element_to_check = element_to_check.next_element

    def is_this_my_place(self, number, element):
        return number <= element.number

    def is_the_next_my_place(self, number, element):
        return number <= element.next_element.number

    def is_last_element(self, element):
        return not element.next_element

    def get_first(self):
        return self.first_element

    def get_last(self):
        return self.last_element

    # Really useful for testing purposes, although
    # Return the list in the format: "[1, 2, 3, 3 ]"
    def __str__(self):
        opener = "["
        separator = ", "
        closer = "]"

        if self.is_empty():
            return (opener + closer)

        string = opener + str(self.first_element)
        element_to_check = self.first_element

        while True:
            if not element_to_check.next_element:
                break
            string = "{0}{1}{2}".format(string, separator, element_to_check.next_element)
            element_to_check = element_to_check.next_element

        return (string + closer)


    # As specified in Java LinkedList, it won' return an error if the element is not present
    # Return True when something is deleted
    def remove_element(self, number):
        if self.is_empty():
            return False
        if number > self.last_element.number:
            return False
        if self.first_element.number == number:
            if not self.first_element.next_element:
                self.last_element = None
            self.first_element = self.first_element.next_element
            return True

        element_to_check = self.first_element

        while True:
            if not element_to_check.next_element:
                return False
            if element_to_check.next_element.number > number:
                return False
            if element_to_check.next_element.number == number:
                # Python should kill it when nothing is referring it
                element_to_check.next_element = element_to_check.next_element.next_element
                return True
            element_to_check = element_to_check.next_element

    def is_empty(self):
        return not self.first_element and not self.last_element

class Element():
    def __init__(self, number=0, next=None):
        if not isinstance(number, int):
            raise ElementIsNotANumber("Element '{}' is not a number".format(number))
        self.number = int(number)  # This will raise an Exception adding a non integer
        self.next_element = next

    def __str__(self):
        return str(self.number)

    def is_number(self, number):
        return self.number == number
