Exercise Resume: Book Collection Manager

In this exercise, we implemented a Book Collection Manager in Python using three parallel lists to store book information: one list for titles, one for authors, and one for status ("read" or "unread"). The position of each element in the lists corresponds to the same book, so index i in all three lists represents one complete book.

To manage the collection, we wrote the following functions:

add_book() → Adds a new book’s title, author, and status.

mark_as_read() → Updates the status of a book to "read".

mark_as_unread() → Updates the status of a book to "unread".

search_book() → Finds and displays a book’s details by title.

list_books() → Lists all books with their authors and current status.

suggest_book() → Suggests a random unread book from the collection.

delete_book() → Removes a book by deleting its data at the corresponding index from all three lists.

This project helped us practice working with parallel lists and maintaining synchronization between them. It also showed how functions can make the program modular, reusable, and easier to extend.