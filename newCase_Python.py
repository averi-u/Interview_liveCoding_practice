"""
Online cloud reading Library 

Description: design the actual app 


- Classes: 
    - representing a book
    represeting
        - id for each book: int
        - title: str 
        - display a page/content: list with key-value pair
            int - string  
        - reading_history: int 

    - representing a Library 
        - collection of Books: use id 
        - active books: use id 


"""

class Book: 
    def _init_(self, book_id, title, content): 
        self.book_id = book_id
        self.title = title
        self.content = content
        self.last_page = 0 
    
    def display_page(self): 
        return self.content[self.last_page]
        
    def turn_page(self): 
        self.last_page += 1 
        return self.display_page()
    
    
    def get_current_page(self) -> str:
        return self.content[self.last_page]

class Library: 
    def _init_(self): 
        self.collection = {}
        self.active_books = None # id
    
    def get_current_books(self): 
        return self.collection 
    
    def add_book(self, book): 
        self.collection[book.book_id] = book 


    def remove_book(self, book_id): 
        if book_id in self.collection: 
            del self.collection[book_id]
            if self.active_books == book_id
                self.active_books = None
        
    def set_active_books (self, book_id): 
        self.active_book = book_id

    

    
