# Exercise 1
# print("Exercise 1")
# number1 = float(input("Please insert first floating point number: "))
# number2 = float(input("Please insert second floating point number: "))
# if number1 > number2:
#     print("Number 1 is greater")
# elif number1 == number2:
#     print("They are equal")
# else:
#     print("Please enter correct numbers")


# Exercise 2
# print("Exercise 2")
# print("Welcome to my Python program!")
# item = []
# i = 0
# iterations = int(input("How many items do you want in your list? "))
#
# for i in range(0,iterations):
#     b = input("Enter list item: ")
#     item.append(b)
# print(item)


# Exercise 3
# print("Exercise 3")
# n = 0
# while n < 30:
#     n += 1
#     if n % 3 == 0 and n % 5 ==0:
#         print("Edinburgh")
#     elif n % 3 ==0:
#         print("Liverpool")
#     elif n % 5 ==0:
#         print("Manchester")
#     else:
#         print(n)


# Exercise 4
# print("Exercise 4")
# department = ["Department1", "Department2", "Department3"]
# cities = ["Hamburgh", "Barcelona", "London"]
# countries = ["Germany", "Spain", "UK"]
#
# department_dict = {}
#
# for i in range(len(department)):
#     department_dict[department[i]] = {
#         'city': cities[i],
#         'country': countries[i]
#     }
# print(department_dict)

# Exercise 5
# print("Exercise 5")
head = 0
tail = 0
flip = 0
i = 0
import random
while flip < 100:
    i = random.randint(0,1)
    if i == 0:
        head = head +1
        print("head!")
    else:
        tail = tail +1
        print("tail!")
    flip = flip +1
print(head)
print(tail)