# class Invoice:

#   def greeting(self):
#     return 'Hi there'


# inv_one = Invoice()
# print(inv_one.greeting())

# inv_two = Invoice()
# print(inv_two.greeting())

#Guide to __init__ constructor

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def formatter(self):
#     return f'{self.client} owes: ${self.total}'


# google = Invoice('Google', 100)
# snapchat = Invoice('SnapChat', 200)

# print(google.formatter())
# print(snapchat.formatter())

#How to Get and Set Data in a Python Class

class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)
