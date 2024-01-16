# Import necessary modules
import utils  # Module for utility functions (e.g., loading books)
import sorts  # Module containing sorting algorithms

# Load book data from CSV files
bookshelf = utils.load_books('books_small.csv')  # Load books from a smaller file
long_bookshelf = utils.load_books("books_large.csv")  # Load books from a larger file

# Create copies of the bookshelf for different sorting operations
bookshelf_v1 = bookshelf.copy()  # Copy for bubble sort by author
bookshelf_v2 = bookshelf.copy()  # Copy for quicksort by author

# Define comparison functions for sorting

def by_title_ascending(book_a, book_b):
 """Compares books alphabetically by title in ascending order."""
 return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
 """Compares books alphabetically by author in ascending order."""
 return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
 """Compares books by the total length of author and title (descending)."""
 return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

# Perform sorting operations

# Sort by title using bubble sort
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# Sort by author using bubble sort and quicksort
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

# Sort the larger bookshelf by total length using quicksort
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

# Print the total length of author and title for each book in the sorted large bookshelf
for book in long_bookshelf:
 print(len(book["author_lower"]) + len(book["title_lower"]))


# print(ord('a'))
# print(ord(' '))
# print(ord('A'))
