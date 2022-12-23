#1
'''a = "yuhunglengzai"
print(len(a))'''

#2
'''list = [1,2,3,4]
print(sum(list))'''
'''
for items in list1:
    total += items
print(total)
'''

#3
'''def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result

list1 = [3, 4, 5]
print(multiplyList(list1))'''

#4
'''list = [2,1,3,4]
list.sort(reverse=True)
print(list[0])'''
'''list1 = [2,3,4,5]
total = 1
for items in list1:
    total *= items
print(total)'''

#5
'''list = [2,1,3,4]
list.sort()
print(list[0])'''
'''list = [1,2,3,4,5,5,55,56]
print(max(list))'''

#6
'''TxtString = "Raffles-University"
list_unique = []
for i in TxtString:
    if i not in list_unique:
        list_unique.append(i)
print(len(list_unique))'''
'''TxtString = "Raffles-University"
print(len(set(TxtString)))'''

#7
'''input_string = "Raffles-University"
frequencies = {}
for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    
    else:  
        frequencies[char] = 1

print(frequencies)'''

#8
'''string = 'Raffles-university'
if len(string) < 2:
    print('')
else:
    new_string = string[:2]+string[-2:]
    print(new_string)'''

#10

'''numbers = []
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        numbers.append(n)
print(numbers)'''

#11
'''import random

number = random.randint(1,10)
user_guess = 0
chance = 1
chance_left = 5

print("-------------------------------------")
print("Welcome to the number guessing game!")
print("-------------------------------------")

while chance < 6:
    user_guess = int(input("Enter a number between 1 to 10, you have " + str(chance_left) + " attempt: "))
    if user_guess < number:
        print("Number is too small, try again :(")
        chance = chance + 1
        chance_left = chance_left - 1
    elif user_guess > number:
        print("Number is too big, try again :(")
        chance = chance + 1
        chance_left = chance_left - 1
    elif user_guess == number:
        print("You guess correct, congrats! :)")
        print("Thank you for playing, see you next time :)")
        break

    if chance == 6:
        print("You have used your 5 attempt, guess better next time!")'''
'''from random import randint  
number = randint(1,9)
while True:
    x = int(input("Enter your number from 1 - 9: "))
    if x != number:
        print("Guessed wrong")  
        
    if x == number:
        print("Well guessed")
        break'''
'''import random
random_num = random.randint(1,9)
guess = int(input("Please guess the number: "))
while True:
 

    if guess == random_num:
        print("You guessed it!")
    else:
        print("You lost!") 
        print("The number was " + str(random_num))
        break'''
#12 

'''print("------------------------")
print("Welcome to mad libs game")
print("------------------------")

friend = input("human best friend: ")
water = input("best liquid in the world: ")
math = input("what is math: ")

print(friend+" is human best friend")
print(water+" is best liquid in the world")
print("math is "+math)'''

'''while True:
    base = input("Enter your favorite pizza base (Thick: 11; Thin: 12): ")
    total = int()

    if base == "thick":
        base=int(11)
    elif base == "thin":
        base=int(12)
    else:
        print("Error 404")
        break
    topping1 = input("Enter your favorite pizza topping [CHOOSE 3](Peperoni: 3; Chicken: 4; Extra Cheese: 3.5; Mushrooms: 2; Olives: 2):")
    if topping1 == "peperoni":
        topping1=int(3)
    elif topping1 == "chicken":
        topping1=int(4)
    elif topping1 == "extra cheese":
        topping1=int(3.5)
    elif topping1 == "mushrooms":
        topping1=int(2)
    elif topping1 == "olives":
        topping1=int(2)
    else:
        print("Error 404")
    topping2 = input("Enter your favorite pizza topping (Peperoni: 3; Chicken: 4; Extra Cheese: 3.5; Mushrooms: 2; Olives: 2):")
    if topping2 == "peperoni":
        topping2=int(3)
    elif topping2 == "chicken":
        topping2=int(4)
    elif topping2 == "extra cheese":
        topping2=int(3.5)
    elif topping2 == "mushrooms":
        topping2=int(2)
    elif topping2 == "olives":
        topping2=int(2)
    else:
        print("Error 404")
    topping3 = input("Enter your favorite pizza topping (Peperoni: 3; Chicken: 4; Extra Cheese: 3.5; Mushrooms: 2; Olives: 2):")
    if topping3 == "peperoni":
        topping3=int(3)
    elif topping3 == "chicken":
        topping3=int(4)
    elif topping3 == "extra cheese":
        topping3=int(3.5)
    elif topping3 == "mushrooms":
        topping3=int(2)
    elif topping3 == "olives":
        topping3=int(2)
    else:
        print("Error 404")
    total = str(base + topping1 + topping2 + topping3)
    print("RM"+str(total))'''








