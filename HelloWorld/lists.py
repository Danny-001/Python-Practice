#lists

dopelist = ["Dan" , "Manucho" , "Kigen" , "Jack"]

print(dopelist)

#lists with different data types 

value = ["alpha" , 5500 , "romeo" , 7200]

print(value)

# list type() function

print(type(dopelist))

# list() constructor

footyclubs = list(("Barca" , "Inter" , "PSG" , "PAOK"))

print(footyclubs)

#list length

print(len(footyclubs))

#accessing list items 

print(footyclubs[2])

print(footyclubs[0:3])

print(footyclubs[-1])

print(footyclubs[1:])

print(footyclubs[-1:])

#to check if an item exists in a list

print("Barca" in footyclubs)

#changing list item value 

footyclubs[3] = "Atletico"

print(footyclubs)

#add items to a list 

footyclubs.append("Bayern")

print(footyclubs)

#to insert items to a specific index 

footyclubs.insert(2 , "Ajax")

print(footyclubs)

#to extend a list by appending two lists

moreclubs = ["Fulham" , "Dortmund" , "Ulinzi"]

footyclubs.extend(moreclubs)

print(footyclubs)

#remove list items 

footyclubs.remove("Ulinzi")

print(footyclubs)

#remove specified index

footyclubs.pop(1)

print(footyclubs)

#we can also use del to delete a specified index 

del footyclubs[1]

print(footyclubs)

#clearing a list

footyclubs.clear()

print(footyclubs)



