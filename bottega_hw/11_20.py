# Write a program that separates each character of a string by a hyphen. Each character should accumulate based on the current iteration count. The start of each accumulated value should be capitalized. 

# IE:  "abcd" => "A-Bb-Ccc-Dddd"\

#      "RqaEzTy" => "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"


# s = "abcd"
# r = "-"


# string = "abcde"
# s = "-"

# for i in string:
#   s += i.upper() + 1
# return s

'''
remove_first_and_last(list_to_clean)

html = ['<h1>', 'some. content', '</h1>']
'some content'

html_2 = ['<h1>', 'some. content', '</h1>']
'some content'

remove_first_and_last(html_2)
 ['some content', 'more']




def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content

html_2 = ['<h1>', 'some. content', '</h1>']

print(remove_first_and_last(html_2))

'''

def hyphen_accumulation(string):
  #setting count to 0 because every iteration can build on this starting point
  r = 0

  #providing an empty list for the looping function to be placed into
  li = []

  for i in string:
    #for every loop iteration it's adding 1 to the r count
    r += 1
    #we are taking the list and appending our list.
    #we are casting to a string the count at that moment and multiplying it by the i value
    #then we are using the capitalize function to capitalize the first letter
    li.append(str(r * i).capitalize())
  #so after every iteration, we are going to join the "-" to the returned iterable that is then added to the empty list. This will take place until the loop is finished.
  return "-".join(li)
#we are running the hyphenated_accumulator with a pass in value of a string ('abcdefg')
print(hyphen_accumulation('abcdefg'))