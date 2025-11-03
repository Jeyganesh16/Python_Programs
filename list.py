def show_menu():
    print("Book Menu")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.Display Book")
    print("4.Sort Book")
    print("5.Exit")

def add_book(book_list):
    book = input("Enter the book name to be add")
    book_list.append(book)
    print(book,"has been added successfully")
def remove_book(book_list):
    book = input("Enter the book name to be remove")
    if book in book_list:
        book_list.remove(book)
        print(book,"has been remove from the list")
    else:
        print("Book not present in the list")
def display_book(book_list):
    if book_list:
        print("Your Book List")
        for i,book in enumerate(book_list,start=1):
            print(i,".",book)
    else:
        print("Your Book list is empty")
    
def sort_book(book_list):
    book_list.sort()
    print("Your book list has been sorted alphabetically")

book_list=[]
while True:
    show_menu()
    choice = input("Enter your choice 1 to 5")

    if choice == "1":
        add_book(book_list)
        #print(book_list)
    elif choice == "2":
        remove_book(book_list)
        #print(book_list)
    elif choice == "3":
        display_book(book_list)
    elif choice == "4":
        sort_book(book_list)
    elif choice == "5":
        print("Exiting program:Goodbye!")
        break
    else:
        print("Invalid choice: Please choose 1 to 5")



    
