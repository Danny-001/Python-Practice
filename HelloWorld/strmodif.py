# for upper case

a = "kenya is in africa"

print(a.upper())

#for lower case

print(a.lower())

#to replace a string

print(a.replace("k" , "K"))

#to combine strings and numbers 

age = 60

txt = f"Mom is {age} years old."

print(txt)

#use of escape characters to inserts to strings

#txt1 = "We are the so called "Vikings" of the north" - python rejects this statement because of the double quotes inside other double quotes
#To solve that problem 

txt1 = "We are the so called \"Vikings\" of the north "

print(txt1)
