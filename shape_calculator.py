class Rectangle:
  def __init__(self, width, height ):
    self.shape = 'Rectangle'
    self.width = width
    self.height = height

  def __repr__ (self):
    info = str(self.shape) + "(width=" + str(self.width) +', height=' + str(self.height) + ')'
    return(info)

  def set_width(self, n_width):
    if self.shape == 'Rectangle':
      self.width = n_width
    else:
      self.width = n_width
      self.heigth = n_width
      
  def set_height(self, n_height):
    if self.shape == 'Rectangle':
      self.height = n_height
    else:
      self.height = n_height
      self.heigth = n_height
    
  def get_area(self):
    area = self.width * self.height
    return(area)
    
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return(perimeter)
  
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return(diagonal)
    
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return("Too big for picture.")
    picture = ""
    for i in range(self.height):
      for j in range(self.width):
        picture = picture + "*"
      picture = picture + "\n"
    return(picture)

  def get_amount_inside(self, other_shape):
    w_dif = rounding(self.width / other_shape.width, 1)
    h_dif = rounding(self.height / other_shape.height, 1)
    #if h_dif == 0 or w_dif == 0:
      #return('0')
    amount = w_dif * h_dif
    return(amount)
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.shape = 'Square'

    def __repr__(self):
        info = str(self.shape) + "(side=" + str(self.width) + ')'
        return info

    def set_side(self, side):
      self.width = side
      self.height = side
      
def rounding(num, divisor):
    return num - (num%divisor)
