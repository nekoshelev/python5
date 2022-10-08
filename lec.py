num = ''

def fun(num):

 for i in range(0, len(num)):
  if (num[i+1])-num[i] != 1:
      return num[i]+1

with open('lessons5/numfile.txt', 'r') as data:
 num = data.read()
num = list(map(int, num.split(', ')))

print(fun(num))

list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list =[list[0]]
max = list[0]
for i in list:
  if i > max:
   new_list.append(i)
max = i
print(new_list)
