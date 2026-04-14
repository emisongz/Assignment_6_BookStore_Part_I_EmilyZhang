import sqlite3

DB_NAME = "bookstore.db"


def print_divider() -> None:
    print("\n" + "-" * 40)


def pause() -> None:
    input("\nPress Enter to continue...")


def print_menu() -> None:
    print_divider()
    print("Bookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Search books by author")
    print("9. Show only books with readNow = 1")
    print("10. Show books within a price range")
    print("11. Count books per category")
    print("12. Quit")


def welcome_screen() -> None:
    print_divider()
    print("Welcome to the Bookstore CLI")
    print("Use the menu to browse and manage your books.")
    pause()


def view_categories(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "SELECT categoryId, categoryName, categoryImage FROM category ORDER BY categoryId"
    )
    rows = cursor.fetchall()

    print_divider()
    print("Categories")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No categories found.")


def view_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT bookId, title, author, price, image, readNow
        FROM book
        ORDER BY title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def view_books_in_category(cursor: sqlite3.Cursor) -> None:
    category_id = input("Enter a category id: ").strip()

    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        ORDER BY book.title
        """,
        (category_id,)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books in category")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def search_by_title(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter a title keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title
        """,
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Matching books")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Enter readNow (0 or 1): ").strip())

        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )

        print_divider()
        print("Book added.")

    except ValueError:
        print_divider()
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        print_divider()
        print("Database error:", error)


def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())

        cursor.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (new_price, book_id)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found.")
        else:
            print("Price updated.")

    except ValueError:
        print_divider()
        print("Invalid input.")


def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id to delete: ").strip())

        cursor.execute(
            "DELETE FROM book WHERE bookId = ?",
            (book_id,)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found.")
        else:
            print("Book deleted.")

    except ValueError:
        print_divider()
        print("Invalid input.")


def search_by_author(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter an author keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price
        FROM book
        WHERE author LIKE ?
        ORDER BY author, title
        """,
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Matching authors")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")
    

def view_read_now_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT bookId, title, author, price, readNow
        FROM book
        WHERE readNow = 1
        ORDER BY title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books with readNow = 1")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def view_books_in_price_range(cursor: sqlite3.Cursor) -> None:
    try:
        minimum_price = float(input("Enter minimum price: ").strip())
        maximum_price = float(input("Enter maximum price: ").strip())

        cursor.execute(
            """
            SELECT bookId, title, author, price
            FROM book
            WHERE price BETWEEN ? AND ?
            ORDER BY price, title
            """,
            (minimum_price, maximum_price)
        )
        rows = cursor.fetchall()

        print_divider()
        print("Books in price range")

        if rows:
            for row in rows:
                print(row)
        else:
            print("No books found.")

    except ValueError:
        print_divider()
        print("Invalid input.")


def count_books_per_category(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT category.categoryName, COUNT(book.bookId)
        FROM category
        LEFT JOIN book ON category.categoryId = book.categoryId
        GROUP BY category.categoryId, category.categoryName
        ORDER BY category.categoryName
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Book count per category")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No categories found.")


def main() -> None:
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()

        welcome_screen()

        while True:
            print_menu()
            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                view_categories(cursor)
                pause()
            elif choice == "2":
                view_books(cursor)
                pause()
            elif choice == "3":
                view_books_in_category(cursor)
                pause()
            elif choice == "4":
                search_by_title(cursor)
                pause()
            elif choice == "5":
                add_book(cursor)
                connection.commit()
                pause()
            elif choice == "6":
                update_price(cursor)
                connection.commit()
                pause()
            elif choice == "7":
                delete_book(cursor)
                connection.commit()
                pause()
            elif choice == "8":
                search_by_author(cursor)
                pause()
            elif choice == "9":
                view_read_now_books(cursor)
                pause()
            elif choice == "10":
                view_books_in_price_range(cursor)
                pause()
            elif choice == "11":
                count_books_per_category(cursor)
                pause()
            elif choice == "12":
                print_divider()
                print("Goodbye!")
                break
            else:
                print_divider()
                print("Invalid option. Try again.")
                pause()


if __name__ == "__main__":
    main()
