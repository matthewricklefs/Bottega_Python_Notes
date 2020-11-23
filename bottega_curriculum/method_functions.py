#Basic Syntax

'''
# sum = 1 + 1

# another_sum = 5 + 2

# def sum(num_one, num_two):
#   return num_one + num_two

# print(sum(1,1))
# print(sum(2,3))

# #Basic Syntax
# def full_name(first, last):
#   print(f'{first} {last}')

# full_name('Kristine', 'Hudgens')


# def auth(email, password):
#   if email == 'kristine@hudgens.com' and password == 'secret':
#     print('authorized')
#   else:
#     print('not authorized')

# auth('kristine@hudgens.com', 'secret')

def counter(max_value):
  for num in range(1, max_value):
    print(num)

counter(501)
'''

#What does it mean to return a value in a Python Function?

'''
def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)
'''

#Nest Functions in Parent Functions

'''
def math():
  def sum(a,b):
    return a + b
  
  def sub(a,b):
    return a - b

math()
'''

'''
def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')
'''

#Guide to Default Arguments

'''
def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())
'''

#Utilize Named Function Arguments

'''
def full_name(first, last):
  print(f'{first}{last}')

full_name(first = 'Kristine', last = 'Hudgens')
'''

#Function Argument Unpacking

'''
def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')
'''

#Overview of Keyword Arguments

'''

def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')
'''

#Combine all Arguemnt Types in a Single Python Function

'''
def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')
'''

#Python Lambdas
'''

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
'''
#fizzbuzz
'''
def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz') 
    elif num % 3 == 0:
      print('Fizz') 
    elif num % 5 == 0:
      print('Buzz')
    else:
      print(num)

fizz_buzz(100)

#def fizz_buzz(max_num):
#   for num in range(1, max_num + 1):
#     if num % 3 == 0 and num % 5 == 0:
#       print('FizzBuzz')
#     elif num % 5 == 0:
#       print('Buzz')
#     elif num % 3 == 0:
#       print('Fizz')
#     else:
#       print(num)


# fizz_buzz(100)
'''
#Remove First and Last Elements from a List


#My first Solution
html = ['Hello', "There", 'Here', 'We', 'Go']

def remove_first_last(html):
  _, *content, _ = html
  return content
print(remove_first_last(html))


def remove_first_last(li):
  if len(li) > 3:
    return li[1:-1]
  else: 
    return "collection must contain more than 2 items to clean..."
print(remove_first_last([1, 2])