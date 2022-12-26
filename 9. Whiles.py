#while loops
a = 5
while (a>0):
    print(" a is a decremented:", a)
    a -= 1


x = 4
while(x<12):
    x = 2*x
    print("x is now", x)

inp = input('hi! please say hello.')
while inp != 'hello':
    inp = input('Please say helllo. ')

print('its\' about time!')

password = ""
while password != 'secret':


    password = input("Please enter the password:'")
    if password == "secret":
        print("welcome!")
    else:
        print("sorry the password you entered us incorrect pleasae try again")
#exit a loops using break

x = 1
while x <= 10:
    if x==5:
        break# this will break out the loop inmediaely
    print(x)
    x += 1

#exit a loop using continue

for  number in range(1, 21):
    #test for add number
    if (number % 2 !=0):
        #test for multiple of 3
        if(number % 3 ==0):
            continue
        print(number)

#nested loops run inner loops in a loop
for i in range(1, 4):
    print('i', i)
    for j in range(1, 3):
        print('\t', 'j:', j)
