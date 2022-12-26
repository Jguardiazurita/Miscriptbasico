
import traceback

def calculator():

# Get dog age
    age = input("Input dog years: ")

    try:
# Cast to float
        d_age = float(age)

        if d_age < 0:
            print("Age cannot be a negative number")
        elif 0 < d_age <= 1.0:
            h_age = d_age * 15
            h_age = "{:.2f}".format(h_age)
            print("the given dog age", d_age, "year old dog to be", h_age, "in human years")
        elif 1.0 < d_age <= 2.0:
            h_age = d_age * 12
            h_age = "{:.2f}".format(h_age)
            print("The given dog age", d_age, "is", h_age, "in human years.")
        elif 2.0 < d_age <= 3.0:
            h_age = d_age * 9.3
            h_age = "{:.2f}".format(h_age)
            print("The given dog age", d_age, "is", h_age, "in human years.")
        elif 3.0 < d_age <= 4.0:
            h_age = d_age * 8
            h_age = "{:.2f}".format(h_age)
            print("The given dog age", d_age, "is", h_age, "in human years.")
        elif 4.0 < d_age <= 5.0:
            h_age = d_age * 7.2
            h_age = "{:.2f}".format(h_age)
            print("The given dog age", d_age, "is", h_age, "in human years.")
        else:
            h_age = 36 + ( d_age - 5) * 7
            h_age = "{:.2f}".format(h_age)
            print("The given dog age", d_age, "is", h_age, "in human years.")
    except:
            print(age, "is an invalid age.")
            print(traceback.format_exc())

calculator() # This line calls the calculator function
