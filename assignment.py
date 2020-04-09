# import libraries
import string
import random
from typing import List


def get_details():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    user_email = input("Please enter your Email address: ")

    details = [first_name, last_name, user_email]

    return details


# generate a random password using user details
def gen_password(details):
    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters) for i in range(length))
    password = str(details[0][0:2] + details[1][-2:] + random_password)
    return password


status = True
container = []
while status:

    details = get_details()

    # show generated password
    password = gen_password(details)
    print("Your password is: " + str(password))

    password_satisfaction = input(str("Are you satisfied with the password? If yes enter Yes, if no enter No and provide another password "))
    password_loop = True
    while password_loop:
        if password_satisfaction == "Yes":
            details.append(password)
            container.append(details)
            break
        else:
            user_password = input(str("Please enter password longer than 7 "))
            password_len = True
            while password_len:
                if len(user_password) >= 7:
                    details.append(user_password)
                    container.append(details)
                    break
                else:
                    print("Your password is less than 7")
                    user_password = input(str("Enter new password equal to or greater than 7 "))
    # new user
    new_user = input(str("Would you like to enter a new user? Yes or No? "))
    if new_user == "No":
        status = False
        for item in container:
            print(item)
    else:
        status = True
