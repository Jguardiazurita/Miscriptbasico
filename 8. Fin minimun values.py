#define a list
numbers = [5, 3, 8,  -1, -2, 0]
#min variable define
min_number = numbers[0]
#find the minimun value
for number in numbers:
    #check if the number is the less than the defined min umber (above)
    if number < min_number:
        #reset min number
        min_number = number

print(min_number, "is the min number")
