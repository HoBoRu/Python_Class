class Calculator(): #類別
 name = 'Good computer'
 price = 18 
 def add(self,x,y):
  print(self.name)
  print(x+y)
 
 def minus(self,x,y):
   c=x-y
   print(c)
  
 def mupli(self,x,y):
  print(x*y)
  
 def divid(self,x,y):
  print(x/y) 
 '''
calcul = Calculator()
input1 = int(input('First num:'))
input2 = int(input('Second num:'))
function = input('choose your function:') 
if function == '+':
 calcul.add(input1,input2)
 print('yo')
elif function == '/':
 calcul.divid(input1,input2)
else:
 print('No Action') 
'''

class Practice(): #for迴圈

 def loopexamole(self):
   list = [1,2,3,4,5,6,7,8,9,10]
   for i in range(len(list)):
    print('Externalloop',i)
    for i in range (1,10,2): #1-9 間隔2
     print('Innerloop',i)
  
   print('hello world')
'''
t = Practice()
t.loopexamole()
'''
