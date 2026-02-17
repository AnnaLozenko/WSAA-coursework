# Lab 3: Requests
# Author Anna Lozenko

# Write a module that interacts with API https://andrewbeatty1.pythonanywhere.com/books

import requests

url = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)

#test response status code, headers and text
#print(response.status_code)
#print(response.headers)
#print(response.text)

# code that gets all the books and prints out the title of each book
#books = response.json()
# print the list of books to see the structure of the data
#print(books)
# iterate through the list of books and print out the title of each book
#for book in books:
    #print(book['title'])


# define a function that prints out the title of each book
def print_book_titles():
    url = "https://andrewbeatty1.pythonanywhere.com/books"
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        books = response.json()
        for book in books:
            print(book['title'])
    else:
        print("Failed to retrieve data from the API")



# define a function that finds a book by ID and prints out its title. Test the function with testing code.

def print_book_by_id(book_id):
    url = f"https://andrewbeatty1.pythonanywhere.com/books/{book_id}"
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        book = response.json()
        print(book)
    else:
        print("Failed to retrieve data from the API")


# define a function that creates a new book. Test the function with testing code.

def create_book(book):
    url = "https://andrewbeatty1.pythonanywhere.com/books"
    response = requests.post(url, json=book)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 201:
        print("Book created successfully")
    else:
        print("Failed to create book")
    return response.json()



# define a function that updates a book. Test the function with testing code.

def update_book(id, book_diff):
    url = f"https://andrewbeatty1.pythonanywhere.com/books/{id}"
    response = requests.put(url, json=book_diff)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Book updated successfully")
    else:
        print("Failed to update book")


# define a function that deletes a book. Test the function with testing code.
def delete_book(id):
    url = f"https://andrewbeatty1.pythonanywhere.com/books/{id}"
    response = requests.delete(url)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 204:
        print("Book deleted successfully")
    else:
        print("Failed to delete book")

if __name__ == "__main__":
    book= {
        "author":"test",
        'title':"test title",
        "price": "123"
    }
    book_diff= {
        "price": "1234444"
    }
    print_book_titles()
    print_book_by_id(1630)
    create_book(book)
    delete_book(1630)
    update_book(1630, book_diff)

def avg_book_price():
    url = "https://andrewbeatty1.pythonanywhere.com/books"
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        books = response.json()
        total_price = 0
        for book in books:
            total_price += book['price']
        avg_price = total_price / len(books)
        print(f"Average book price: {avg_price}")
    else:
        print("Failed to retrieve data from the API")

avg_book_price()