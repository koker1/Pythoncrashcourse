#index operator [] = gives access to a sequence's element (str,list,tuples)

name = "loh Kok Hao" 

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:3].upper()
last_name = name[4:].lower()
last_character = name[-2]

print(name)
print(first_name)
print(last_name)
print(last_character)