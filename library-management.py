import pandas as pd
import random

# Load the CSV files
Library_users = pd.read_csv('user.csv')
library_books = pd.read_csv('library_books.csv')

r = 'yes'
while r == 'yes':
    print('1. Apply for library card')
    print('2. See Books in library')
    print('3. Issue Book from library')
    print('4. Return Book to library')
    print('5. Exit')
    print()

    res = int(input('Enter your response (1,2,3,4): '))

    if res == 1:
        name = input('Enter your Name: ')
        age = int(input('Enter your age: '))
        address = input('Enter your address: ')
        
        # Generate a unique card ID
        card_id = random.randint(100, 1000)
        while card_id in Library_users['card id'].values:
            card_id = random.randint(100, 1000)
        
        print('Your library card is generated:')
        print(f'Name: {name}')
        print(f'Age: {age}')
        print(f'Address: {address}')
        print(f'Card ID: {card_id}')
        print()
        
        details = [name, age, address, card_id]
        Library_users.loc[len(Library_users)] = details
        Library_users.to_csv('user.csv', index=False)
        
        r = input('Would you like to continue (yes/no): ').lower()
        print()

    elif res == 2:
        print(library_books)
        print()

    elif res == 3:
        book_id = int(input('Enter book id: '))
        while book_id not in library_books['Book ID'].values:
            print('Please Enter valid Book ID')
            book_id = int(input('Enter book id: '))

        book_name = input('Enter book name: ')
        while book_name not in library_books['Book Name'].values:
            print('Please Enter valid Book Name')
            book_name = input('Enter book Name: ')

        # Filter the book based on Book ID and Book Name
        Book = library_books[(library_books['Book ID'] == book_id) & (library_books['Book Name'] == book_name)]
        if Book.empty:
            print('Book not found. Please check the details again.')
            continue

        Status = Book['Status'].iloc[0]
        if Status == 'Issued':
            print('Book is already issued')
            continue

        library_card = int(input('Enter your library card id: '))
        while library_card not in Library_users['card id'].values:
            print('Please Enter valid card id')
            library_card = int(input('Enter your library card id: '))

        print(f'Your book "{book_name}" is issued')
        Book_index = Book.index[0]
        library_books.loc[Book_index, 'Status'] = 'Issued'
        library_books.to_csv('library_books.csv', index=False)
        
        r = input('Would you like to continue (yes/no): ').lower()
        print()

    elif res == 4:
        book_id = int(input('Enter book id: '))
        while book_id not in library_books['Book ID'].values:
            print('Please Enter valid Book ID')
            book_id = int(input('Enter book id: '))

        book_name = input('Enter book name: ')
        while book_name not in library_books['Book Name'].values:
            print('Please Enter valid Book Name')
            book_name = input('Enter book Name: ')

        # Filter the book based on Book ID and Book Name
        Book = library_books[(library_books['Book ID'] == book_id) & (library_books['Book Name'] == book_name)]
        if Book.empty:
            print('Book not found. Please check the details again.')
            continue

        Status = Book['Status'].iloc[0]
        if Status == 'Available':
            print('Book is already available. Please check the book details again.')
            continue

        library_card = int(input('Enter your library card id: '))
        while library_card not in Library_users['card id'].values:
            print('Please Enter valid card id')
            library_card = int(input('Enter your library card id: '))

        print('Thanks for returning the book')
        Book_index = Book.index[0]
        library_books.loc[Book_index, 'Status'] = 'Available'
        library_books.to_csv('library_books.csv', index=False)

        r = input('Would you like to continue (yes/no): ').lower()
        print()

    elif res==5:
        break
    
    else:
        print('Please Enter valid response')
        print()
