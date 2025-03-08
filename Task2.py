#Assignment 1:
## Module 2: Basic Python Concepts
### Task 2: Create a Personalized Greeting
#### This Program takes a user's first name and last name: first and last as input from the user. It typecast the inputs to str and store in first & last
first = str(input('Enter your first name: '))
last = str(input('Enter your last name: '))

#### Concatenates the first name and last name into full name

full_name = first +" "+ last

#### Prints a personalized greeting message using the full_name
#print('Hello,', full_name,'! Welcome to the Python program.')
#####show greeting with above print but it is putting extra space between last name and !, Hence form greeting string and print personalized greeting message.
greeting = "Hello, "+ full_name + "! Welcome to the Python program."
print(greeting)