#string slicing is the returning part of a string 

a = "Hello World"

print(a [2:7])

#slicing from the start

print(a [: 7])

#Slicing to the end 

print(a [2 :])

#slicing from the end or negative slicing 

print(a [-7 : -2])

#split() method - splits the string into a list

sentence = "Hello, welcome to the world of Python"
print(sentence.split())  # Splits at each space

#join() method - joins the elements of an iterable (like a list) into a single string, with a specified separator.

words = ["Hello", "world", ",", "welcome", "to", "Python"]
sentence = " ".join(words)  # Joins with a space
print(sentence)

#escape characters - used to insert characters that are illegal in a string

text = "He said, \"Hello, how are you?\""
print(text)

#or.....

text = "He said, 'Hello, how are you?'"
print(text)

#strip() method - removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

text = "   Hello, World!   "
new_text = text.strip()  # Removes leading and trailing spaces
print(new_text)

#letter case manipulation

text = "hello world"
print(text.upper())  # Converts to uppercase

text = "HELLO WORLD"
print(text.lower())  # Converts to lowercase

#format() method - allows you to format selected parts of a string.

movie = "\"The Hangover\""
year = 2009
fav_movie = f"My favorite movie is {movie} which was released in {year}."
print(fav_movie)