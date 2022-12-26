def numeric_to_letter_grade():
    #get the user input of a numerical grade
    grade = input("Enter your grade")
    # cast to in a int
    grade = int(grade)

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print ("B")
    elif grade >= 70:
        print ("C")
    elif grade >= 60:
        print ("D")
    else:
        print ("F")

numeric_to_letter_grade()


def numeric_to_letter_grade(grade):

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print ("B")
    elif grade >= 70:
        print ("C")
    elif grade >= 60:
        print ("D")
    else:
        print ("F")

grade = input("Enter your number ")
grade = int(grade)

numeric_to_letter_grade(grade)
