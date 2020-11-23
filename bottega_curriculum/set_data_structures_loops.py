#Set Data Structures

'''
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}
# print(tags[0])

#Nope
#print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)
'''

#Merging Sets
'''
tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}
'''
#Merged Tags
'''
merged_tags = tags_one | tags_two
print(merged_tags)

# #tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

#tags in tags_two but not in tags_one
exclusive_to_tag_two = tags_two - tags_one
print(exclusive_to_tag_two)

#tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)
'''

