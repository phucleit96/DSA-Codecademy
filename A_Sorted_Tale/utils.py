import csv

# --- Function to load book data from a CSV file ---
# This function reads book information from a specified CSV file,
# processes it, and returns a list of book dictionaries.
def load_books(filename):

 # --- Create an empty list to store the books ---
 bookshelf = []  # This list will hold all the book dictionaries we create

 # --- Open the CSV file and read its contents ---
 with open(filename) as file:  # Open the file safely using a context manager

   # --- Use the csv module to read the file as a dictionary reader ---
   shelf = csv.DictReader(file)  # This creates a reader that treats each row as a dictionary

   # --- Loop through each book (row) in the CSV file ---
   for book in shelf:

     # --- Create lowercase versions of author and title for easier comparison ---
     book['author_lower'] = book['author'].lower()  # Store a lowercase version of the author's name
     book['title_lower'] = book['title'].lower()   # Store a lowercase version of the book's title

     # --- Add the current book (dictionary) to the bookshelf list ---
     bookshelf.append(book)

 # --- Return the list of books (bookshelf) after processing the file ---
 return bookshelf
