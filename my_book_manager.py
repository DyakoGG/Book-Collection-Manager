#
titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"

def add_book(title_name: str, author_name: str):
    titles.append(title_name)
    authors.append(author_name)
    statuses.append("Unread")
    print(f"Title {title_name} from {author_name} was added to your library")

    # Append the title to titles list
    # Append the author to authors list
    # Append "Unread" to statuses list
    # Print a message confirming the addition

def mark_as_read(title: str):
    index = 0
    for each_title in titles:
        if each_title == title:
            statuses.pop(index)
            statuses.insert(index, "Read")
        index += 1

    # Loop through the titles list
    # If the title is found, update the corresponding status to "Read"
    # Print confirmation or error if not found

def mark_as_unread(title: str):
    index = 0
    for each_title in titles:
        if each_title == title:
            statuses.pop(index)
            statuses.insert(index, "Unread")
        index += 1
    # Same logic as mark_as_read, but set status to "Unread"

def search_book(keyword: str):
    index = 0
    title = titles[index]
    author = authors[index]
    status = statuses[index]
    keyword_found = False
    for each_title in titles:
        if keyword in each_title:
            keyword_found = True
        index += 1
    index = 0

    for each_author in authors:
        if keyword in each_author:
            keyword_found = True
        index += 1
    if keyword_found:
        print(f"Book found: Title {title} from {author}, satus: {status}")
    else:
        print("No books found.")

    # Loop through the titles and authors
    # If keyword is found in title or author (case-insensitive), print book info
    # If no matches, print "No books found."

def list_books():
    current_index = 0
    book_num = 0
    for book in range(len(titles)):
        book = titles[current_index]
        author_in_list = authors[current_index]
        current_status = statuses[current_index]
        current_index += 1
        book_num += 1

        print(f"{book_num}.{book} by {author_in_list}:{current_status}")
    # Loop through all books
    # Print each title, author, and status with numbering

def suggest_book():
    unread_books = []
    no_unread_books_found = False
    index = 0

    for each_satus in statuses:
        if each_satus == "Read":
            index += 1
            continue

        unread_books.append(index)
        index += 1
    if no_unread_books_found:
        pass




    # Find all books where status is "Unread"
    # If at least one unread book exists, pick one at random and suggest it
    # If all books are read, print "No unread books left."

def delete_book(title):
    index = 0
    author = authors[index]
    book_found = False
    for each_tite in titles:
        if each_tite == title:
            titles.pop(index)
            authors.pop(index)
            statuses.pop(index)
            book_found = True
        index += 1
    if book_found:
        print(f"Book found: Title {title} from {author} deleted.")
    else:
        print("Book not found.")

    # Loop through titles
    # If match found, remove the title, author, and status at the same index
    # Print confirmation or "Book not found."

def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()