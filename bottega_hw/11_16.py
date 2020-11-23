#1. Sum all numbers in a list
# EX: [1, 2, 3] => 6
# I want at least 2 solutions here, but shoot for three different answers here:
import math

# 1st Approach
#Creating list
li = [1,2,3]
#creating new variable with numbers in orginal variable
sum_li = [1+2+3]
#print new variable
print(sum_li)

##2nd Approach
#creating list
nums = [1,2,3,4]
#using addition operator: sum(a)
sum_of_nums = sum(nums)
#displaying summation process
print(sum_of_nums)

###3rd Approach
# Numbers to be added
num = 5
num_2 = 4
# Summation process
sum = num + num_2
# Displaying Output
print('The sum of {0} and {1} is {2}'.format(num, num_2, sum))
'''
'''
#2. Take list of words and return the longest one:
# EX: ["PHP", "Backend", "Exercises"] => "Exercises"
# Longest String in list 
# using loop 

        
#creating strings in a list
li = ['Very', 'Longer', 'Examples']

#setting variable equal to the string with the largest len
longest_string = max(li, key=len)

#printing longest string
print(longest_string)
'''

from functools import reduce
#1. Sum all numbers in a list
# EX: [1, 2, 3] => 6
# I want at least 2 solutions here, but shoot for three different answers here:
def sum_of_list(li):
  return reduce(lambda x, y: x + y, li)
print("sum using reduce: ", sum_of_list([1, 2, 3]))
def sum_of_list_iterative(li):
  count = 0
  for number in li:
    count += number
  return count
print("sum using iteration: ", sum_of_list_iterative([1 , 2, 3, 4]))
print("sum using sum function: ", sum([1, 2, 3, 4, 5]))
