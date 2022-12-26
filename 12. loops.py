my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.pop()
my_list.pop(1)
print(my_list)

my_list = ['cat', 'dog', 'fish']
print('cat' in my_list)

for i in range(5):
    print(i)
x = 0
while x <= 5:
    if x == 4:
        break
    print(x)
    x += 1
x = 0

for x in range(5):
    if x == 3:
        continue
    print(x)

string = 'pasta'
result = ''

for i in range(len(string) - 1, -1, -1):
    result += string[i]
print(result)


lst = []
for i in range(2):
    for j in range(1, 3):
        lst.append(i * j)
print(lst)


x = [1, 2, 3, 4]
print(x[1])
