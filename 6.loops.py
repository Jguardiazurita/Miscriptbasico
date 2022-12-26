#forloops

numbers = [5, 3,  8, -1, -2, 0]

#define in number variable
min_number = numbers[0]
# find the minimun value
for number in numbers:
    #check if the number less than the defined min number (above)

    if number < min_number:
        #reset min nuber
        min_number = number
print(min_number, "is the min number")
