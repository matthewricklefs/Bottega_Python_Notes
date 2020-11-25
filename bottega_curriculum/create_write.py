#How to Create and Write to a File in Python

# file_builder = open("logger.txt", "w+")

# for i in range(1000):
#     file_builder.write(f"I'm on line {i + 1}\n")


# # file_builder.write("Hey, I'm in a file!")

# file_builder.close()

### Using Regular Expressions to List File Types in Python

# import fnmatch
# from fnmatch import fnmatchcase
# import os

# def list_files():
#     for file in os.listdir('.'):
#         if fnmatch.fnmatch(file, '*.txt'):
#             print('Text files:', file)

#         if fnmatch.fnmatch(file, '*.rb'):
#             print('Ruby files:', file)

#         if fnmatch.fnmatch(file, '*.yml'):
#             print('Yaml files:', file)

#         if fnmatch.fnmatch(file, '*.py'):
#             print('Python files:', file)


# list_files()

# players = [
#     "Jose Altuve 2B",
#     "Carlos Correa SS",
#     "Alex Bregman 3B",
#     "Scooter Gennett 2B"
# ]

# second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

# print(second_base_players)

###Appending to a File in Python

# import datetime
# from time import sleep

# for i in range(5):
#     file_builder = open("logger.txt", "a+")
#     file_builder.write(f'{datetime.datetime.now()}\n')
#     file_builder.close()

#     print("file created")

#     sleep(1)


### READING AND WORKING WITH FILE DATA

# def get_file_contents(filename):
#     queried_file = open(filename, 'r')

#     if queried_file.mode == 'r':
#         return queried_file.read()


# content = get_file_contents('file-section/text_content.txt')

# print(content)

# print("Number of words", len(content.split()))


####DELETING files  

# import os

# os.remove("file-section/file_to_be_deleted.txt")

# print("File Removed!")


