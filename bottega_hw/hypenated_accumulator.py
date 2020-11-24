def hyphenated_accumulator(string):
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
print(hyphenated_accumulator('abcdefg'))