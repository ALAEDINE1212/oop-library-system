# test_library.py
import unittest
from library_system import Book, Member


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Create standard test objects before each test runs
        self.book = Book("Clean Code", "B771", "Robert Martin")
        self.member = Member("Alice Smith", "M202")

    def test_polymorphism_output(self):
        # Test if the polymorphic overridden method functions as expected
        self.assertIn("Robert Martin", self.book.get_details())

    def test_borrowing_encapsulation(self):
        # Test if borrowing logic modifies encapsulated properties accurately
        success = self.member.borrow_item(self.book)
        self.assertTrue(success)
        self.assertTrue(self.book.is_borrowed)
        self.assertEqual(self.member.get_borrowed_count(), 1)


if __name__ == "__main__":
    unittest.main()
