a_tuple = (12,3,5,15,6)
b_tuple = 2,4,6,7,8
a_list =[12,3,67,7,82]
a_list.append(0) #添加
a_list.insert(2,11) #添加在指定位置
a_list.remove(12) #只會刪除碰到第一個12

for i in range(len(a_list)): #依照list長度分別輸出第幾個元素的value
 print(i,a_list[i])

print('Last element:',a_list[-1])#從最後一個開始數
#print(a_list)
print('first to three element:',a_list[0:3])
print('After No.3 element:',a_list[3:])
print('Before No.3 element:',a_list[:3])
print('back:',a_list[0:-2])
print('Find index 67:',a_list.index(67)) #找67的索引
print('Count numbers:',a_list.count(0)) #計算個數
print('reverse:',a_list[::-1])
print('normal:',a_list[::1])




#排序
a_list.sort()
print(a_list)
a_list.sort(reverse = True)
print(a_list)
