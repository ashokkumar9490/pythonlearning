class Book:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Number of Pages:", self.number_of_pages)

page1 = Book("The Python program language", "Dock meker",1765)
page2 = Book("The oops concepts", "Jackes domen", 11000)

page1.display_info()
print("\n") 
page2.display_info()
