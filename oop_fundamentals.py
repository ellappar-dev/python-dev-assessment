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
