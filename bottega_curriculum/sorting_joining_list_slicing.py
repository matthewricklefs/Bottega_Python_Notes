'''
User Database Query
Kristine
Tiffany
Jordan
'''

'''
users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(0, 'Anthony')

print(users)

users.append('Ian')

print(users)

print([users[2]])

users[4] = 'Brayden'

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop()

print(popped_user)
print(users)

del users[0]

print(users)
'''
'''
users = ['Kristine', 'Tiffany', 'Jordan']

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(mixed_list)
print(user_list)

nested_lists = [[123], [234], [345]]
'''

#query processes
'''
tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)
'''

#sorting
'''
tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)
'''

#Join Function
# https://www.google.com/search?q=python+development+tutorial
'''
uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(formatted_tags)
print (query_uri)
'''

#Overview of Ranges
'''
tags = ['python', 'development', 'tutorials', 'code']

tags_range = tags[1:2]

print(tag_range)
'''
'''
#Advanced Ranges and Slices

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

#tag_range = tags[:-1:2]

#reverse

#tag_range = tags[::-1]

#print(tag_range)

sorted_tags = tags.sort(reverse=True)

print(sorted_tags)
'''

#Finding the Median Value in a List
'''
Tools:
- math library
-sorted function
-list slicing
-computations
'''

import math

#Create list of values
'''
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

#Sort the List max-min

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice +1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
'''

'''
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
print(sorted_list)

list_length_mid = len(sale_prices) // 2
print(list_length_mid)

median = sorted_list[math.floor(list_length_mid)]
print(median)

def median_odd(num_list):
  sorted_list = sorted(num_list)
  list_length_mid = len(sale_prices) // 2

  return sorted_list[math.floor(list_length_mid)]

print(median_odd(sale_prices))
'''

'''
#Modulus Operator Example
import math
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3,
  9,
  15,
]
def median_odd(num_list):
  if len(num_list) % 2 == 0:
    return "List must have odd number it elements"
  sorted_list = sorted(num_list)
  list_length_mid = len(sale_prices) // 2
  return sorted_list[list_length_mid]
print(median_odd(sale_prices))
'''

'''
# the slice class

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

#print(tags[:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])
'''
'''
tags = [
  'python',
  'development',
  'tutorials',
  'code',
]

'''
'''
tags[-1] = 'Programming'
print(tags)


#tags.extend(['Programming'])
#print(tags)

new_tags = tags.extend(['Programming'])

new_tags = tags + ['Programming']

print(new_tags)

print(tags)
'''

#Dictionary 

friends = {
  'F1': 'Jean Paul',
  'F2': 'Uche',
  'F3': 'Segun',
  'F4': 'Michael'
}

second_friend = players['F2']

print(friends)

print(second_friend)