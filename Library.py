class Library:
    list = []
    unique_id= 100

    @classmethod
    def entry_book(cls,book):
        cls.list.append(book)

    @classmethod
    def Rent_book_by_id(self,id):
        for book in self.list:
            if book.id == id:
                return book

    @classmethod
    def view_all_book(self):
        print("--Availble Books--")
        for book in Library.list:
            status = "Available" if book.check else "Booked"
            print(f"ID: {book.id} Title: {book.title} Author: {book.author} Status: {status}")

    


class Book:

    def __init__(self,title,author,check=True):
        self.id=Library.unique_id
        Library.unique_id +=1
        self.title=title
        self.author=author
        self.check=check
        Library.entry_book(self)

    def rent_book(self):
        if self.check: self.check=False
        else: print("Its Not Available, Try again a few moment, Tnq u")
    

    def return_book(self):
        if not self.check: self.check=True
        else: print("Its Available, U Can Rent It")
    
    def view_book_info(self):
        check = "Available" if self.check else "Booked"
    


Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")
Book("Didar_Ahmed_Belal", "Belal")


while True:
    print("=== Library Menu ===")
    print("1. View All Books")
    print("2. Rent Book")
    print("3. Return Book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice=='1':
        Library.view_all_book()
    elif choice == '2':
        id = int(input("Enter Book ID to rent: "))
        book = Library.Rent_book_by_id(id)
        if book:
            book.rent_book()
        else:
            print("Ivalid Book ID: ")
    elif choice=='3':
        ID = int(input("Enter Book ID to rent: "))
        book = Library.Rent_book_by_id(id)
        if book:
            book.return_book()
        else:
            print("Invalid Book ID.")
    elif choice =='4':
        print("Arigato Gozaimas!")
        break
    else:
        print("Are U Kidding Me ?????")
       