#define list of string
planets = ['sun', 'mercury', 'venus', 'earth', 'mars']

for planet in planets:
    if (planet == 'sun'):
        print(planet, 'is no a planet')
    else:
        print(planet, 'is a planet')
    if (planet == 'mercury'):
        print(planet, 'is closest to the sun')




month = 'februry'
print(month, 'is spelling:')

for x in month:
    print(x, end = ' ')

name = input('whatis the first name  ')

letter_count = 0

print(name, "is spelled:")
for x in name:
    print(x," ")
    letter_count +=1
print(' ')
print(letter_count, 'letter in the name  ', name)

#for loops using range
#iterate over sequence of 10 numbers, 0 - 9
for x in range(10):
    print(x)
#iterate over sequence of numbers, 0 - 9
for x in range(0, 10):
    print(x)
#iterate over a sequence of 5 numbers , 0 - 28, skiping every 6 numbers
for x in range(0, 30, 7):
                print(x)
#iterate over sequence of 6 numbers, counting backwards froms 5 - 0
for x in range(5, -1, -1):
    print(x)
print("")
#find the numbers betwen 1 and 1200 that are odd
odd_numbers = []
for number in range(1, 1201):
    # if odd opeende to add numbers list
    if(number % 2 !=0):
        odd_numbers.append(number)
print(odd_numbers,"this are the odd numbers")
