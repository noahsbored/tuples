def add_book(library, title, author):
    for existing_title, existing_author in library:
        if existing_title == title and existing_author == author:
            print(f"The book '{title}' by {author} already exists in the library.")
            return library

    library.append((title, author))
    print(f"The book '{title}' by {author} has been added to the library.")
    return library

