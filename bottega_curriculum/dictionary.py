#HW Coding Challenge
'''
palindrome = 'racecar'

if (palindrome == palindrome[::-1]):
   print('True')
else:
   print('False')   

print(palindrome)
'''

'''
def palendrome(words):
    reverse_word = words[::-1]
    for i in words:
      if words == reverse_word:
        return f"""
        The word {words} is an Palindrome which 
        is the same forwards and backwards 
        {words}:{reverse_word}
        """.strip()
    else: 
        return "This is not a Palindrome... sorry"
print(palendrome('racecar'))
print(palendrome('Jacob'))
print(palendrome('ryan'))
print(palendrome('tom'))
'''
'''
def palindrome():
  user_input = input('Enter a word to check: ')

  if user_input == user_input[::-1]:
    return f'yes, {user_input} is a palindrome.'
  else:
    return f'no, {user_input} is not a palindrome.'
print(palindrome())
'''

#Nested Collections
'''
teams = {
  "astros": ['Altuve','Correa', 'Bregman'],
  "angels": ['Trout','Pujols'],
  "yankees": ['Judge','Stanton'],
}

astros = teams['astros']


print(teams['astros'])
print(teams['yankees'])
print(teams['angels'])
'''

#Adding Key Value Pairs
'''
teams = {
  "astros": ['Altuve','Correa', 'Bregman'],
  "angels": ['Trout','Pujols'],
  "yankees": ['Judge','Stanton'],
}

teams['red sox'] = ['Price', 'Betts']

print(teams)
'''
#using Get Function & Configuring Fallback Loops
'''
teams = {
  "astros": ['Altuve','Correa', 'Bregman'],
  "angels": ['Trout','Pujols'],
  "yankees": ['Judge','Stanton'],
}

featured_team = teams.get('mets', 'No featured team')

print(featured_team)
'''
#Python Dictionary View Objects
'''
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

player_names = list(players.copy().values())

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1][1][0])
'''

#Multiple Methods for Deleting Items
'''
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

removed_team = teams.pop('yankees', 'No team found by that name')

print(teams)
print(removed_team)
'''

#Lists of Nested Dictionaries
'''
teams = [
  {
    'astros': {
    '2B': 'Altuve',
    'SS': 'Correa',
    '3B': 'Bregman',
    }
  },
  
  {
    'angels': {
    'OF': 'Trout',
    'DH': 'Pujols',
    },
  }
]

#print(teams)

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])
'''

import random

#Original Solution
'''
lottery = {
  'winning': 1,
  'break_even': 2,
  'losing': 3
}
random_lottery = random.shuffle(list(lottery.items()))
'''
#Master Solution
'''
weights = {
  'winning': 1,
  'break_even': 2,
  'losing': 3
}

def weighted_lottery(weights):
  container_list = []

  for key, value in weights.items():
    for _ in range(value):
      container_list.append(key)

  return random.choice(container_list)


print(weighted_lottery(weights))
'''
'''
histogram = {
  'g': 20,
  'f': 40,
  't': 10,
  'o': 12
}
'''
'''
def values_hist(histogram):
  container_list = []

  for key, value in histogram.items():
    for _ in range(value):
     container_list.append(key)
  return math.mul($(container_list))

print(values_hist(histogram))
'''
'''
print('g' + histogram['g'] * '$')
print('f' + histogram['f'] * '$')
print('t' + histogram['t'] * '$')
print('o' + histogram['o'] * '$')
'''
'''
def my_histogram(histogram):
  final_output = ''

  for key, value in histogram.items():
    final_output += f'{key}{"$" * value}\n\n'

  return final_output

print(my_histogram(histogram))
'''

#Replace all occurencies of the first letter in string with '$' EXCEPT for the first letter itself.
# EX: "racecar" => "raceca$"
# "retrofit" => "ret$ofit"
# "talkative" => "talka$ive"
# "bobby" => "bo$$y"
# 1
def char_replace(string):
  # replace_value = string[0]
  # second_half = string[1:]
  # new_string = f'{replace_value}{second_half.replace(replace_value, "$")}'
  # return new_string
  return f'{string[0]}{string[1:].replace(string[0], "$")}'
print(char_replace("racecar"))
print(char_replace("bobby"))
# 2
def char_replace(string):
  # replacement_list = []
  replacement_list = ""
  for i in string[1:]:
    if i == string[0]:
      # replacement_list.append('$')
      replacement_list += '$'
    else:
      # replacement_list.append(i)
      replacement_list += i
  # return f'{string[0]}{"".join(replacement_list)}'
  return f'{string[0]}{replacement_list}'
print(char_replace("talkative"))
# 3 WTF!?!
def custom_split(string):
  return [char for char in string]
def char_replace(string):
  split_list = custom_split(string)
  second_half = split_list[1:]
  for letter in second_half:
    if letter == split_list[0]:
      idx = second_half.index(letter)
      second_half[idx] = "$"
  return f'{split_list[0]}{"".join(second_half)}'
print(char_replace("retrofit"))