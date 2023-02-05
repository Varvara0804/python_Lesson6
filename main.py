class Printer:
   def __init__(self, char, width, height):
       self.char = char
       self.widch = width
       self.height = height


   def set_char(self, x):
       self.char = x




   def print(self):
       for i in range(self.height):
           print(self.char * self.widch)

   def set_width(self):
       self.widch = 7



myPrinter = Printer('0', 5, 2)
myPrinter.print()
myPrinter.set_char('x')
myPrinter.print()
myPrinter.set_width()
myPrinter.print()

