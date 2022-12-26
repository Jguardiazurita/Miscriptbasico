#define list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to store even numbers
even_numbers = []
#to store count of even numbers
even_count = 0
# literate over the list
for number in numbers:
    if(number % 2 == 0):
        even_numbers.append(number)
        #increment count
        even_count += 1
print(even_numbers)
print("there are", even_count, "numbers in the even list . " )
print("there are", len(even_numbers), "numbers in the even list . " )
