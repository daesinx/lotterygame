

import numpy as np

# gathering user input

first_number = int(input("Choose your first lotto number: "))
if first_number >= 4:
    print("Please enter a number between 1 and 4")
    first_number = int(input("Choose your first lotto number: "))
elif first_number < 1:
    print("Please enter a number between 1 and 4")
    first_number = int(input("Choose your first lotto number: "))

second_number = int(input("Choose your second lotto number: "))
if second_number >= 4:
    print("Please enter a number between 1 and 4")
    second_number = int(input("Choose your second lotto number: "))
elif second_number < 1:
    print("Please enter a number between 1 and 4")
    second_number = int(input("Choose your second lotto number: "))

third_number = int(input("Choose your third lotto number: "))
if third_number >= 4:
    print("Please enter a number between 1 and 4")
    third_number = int(input("Choose your third lotto number: "))
elif third_number < 1:
    print("Please enter a number between 1 and 4")
    third_number = int(input("Choose your third lotto number: "))

fourth_number = int(input("Choose your fourth lotto number: "))
if fourth_number >= 4:
    print("Please enter a number between 1 and 4")
    fourth_number = int(input("Choose your fourth lotto number: "))
elif fourth_number < 1:
    print("Please enter a number between 1 and 4")
    fourth_number = int(input("Choose your fourth lotto number: "))

fifth_number = int(input("Choose your fifth lotto number: "))
if fifth_number >= 4:
    print("Please enter a number between 1 and 4")
    fifth_number = int(input("Choose your fifth lotto number: "))
elif fifth_number < 1:
    print("Please enter a number between 1 and 4")
    fifth_number = int(input("Choose your fifth lotto number: "))

sixth_number = int(input("Choose your sixth lotto number: "))
if sixth_number >= 4:
    print("Please enter a number between 1 and 4")
    sixth_number = int(input("Choose your sixth lotto number: "))
elif sixth_number < 1:
    print("Please enter a number between 1 and 4")
    sixth_number = int(input("Choose your sixth lotto number: "))

print("Your lotto numbers are : " +str(first_number)+", " +str(second_number)+", " +str(third_number)+", " +str(fourth_number)+", " +str(fifth_number)+", " +str(sixth_number))
print("Good luck!")

winningticketnumber1 = np.random.randint(1,4)
winningticketnumber2 = np.random.randint(1,4)
winningticketnumber3 = np.random.randint(1,4)
winningticketnumber4 = np.random.randint(1,4)
winningticketnumber5 = np.random.randint(1,4)
winningticketnumber6 = np.random.randint(1,4)

print("The winning numbers are..  " +str(winningticketnumber1)+", " +str(winningticketnumber2)+", " +str(winningticketnumber3)+", " +str(winningticketnumber4)+", " +str(winningticketnumber5)+", " +str(winningticketnumber6))


