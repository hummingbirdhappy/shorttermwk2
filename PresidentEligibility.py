#ask for the person's age
age = raw_input("Please enter your age: ")
if age.isdigit():
    age = int(age)
else:
    print ("You need to enter an integer for your age.")

#ask if the person is a natural born citizen
citizen = raw_input("Are you a citizen of the United States of America?").lower()
if citizen == "yes":
    natural_born = raw_input("Were you born in the U.S.?").lower()
    if natural_born == "yes":
        nbc = True
    else:
        nbc = False
else:
    citizen = False
    nbc = False

#ask how many years the person has lived in the U.S.
residence_years = raw_input("How many years have you lived in the U.S.?")
if residence_years.isdigit():
    residence_years = int(residence_years)
else:
    print ("Please enter an integer for the number of years you have lived in the U.S.")

#all eligibility requirements are met or not
if age >= 35 and nbc ==True and residence_years >= 14:
    print ("You are eligible to run for presidency in the U.S.")
else:
    print ("You are not eligible to run for presidency in the U.S.")
    

