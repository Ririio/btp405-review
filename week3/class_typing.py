class Book:
    def __init__(self, title: str, author: str, price: float, pages: int) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.current_page = 0
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author} costs {self.price}"
    
    def read(self, pages: int) -> None:
        self.current_page += pages
    
    def bookmark(self) -> int:
        return self.current_page

    
if __name__ == '__main__':
    harry_potter = Book("Harry Potter", "J.K. Rowling", 40.0, 300)
    print(harry_potter)
    print(f'Bookmark: {harry_potter.bookmark()}')
    print('Reading 10 pages...')
    harry_potter.read(10)
    print(f'Bookmark: {harry_potter.bookmark()}')