# Assignment-1-BPC

It is Repository for Assignment-1-Module 2: Basic Python Concepts.

It is having two file Task1.py and Task2.py as per assignment tasks.

#Task1.py File

#Assignment 1:
## Module 2: Basic Python Concepts
### Task 1: Perform Basic Mathematical Operations
#### This Program takes two numbers num1 and num2 as input from the user . It typecast the inputs to int and store in num1 & num2

num1 = int (input('Enter the first number: '))

num2 = int (input('Enter the second number: '))

#### Performs the basic mathematical operations on these two numbers and display the results of each operation on the screen

print('Addition: ', num1+num2)
print('Subtraction: ', num1-num2)
print('Multiplication: ', num1*num2)
print('Division: ', num1/num2)

#---------------------End of Task1.py--------------------------------

###Output of Task1.py

Enter the first number: 3
Enter the second number: 4
Addition:  7
Subtraction:  -1
Multiplication:  12
Division:  0.75

----------------------------------------------

#Task2.py File

#Assignment 1:
## Module 2: Basic Python Concepts
### Task 2: Create a Personalized Greeting
#### This Program takes a user's first name and last name: first and last as input from the user. It typecast the inputs to str #### and store in first & last

first = str(input('Enter your first name: '))

last = str(input('Enter your last name: '))

#### Concatenates the first name and last name into full name

full_name = first +" "+ last

#### Prints a personalized greeting message using the full_name

#print('Hello,', full_name,'! Welcome to the Python program.')

##### show greeting with above print but it is putting extra space between last name and !, Hence form greeting string and print ##### personalized greeting message.

greeting = "Hello, "+ full_name + "! Welcome to the Python program."

print(greeting)

#--------------------End of Task2.py------------------------------

###Output of Task2.py

Enter your first name: John
Enter your last name: Doe
Hello, John Doe! Welcome to the Python program.

#--------Thank you-----------
