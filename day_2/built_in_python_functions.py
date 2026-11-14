#Day 2: 30 Days of Python - Built-in Python Functions

#print("....") - Is for printing the output to the console. It can take multiple arguments and print them in a single line. It can also take optional parameters like sep, end, and file to customize the output.

#len() - This function returns the number of items in an object. It can be used with strings, lists, tuples, dictionaries, and other iterable objects.
#e.g: 
len("Hello")

#returns 5, 

len([1, 2, 3]) 
#returns 3.

#str() - This function converts an object to a string representation. It can be used to convert numbers, lists, tuples, and other objects to strings.
#e.g: 
str(123)
#returns '123',

#On the pyhton console if you type help(keyword) it will give you the documentation of that keyword. It is a built-in function that provides information about the specified object, including its methods, attributes, and usage.

# However, if you wat to see all the python keywords, you can just use help('keywords') and it will give you a list of all the keywords in python.


#Next, we will learn about variables and data types in python. Variables are used to store data in a program, and data types define the type of data that can be stored in a variable. Python has several built-in data types, including integers, floats, strings, lists, tuples, dictionaries, and sets. Each data type has its own characteristics and methods that can be used to manipulate the data.

#Checkout these examples of variable declarations in python:
# Variables in Python
first_name = 'Caleb'
last_name = 'Murithi'
full_name = first_name + ' ' + last_name
country = 'Kenya'
city = 'Nyeri'
age = 21
year = 2026
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Caleb',
   'lastname':'Murithi',
   'country':'Kenya',
   'city':'Nyeri'
   }

print(type('Caleb'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Caleb'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

print(first_name, last_name, country, city, age, is_married, skills, person_info)

print(len(first_name)) # returns 5

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


first_name = input('please enter your first name: ')
age = input('How old are you?: ')

print('Your name is:', first_name)
print('Your age is:', age)


#In Python, we can use the input() function to get user input from the console. The input() function takes a prompt string as an argument and waits for the user to enter a value. Once the user enters a value and presses Enter, the input() function returns the value as a string.

#Moreover,  there is a very interesting concept in python called type conversion. It is the process of converting a value from one data type to another. In Python, we can use built-in functions like int(), float(), str(), and bool() to convert values between different data types.

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Caleb'
last_name = 'Murithi'
print(first_name)               # 'Caleb'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['C', 'a', 'l', 'e', 'b']

print('The length of my first name is:', len(first_name), 'Whilst the length of my last name is:', len(last_name)) 

num_one = 5

num_two = 4

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = 30 

area_of_circle = 3.142 * radius**2 

circum_of_circle = 2 * 3.142 * radius

radius = float(input('please enter the radius of a circle: '))

area = 3.14 * radius ** 2
print(f'The area of the circle is: {area}')

#And with that, day 2 of the 30 days of python challenge is complete. We have learned about built-in python functions, variables, data types, type conversion, and basic arithmetic operations. In the next day, we will learn about operators in python, including arithmetic, comparison, logical, and bitwise operators. We will also learn about operator precedence and how to use parentheses to group expressions.