#Exercise 1
print("Exercise 1 \n")

x = "python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/"
print("The " + x.capitalize() + ".")

#Exercise 2
print("\nExercise 2\n")

h = 5

for i in range(1,h+1):
    space = " " *(h-i)
    stars = "*" * (2*i-1)
    print(space + stars)

#Exercise 3
print("\nExercise 3\n")
x = "Your line spacing options aren\'t limited to the ones in the Line and Paragraph Spacing menu. \nTo adjust spacing with more precision, select Line Spacing Options from the menu to access the Paragraph dialog box.You\'ll then have a few additional options you can use to customize spacing."
print(x)

#Exercise 4
print("\nExercise 4\n")

print("Hey! {0:s}, your account has been credited £{1:.3f}".format("John",5786.72478))

#Exercise 5
print("\nExercise 5\n")

import datetime
current_date = datetime.datetime.now()
date_object = datetime.datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S.%f')
print(date_object)

#Exercise 6
print("\nExercise 6\n")

# name = input("What is your name?: ")
# city = input("What is your city?: ")
# country = input("What is your country?: ")
# print(f"Nice to meet you {name} from {city}, {country}.")

#Exercise 7
print("\nExercise 7\n")

sentence1 = "Simple is better than complex ."
sentence2 = "Complex is better than complicated ."
sentence1 = set(sentence1.split(' '))
sentence2 = set(sentence2.split(' '))
print(sentence1.union(sentence2))
print(sentence1.intersection(sentence2))
print(sentence1.difference(sentence2))
print(sentence1.isdisjoint(sentence2))
print(sentence1.issubset(sentence2))
print(sentence1.issuperset(sentence2))

#Exercise 8
print("\nExercise 8\n")
Company = { "Department1" : { "name" : "Data Governance", "Revenue" : 20011.78 }, "Department2" : { "name" : "Electricity Pricing", "Revenue" : 55451.901 }, "Department3" : { "name" : "Gas Pricing", "Revenue" : 62728.99 }, "Department4" : { "name" : "Smart Meter", "Revenue" : 41728.99 } }
print(Company.keys())
print(Company["Department1"].keys())
print(Company["Department2"])
print(Company["Department3"])
print(Company["Department2"]["name"])
print(Company["Department4"]["Revenue"])
print(Company["Department4"].keys())