import math
import random
import sys

# ERROR HANDLING

def get_age():
    print("How old are you ")
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"

print(get_age())



# We can generate a random number using the randint method


random_number = random.randint(0,10)

circumfrence = 2*math.pi * random_number

print(circumfrence)



#name = sys.argv[1]


#print(name)



# BIRTHDATE

print("How old are you?")
age = int(input())

print("you were born in")
year = int(2021-age)
print(year)


print("you will turn 80 in")
granny = int(2021 + 80)

print(granny)


players = 5

while players >= 2 :
    print("The remaining players are",players)
    players -= 1


birthdays = {"John":"August 1","Marcus":"April 8"}
birthdays["mary"] = "September 14"
print(birthdays) # this prints {"John":"August 1","Marcus":"April 8","Mary":"September 14"}

#default

print("Enter a string")

input_string = input()

characters = {}


for character in input_string:
  characters.setdefault(character,0)
  characters[character] = characters[character] + 1

print(characters)



alpha = "I like old music"
password = "K34jndnks"
number_string = "12345"
tabbs = "       "
titles = "I Love Cups"
false_titles = "I love Cups"

print( alpha.isalpha() )
print( password.isalnum() )
print( number_string.isdecimal() )
print( tabbs.isspace() )
print( titles.istitle() )
print( false_titles.istitle())


def fun_a (a,b):
    return a+b

sum = fun_a(4,5)

print(sum)



# MULTIPLES OF 3 AND 5

for fizzbuzz in (range(0,51)):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue

    fizzbuzz.reverse()
    
    print(fizzbuzz)