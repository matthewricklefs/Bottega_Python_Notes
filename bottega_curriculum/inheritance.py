### Inheritance

# class User:
#   def __init__(self, email, first_name, last_name):
#     self.email = email
#     self.first_name = first_name
#     self.last_name = last_name

#   def greeting(self):
#     return f'Hi {self.first_name} {self.last_name}'

# class AdminUser(User):
#   def active_users(self):
#     return '500'


# tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

# kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

# print(tiffany.active_users())
# print(tiffany.greeting())
# print(kristine.active_users())

###POLYMORPHISM

# class Html:
#     def __init__(self, content):
#         self.content = content

#     def render(self):             
#         raise NotImplementedError("Subclass must implement render method")


# class Heading(Html):
#     def render(self):
#         return f'<h1>{self.content}</h1>'


# class Div(Html):
#     def render(self):
#         return f'<div>{self.content}</div>'


# tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

# for tag in tags:
#     print(str(tag) + ': ' + tag.render())


### Building Polymorphic Functions

# class Heading:
#     def __init__(self, content):
#       self.content = content

#     def render(self):
#       return f'<h1>{self.content}</h1>'

# class Div:
#   def __init__(self, content):
#     self.content = content

#   def render(self):
#     return f'<div>{self.content}</div>'

# div_one = Div('Some content')
# heading = Heading('My Amazing Heading')
# div_two = Div('Another div')

# def html_render(tag_object):
#   print(tag_object.render())

# html_render(div_one)
# html_render(div_two)
# html_render(heading)

# Parent Class 
# Abstract class

### Class Inheritance Example..
# class Fish:
#   def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.skeleton = skeleton
#     self.eyelids = eyelids

#   def swim(self):
#     return "Swim Forwards"

#   def swim_backwards(self):
#     return "Swim backwards"

# # Inheritance
# class Trout(Fish):
#   pass
# bob = Trout("Bob",  "Fishers")

# print(bob.first_name + " " + bob.last_name)
# print(bob.eyelids)
# print(bob.swim())
# print(bob.swim_backwards())
# # Subclass with its own class method

# class Clownfish(Fish):
#   def live_with_anemone(self):
#     return "The clownfish is coexisting with sea anemone"
# casey = Clownfish("Casey")

# print(casey.first_name + " " + casey.last_name)
# print(casey.swim())
# print(casey.live_with_anemone())

# # print(bob.live_with_anemone())

# class Shark(Fish):
#   # Override counstructor and swim_backwards methods, but inherits the swim method
#   def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.skeleton = skeleton
#     self.eyelids = eyelids

#   # polymorphism
#   def swim_backwards(self):
#     return "The shark cannot swim backwards, but can sink backwards"
# sammy = Shark("Sammy")
# print(sammy.first_name + " " + sammy.last_name)
# print(sammy.swim())
# print(sammy.swim_backwards())

# # Mulitple Inheritance
# class Coral:
#   def community(self):
#     return "Coral lives in a community."
# class Anemome:
#   def protect_clownfish(self):
#     return "The anmeone is protecting the Clownfish"
# class CoralReef(Coral, Anemome):
#   pass
# great_barrier = CoralReef()
# print(great_barrier.community())
# print(great_barrier.protect_clownfish())