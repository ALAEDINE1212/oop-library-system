# library_system.py

# 1. Parent Class (Demonstrating Encapsulation)
class Item:
    def __init__(self, title: str, item_id: str):
        self.title = title  # Public property
        self._item_id = item_id  # Protected property (Encapsulation)
        self.is_borrowed = False

    def get_details(self) -> str:
        return f"Generic Library Item: {self.title}"


# 2. Child Class (Demonstrating Inheritance & Polymorphism)
class Book(Item):
    def __init__(self, title: str, item_id: str, author: str):
        super().__init__(title, item_id)  # Inherits from Item parent class
        self.author = author

    # Overriding the parent class method (Polymorphism)
    def get_details(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title} by {self.author} [{status}]"
