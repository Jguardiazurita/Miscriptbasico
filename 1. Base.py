print("Hi")

#Replace Variables
x = y = 10
z = 10 + y
print (" I have  ", (z), "Years Old")

#Calculate age
        #Input introducir algo
        #int es para almacenar

age = int(input ("How Old are you "))
print(age)

#calculate in 3 years

print(age+3)

#Exercise 1 Float is for deciamls

#Primero es bueno colocar la variables despues que va a hacer esa variable
bill = float(input ("How much is the Pizza Chesse "))

tax = float(input ("what is the tax (porcentage) "))

tip = float(input ("tip "))


#calculate tax

tax_amount = (bill * tax) / 100
total = bill + tax_amount

#calculate tip

tip_amount = (total * tip) / 100
total = total + tip_amount

# round 2 decimal

total = round(total, 2)
# final

print("the total bill is $ ", total, sep = '')

# Boolean is going to give False or True
print(3 >= 3)
