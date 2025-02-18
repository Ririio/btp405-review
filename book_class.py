class Book:
  '''A simple class to represent a book'''
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
    self.current_page = 0
  
  def __str__(self):
    return f'{self.title} by {self.author}'
  
  def read(self, pages):
    self.current_page += pages

  @property
  def next_page(self):
    return self.current_page + 1  

if __name__ == '__main__':
  lotr = Book('Lord of the Rings', 'J.R.R. Tolkien', 1000)
  print(lotr)

  print(f'Before Reading: {lotr.current_page}')
  lotr.read(100)
  print(f'After Reading: {lotr.current_page}')

  print(f'Next Page: {lotr.next_page}')
  print(f'Current Page: {lotr.current_page}')