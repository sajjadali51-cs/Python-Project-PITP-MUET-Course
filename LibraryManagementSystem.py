import datetime

# Book and Member Data (initial sample data)
books = [
    {"id": 1, "title": "Python Basics", "author": "John", "available": True, "borrowed_by": None, "due_date": None},
    {"id": 2, "title": "C++ OOP", "author": "Mark", "available": True, "borrowed_by": None, "due_date": None},
    {"id": 3, "title": "Data Structures", "author": "Alice", "available": True, "borrowed_by": None, "due_date": None}
]

members = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

# Helper functions
def display_all_books():
    print("\n--- All Books ---")
    for b in books:
        print(f"{b['id']}. {b['title']} by {b['author']} - {'Available' if b['available'] else 'Borrowed'}")

def display_available_books():
    print("\n--- Available Books ---")
    for b in books:
        if b['available']:
            print(f"{b['id']}. {b['title']} by {b['author']}")

def display_all_members():
    print("\n--- Members ---")
    for m in members:
        print(f"{m['id']}. {m['name']}")

def search_books():
    keyword = input("Enter book title/author to search: ").lower()
    print("\n--- Search Results ---")
    for b in books:
        if keyword in b['title'].lower() or keyword in b['author'].lower():
            print(f"{b['id']}. {b['title']} by {b['author']} - {'Available' if b['available'] else 'Borrowed'}")

def borrow_book():
    display_all_members()
    mid = int(input("Enter Member ID: "))
    display_available_books()
    bid = int(input("Enter Book ID to borrow: "))
    for b in books:
        if b['id'] == bid and b['available']:
            b['available'] = False
            b['borrowed_by'] = mid
            b['due_date'] = datetime.date.today() + datetime.timedelta(days=7)
            print(f"{b['title']} borrowed successfully! Due date: {b['due_date']}")
            return
    print("Book not available!")

def return_book():
    bid = int(input("Enter Book ID to return: "))
    for b in books:
        if b['id'] == bid and not b['available']:
            b['available'] = True
            b['borrowed_by'] = None
            b['due_date'] = None
            print(f"{b['title']} returned successfully!")
            return
    print("Invalid book or not borrowed.")

def view_member_books():
    mid = int(input("Enter Member ID: "))
    print(f"\n--- Books borrowed by Member {mid} ---")
    for b in books:
        if b['borrowed_by'] == mid:
            print(f"{b['id']}. {b['title']} (Due: {b['due_date']})")

def view_overdue_books():
    today = datetime.date.today()
    print("\n--- Overdue Books ---")
    for b in books:
        if not b['available'] and b['due_date'] < today:
            print(f"{b['id']}. {b['title']} borrowed by Member {b['borrowed_by']} (Due: {b['due_date']})")

def library_report():
    total = len(books)
    borrowed = len([b for b in books if not b['available']])
    available = total - borrowed
    print("\n--- Library Report ---")
    print(f"Total Books: {total}")
    print(f"Available: {available}")
    print(f"Borrowed: {borrowed}")
    print(f"Total Members: {len(members)}")

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    new_id = len(books) + 1
    books.append({"id": new_id, "title": title, "author": author, "available": True, "borrowed_by": None, "due_date": None})
    print("Book added successfully!")

def register_new_member():
    name = input("Enter member name: ")
    new_id = len(members) + 1
    members.append({"id": new_id, "name": name})
    print("Member registered successfully!")

# Main Program Loop
while True:
    print("\n====================================")
    print("        LIBRARY MANAGEMENT SYSTEM   ")
    print("====================================")
    print("1. Display All Books")
    print("2. Display Available Books")
    print("3. Display All Members")
    print("4. Search Books")
    print("5. Borrow a Book")
    print("6. Return a Book")
    print("7. View Member's Borrowed Books")
    print("8. View Overdue Books")
    print("9. Library Report")
    print("10. Add New Book")
    print("11. Register New Member")
    print("0. Exit")
    print("====================================")

    choice = input("Enter your choice (0-11): ")

    if choice == "1":
        display_all_books()
    elif choice == "2":
        display_available_books()
    elif choice == "3":
        display_all_members()
    elif choice == "4":
        search_books()
    elif choice == "5":
        borrow_book()
    elif choice == "6":
        return_book()
    elif choice == "7":
        view_member_books()
    elif choice == "8":
        view_overdue_books()
    elif choice == "9":
        library_report()
    elif choice == "10":
        add_new_book()
    elif choice == "11":
        register_new_member()
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
