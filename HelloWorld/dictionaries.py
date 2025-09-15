#dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)

team = {
    "forwards": ["Messi", "Neymar", "Suarez"],
    "midfielders": ["Iniesta", "Busquets", "Xavi"],
    "defenders": ["Pique", "Alba", "Puyol", "Alves"],
    "goalkeepers": ["Valdez", "Bravo", "Ter Stegen"],
}
print(team)

employees = {
    "finance": ["John", "Doe", "Smith"],
    "marketing": ["Jane", "Dane", "Brown"],
    "sales": ["Mike", "Wilson", "Taylor"], 
    "hr": ["Sara", "Davis", "Miller"]
}
print(employees)

#adding items to a dictionary

employees["it"] = ["Dan", "Kigen", "Manucho"]
print(employees)

employees["ceo"] = "Jack"
print(employees)

employees.update({"cto": "Dante"})
print(employees)

employees.update({"cfo": ["Eli", "Babu"]})
print(employees)

#accessing items in a dictionary

print(employees.get("sales"))
print(employees.get("marketing"))
print(employees["hr"])
print(employees["finance"]) 






barcelona = {
    "country": "Spain",
    "founded": 1899,
    "stadium": "Camp Nou",
    "sponsor": "Nike",
    "coach": "Hansi Flick",
    "captain": "Raphinha",
}

barcelona.update({"league": "La Liga"})
barcelona.update({"top_scorer": "Lewandowski"})


print(barcelona)
print(barcelona.get("coach"))
print(barcelona.get("captain"))



united_fc = {
    "country": "England",
    "founded": 1878,
    "stadium": "Old Trafford",
    "sponsor": "Adidas",
}


united_fc.update({"coach": "Amorim"})
united_fc.update({"captain": "Bruno Fernandes"})

print(united_fc)
print(united_fc.get("coach"))
print(united_fc.get("captain"))
print(united_fc.get("country"))


phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "release_year": 2023,
}

phone.update({"os": "Android"})
phone.update({"price": 999})
print(phone)
print(phone.get("brand"))
print(phone.get("model"))
print(phone.get("release_year"))