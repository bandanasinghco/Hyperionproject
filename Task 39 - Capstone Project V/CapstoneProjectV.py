import sqlite3

db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()  # Get a cursor object


# delete function to delete the selected book
def delete_book():
    cursor.execute('''
        SELECT * FROM books
        ''')

    data = cursor.fetchall()
    print(data, "\n")

    id_select = int(input("Please select the id of the book you'd like to delete: "))

    cursor.execute('''
                    DELETE FROM books WHERE id=?''', (id_select,))

    print("Data deleted successfully")
    db.commit()


# update function to update the book details
def update_book():
    cursor.execute('''
    SELECT * FROM books
    ''')

    data = cursor.fetchall()
    print(data, "\n")

    id_select = int(input("Please select the id of the book you'd like to edit: "))

    edit_choice = input("Whats aspect would you like to edit (title, author, qty): ").lower()

    if edit_choice == 'title':
        new_title = input("Please enter the new title of the book: ")

        cursor.execute('''
                       UPDATE books SET title=? WHERE id=?''', (new_title, id_select,))
        print("Title of the book is updated successfully")

    elif edit_choice == 'author':
        new_author = input("Please enter the new author of the book: ")

        cursor.execute('''
                      UPDATE books SET author=? WHERE id=?''', (new_author, id_select,))

        print("\n Author of the book is updated successfully")

    elif edit_choice == 'qty':

        new_qty = int(input("Please enter the new quantity of the book"))

        cursor.execute('''
                       UPDATE books SET qty=? WHERE id=?''', (new_qty, id_select,))
        print("Quantity of book updated successfully")
    db.commit()


# search for book function
def view_book():
    id_check = int(input("Please enter the id of the book you'd like to search: "))

    cursor.execute('''
    SELECT * FROM books WHERE id=?''', (id_check,))
    data = cursor.fetchone()
    print("View book is here: ")
    print(data)


# creating function to add books
def add_book() -> object:
    id = int(input("Enter the id of this book entry: "))
    title = input("Enter the title of the book entry: ")
    author = input("Enter the author of the book entry: ")
    qty = int(input("Enter the quantity of books in stock: "))

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', (id, title, author, qty))

    print("New Book added successfully")
    db.commit()


# create books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')

print('database created!')
db.commit()

# inserts all rows value into books table
id_one = 3001
title_one = 'A Tale of Two Cities'
author_one = 'Charles Dickens'
qty_one = 30

id_two = 3002
title_two = "Harry Potter and the Philosopher's Stone"
author_two = 'J.K Rowling'
qty_two = 40

id_three = 3003
title_three = 'The Lion, the Witch and the Wardrobe'
author_three = 'C.S. Lewis'
qty_three = 25

id_four = 3004
title_four = 'The Lord of the Rings'
author_four = 'J.R.R Tolkien'
qty_four = 37

id_five = 3005
title_five = 'Alice in Wonderland'
author_five = 'Lewis Carroll'
qty_five = 12

books_ = [(id_one, title_one, author_one, qty_one), (id_two, title_two, author_two, qty_two),
          (id_three, title_three, author_three, qty_three),
          (id_four, title_four, author_four, qty_four), (id_five, title_five, author_five, qty_five)]

cursor.executemany('''
INSERT INTO books(id, title, author, qty) VALUES(?,?,?,?)
''', books_)

print("Entry added")
db.commit()


# This is the user_choice which will be promoted with few option, see print line
def user_choice():
    print("Welcome to the book clerk ")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")


user_choice()
loop = True
while loop:
    print()
    user_choice = int(input("Enter the number corresponding to the option that you would like to action: "))

    if user_choice == 1:  # adds the book
        add_book()

    elif user_choice == 2:  # update the book
        update_book()

    elif user_choice == 3:  # user will be able to view book via id
        view_book()

    elif user_choice == 4:  # deletes the selected book
        delete_book()

    elif user_choice == 0:  # quit option
        print("Program Terminated! Try again to view book")
        break

    else:
        print("Incorrect input - Please try again.")
db.commit()