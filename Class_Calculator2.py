class Calculator: #類別
   
 def __init__ (self, name, price, height, width, weight): #初始
  self.name = name
  self.price = price
  self.h = height
  self.w = width
  self.we =weight
  self.add(1,2)
 def add(self,x,y):
  #print(self.name)
  print(x+y)
 
 def minus(self,x,y):
   c=x-y
   print(c)
  
 def mupli(self,x,y):
  print(x*y)
  
 def divid(self,x,y):
  print(x/y) 
 
#c = Calculator('123',12,11,10,9)  #有init需要符合他的參數
#c.add(5,3)
#print(c.h)
