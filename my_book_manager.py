import random
from random import choice

titles = []
authors = []
statuses = []

def add_book(title_name: str, author_name: str):
    titles.append(title_name)
    authors.append(author_name)
    statuses.append("Unread")
    return f"Title {title_name} from {author_name} was added to your library."


def mark_as_read(title: str):
    index = 0
    title_found = False
    for each_title in titles:
        if each_title == title:
            title_found = True
            statuses.pop(index)
            statuses.insert(index, "Read")
        index += 1
    if title_found:
        return f"{title} is now marked as 'Read'."
    else:
        return f"{title} not found.Try again!"


def mark_as_unread(title: str):
    index = 0
    title_found = False
    for each_title in titles:
        if each_title == title:
            title_found = True
            statuses.pop(index)
            statuses.insert(index, "Unread")
        index += 1
    if title_found:
        return f"{title} is now marked as 'Unread'."
    else:
        return f"{title} not found.Try again!"


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
        return f"Book found: Title {title} from {author}, satus: {status}"
    else:
        return "No books found."


def list_books():
    current_index = 0
    if authors:
        for _ in range(1, len(titles) + 1):
            book = titles[current_index]
            author_in_list = authors[current_index]
            current_status = statuses[current_index]
            print(f"{_}.{book} by {author_in_list}: {current_status}")
            current_index += 1
    else:
        print("Your list is empty!")


def suggest_book():  #TODO
    unread_books = []
    index = 0
    for each_satus in statuses:
        if each_satus == "Read":
            index += 1
        else:
            unread_books.append(index)
            index += 1
    if not unread_books:               #TODO
        return "No unread books in your list.Add some more!"
    else:
        index = random.randint(0, len(unread_books))
        return f"How about {titles[index]} writen by {authors[index]}?"


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
        return f"Book found: Title {title} from {author} successfully deleted."
    else:
        return "Book not found.Try again!"


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
            print(add_book(title, author))

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            print(mark_as_read(title))

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            print(search_book(keyword))

        elif choice == '5':
            list_books()

        elif choice == '6':
            print(suggest_book())

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            print(delete_book(title))

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()