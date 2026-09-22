# akshay = input("What is your age? ")  # input will always give you a string.

# if not akshay.isdigit():
#     print("Please enter a valid number")
# else:
#     if int(akshay) >= 18 and int(akshay)<= 40:
#         print("You can enter")
#     else:
#         print("Get out!!")

#If it is not a number, it will print "Please enter a valid number".
# if int(akshay) < 18:
#     print("Get OUT!!")
# elif int(akshay) >= 18 and int(akshay) <= 40:
#     print("You can enter")
# elif int(akshay) <= 60:
#     print("Hold yourself together")
# else:
#     print("You aren't valid!!")

# for i in range(0, 11, 2): # start, stop, step
#     print(i-1)

# i = 10 
# while i > 7:
#     print(i)
#     i = i-1

def age_checker(age):
     
    if int(age) < 18:
        print("Get OUT!!")
    elif int(age) >= 18 and int(age) <= 40:
        print("You can enter")
    elif int(age) <= 60:
        print("Hold yourself together")
    else:
        print("You aren't valid!!")   


salva = 27
akshay = 28
fran = 65

age_checker(salva)
age_checker(akshay)
age_checker(fran)

#Make a Menu for a restaurant.
# 5 items. 1 entre, 2 main, 2 dessert.
# each item should have it's ingredients listed.
# each item should have a price.
# Upon request you should be able to substitute ingredients.
# make a function that will calculate the final bill based on each items price.

print