class Library: # handles the Library functionalities
    num_of_books = 7
    
    def __init__(self,books):
        self.books = books

    def add_book(self,bookName):
        self.books.append(bookName)
        self.num_of_books += 1
    def show_books(self,books):
        print(self.books)

books = ["In Search of Lost Time","One Hundred Years of Solitude","The Great Gatsby","Hamlet","The Divine Comedy","Crime and Punishment","To The Light House"]

lib = Library(books)




def main(): # the program structure
    # printing controls to access library functionalities.
    print("Press J to show the books list.")
    print("Press K to add a book")
    print("Press I for total number of books")
    # asking user response.
    userResponse = input()

    # giving the user specified functionality based on response
    if(userResponse == "J"):
        lib.show_books(books)
    elif(userResponse == "K"):
        bookName = input("Enter the name of the book which you want to enter.")
        lib.add_book(bookName)
        print(f"The book {bookName} is added to the library!")
        # print(lib.books) for debugging purposes.
    elif(userResponse == "I"):
        print(lib.num_of_books)


isRunning = True


while isRunning: # this loop controls the structure
    main()
    userResponse1 = input("Do you want help in something else? Press Y for yes and N for no")
    if(userResponse1 != "Y"):
        print("Goodbye!")
        isRunning = False


