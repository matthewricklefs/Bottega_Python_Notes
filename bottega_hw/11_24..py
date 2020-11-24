#my original solution
# my_dict= dict(a=2, b='abc', c=5, d='def',e=10)

# sum(value for value in my_dict.values() if isinstance(value, (int, float)))

#Ryan Solution

dictionary = {
  'data': '100',
  'data_2': 150,
  'data_3': '150',
  'data_4': 10,
  'data_5': 100,
}

def dictionary_total(dictionary):
  total = 0

  for value in dictionary.values():
    if type(value) == type(1):
      total += value
  
  return total


print(dictionary_total(dictionary))