def main(b,c):
 
 d= c+b
 print ('This is', d , '\n hi')
 #換行符號 以及函式的運用

def test2(): #文件寫入1
 text = 'This is a test \nThis second line \nThis is last line'
 file = open('myfile.text','w')
 #w改成r會變成讀取,改成a會變成加入
 file.write(text)
 file.close
      
def test3():
    file = open('myfile.text','r')
    #content =file.read()#一行一行讀取,長怎樣就讀怎樣
    #content =file.readlines() #存list的方式去顯示
    content =file.readline() #只讀第一行,並且顯示第一行
    content1 =file.readline() #這樣就會讀第二行
	#可以試試看excel檔案
    print(content,'\n',content1)
#test2()
#test3()

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
