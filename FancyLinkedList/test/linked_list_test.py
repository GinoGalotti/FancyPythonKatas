import unittest
from random import shuffle

from FancyLinkedList.exceptions import ElementIsNotANumber
from FancyLinkedList.linked_list import LinkedList


# Assertions are going to be slightly different depending on the amount of logging vs simplicity required.
# Showing both examples, but the ideal scenario is adapting it to each team needs / wants.
class LinkedListTest(unittest.TestCase):
    # This is the example of "I want overdose of mesages when something fail"
    def test_create_empty_list(self):
        test_list = LinkedList()

        self.assertFalse(test_list.get_first(),
                         "First element should be None instead of {}".format(test_list.first_element))
        self.assertFalse(test_list.get_last(),
                         "Last element should be None instead of {}".format(test_list.last_element))
        self.assertEqual(str(test_list), "[]", "Expecting empty list, but found {}".format(str(test_list)))

    # This is the "I don't care about messages as long as the test case is simple approach
    def test_add_to_empty(self):
        test_list = LinkedList()

        test_list.add_sorted(1)
        assert test_list.get_first().is_number(1)
        assert test_list.get_last().is_number(1)
        assert str(test_list) == "[1]"

    # This is the example of "I want overdose of mesages when something fail"
    def test_add_string(self):
        test_list = LinkedList()

        with self.assertRaises(ElementIsNotANumber):
            test_list.add_sorted("Not a number")

        self.assertFalse(test_list.get_first(),
                         "First element should be None instead of {}".format(test_list.first_element))
        self.assertFalse(test_list.get_last(),
                         "Last element should be None instead of {}".format(test_list.last_element))
        self.assertEqual(str(test_list), "[]", "Expecting empty list, but found {}".format(str(test_list)))

    def test_add_minimum(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(3)

        test_list.add_sorted(1)
        assert test_list.first_element.is_number(1)
        assert test_list.last_element.is_number(4)
        assert str(test_list) == "[1, 3, 4]"

    def test_add_negative(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(3)

        test_list.add_sorted(-2)
        assert test_list.first_element.is_number(-2)
        assert test_list.last_element.is_number(4)
        assert str(test_list) == "[-2, 3, 4]"

    def test_add_maximum(self):
        test_list = LinkedList()
        test_list.add_sorted(0)
        test_list.add_sorted(2)

        test_list.add_sorted(5)
        assert test_list.first_element.is_number(0)
        assert test_list.last_element.is_number(5)
        assert str(test_list) == "[0, 2, 5]"

    def test_add_in_the_middle(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(25)

        test_list.add_sorted(3)
        assert test_list.first_element.is_number(2)
        assert test_list.last_element.is_number(25)
        assert str(test_list) == "[2, 3, 4, 25]"

    def test_add_duplicate(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)

        test_list.add_sorted(2)
        assert test_list.first_element.is_number(2)
        assert test_list.last_element.is_number(4)
        assert str(test_list) == "[2, 2, 4]"

    def test_add_duplicate_to_last(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)

        test_list.add_sorted(4)
        assert test_list.first_element.is_number(2)
        assert test_list.last_element.is_number(4)
        assert str(test_list) == "[2, 4, 4]"

    # Let's try a little bit of the performance
    def test_add_a_lot(self):
        test_list = LinkedList()

        shuffled_list_100_elements = range(100)
        shuffle(shuffled_list_100_elements)

        sorted_list_100_elements = range(100)

        for i in shuffled_list_100_elements:
            test_list.add_sorted(i)

        assert test_list.first_element.is_number(0)
        assert test_list.last_element.is_number(99)
        self.assertEqual(str(test_list), str(range(100)),
                         "Expecting {}, but got {}".format(str(sorted_list_100_elements), str(test_list)))

    # This is extra. Specification doesn't say anything about deleting, so it's not as complete. Just wanted to check
    # that I haven't screwed it.

    def test_remove_element(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(3)

        assert test_list.remove_element(3)
        assert str(test_list) == "[2, 4]"

    def test_add_after_removing(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(3)
        test_list.remove_element(3)

        test_list.add_sorted(3)
        assert str(test_list) == "[2, 3, 4]"

    def test_remove_non_existing(self):
        test_list = LinkedList()
        test_list.add_sorted(4)

        assert not test_list.remove_element(2)
        assert str(test_list) == "[4]"

    def test_remove_duplicate(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(3)
        test_list.add_sorted(3)

        assert test_list.remove_element(3)
        assert str(test_list) == "[2, 3, 4]"

    def test_remove_first(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(3)

        assert test_list.remove_element(2)
        assert str(test_list) == "[3, 4]"

    def test_remove_last(self):
        test_list = LinkedList()
        test_list.add_sorted(4)
        test_list.add_sorted(2)
        test_list.add_sorted(3)

        assert test_list.remove_element(4)
        assert str(test_list) == "[2, 3]"

    def test_remove_empty(self):
        test_list = LinkedList()

        assert not test_list.remove_element(0)


if __name__ == '__main__':
    unittest.main()
