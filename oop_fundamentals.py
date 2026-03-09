<<<<<<< HEAD
# Task 2.2: OOP Fundamentals - Book Class Example

class Book:
    def __init__(self, title, author, age, summary):
        self.title = title
        self.author = author
        self.age = age
        self.summary = summary

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Age: {self.age} years, Summary: {self.summary}"


# Create 3 Book objects
book1 = Book("1984", "George Orwell", 76, "A dystopian novel about surveillance and control.")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 66, "A novel exploring racial injustice in the American South.")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 101, "A story of wealth, love, and the American dream.")

# Print their details
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
=======
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


# Create three book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Print them
print(book1)
print(book2)
print(book3)
>>>>>>> 368e060317a66df300dcbef080e78f94263404f3
