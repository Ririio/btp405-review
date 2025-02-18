import book_class as bc

class Comic(bc.Book):
  def __init__(self, title, author, illustrator):
    super().__init__(title, author, 0)
    self.illustrator = illustrator

  def __str__(self):
    return f'{self.title} by {self.author} and Illustrated by {self.illustrator}'
  
  def coloured(self):
    return f'{self.title} is a coloured comic'
  
if __name__ == '__main__':
  one_piece = Comic('One Piece', 'Eiichiro Oda', 'Someone')
  print(one_piece)

  print(f'Before Reading: {one_piece.current_page}')
  one_piece.read(100)
  print(f'After Reading: {one_piece.current_page}')

  print(f'Next Page: {one_piece.next_page}')
  print(f'Current Page: {one_piece.current_page}')

  print(one_piece.coloured())