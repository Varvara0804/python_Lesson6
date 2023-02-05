class Printer:
   def __init__(self, char, width, height):
       self.char = char
       self.width = width
       self.height = height

   def set_char(self, x):
       self.char = x

   def print(self):
       for i in range(self.height):
           print(self.char * self.width)

   def set_width(self, k):
       self.width = k


myPrinter = Printer('0', 5, 2)
myPrinter.print()
myPrinter.set_char('x')
myPrinter.print()
myPrinter.set_width(7)
myPrinter.print()
