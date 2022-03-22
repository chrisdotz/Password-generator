#Password generator

#user input
first_name = input("Please enter your First Name here: ")
last_name = input("Please enter your Last Name here: ")
fav_number = input("Please enter your favorite number here: ")
fav_animal = input("Please enter your favorite animal here: ")

#change
first_name = first_name.lower()
last_name = last_name.lower()
fav_number = int(fav_number)
fav_animal = fav_animal.lower()

#grabbing first initals in CAPS
first_inital = first_name[0]
first_inital = first_inital.upper()

#adding 1 to favorite number
fav_number += 1
fav_number = str(fav_number)


print(f"Your new password login to access your privite data base is: {first_inital + last_name + fav_number + fav_animal}")