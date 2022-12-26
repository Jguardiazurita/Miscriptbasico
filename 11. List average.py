num_list = []
i = 0
playing = True

while(playing == True):

    num = int(input("enter an int"))
    if (num == -1):
        playing = False

    num_list.append(num)
    i += 1

num_sum = 0
for num in num_list:
    mum_sum += num

num_avg = num_sum / i

print("avg" , num_avg)
