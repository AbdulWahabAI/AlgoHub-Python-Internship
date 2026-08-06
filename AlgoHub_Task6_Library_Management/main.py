from database import setup_database, add_book_db, view_books_db, update_book_db, delete_book_db

def main():
    setup_database()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter publication year: ").strip()
            
            if title and author and year.isdigit():
                add_book_db(title, author, int(year))
                print("Book added successfully!")
            else:
                print("Invalid input. Please try again.")
                
        elif choice == "2":
            books = view_books_db()
            if not books:
                print("No books found in the library.")
            else:
                print("\nID | Title | Author | Year | Status")
                print("-" * 40)
                for book in books:
                    print(f"{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]}")
                    
        elif choice == "3":
            book_id = input("Enter book ID to update: ").strip()
            if book_id.isdigit():
                title = input("Enter new title: ").strip()
                author = input("Enter new author: ").strip()
                year = input("Enter new year: ").strip()
                
                if title and author and year.isdigit():
                    update_book_db(int(book_id), title, author, int(year))
                    print("Book updated successfully!")
                else:
                    print("Invalid details provided.")
            else:
                print("Invalid ID format.")
                
        elif choice == "4":
            book_id = input("Enter book ID to delete: ").strip()
            if book_id.isdigit():
                delete_book_db(int(book_id))
                print("Book deleted successfully!")
            else:
                print("Invalid ID format.")
                
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 5.")

if __name__ == "__main__":
    main()