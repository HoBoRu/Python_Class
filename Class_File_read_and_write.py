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
