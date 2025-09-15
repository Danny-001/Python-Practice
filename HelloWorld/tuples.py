#tuples ar elists that are immutable i.e cannot be changed 

grades = ("A", "B", "C", "D", "F")

print(grades[2])


final_pos = ("Babu", "Kigen", "Eli", "Manu", "Dante", "Jack", "Dan")

print(final_pos[0:6])

f1_points = ((1, 25), (2, 18), (3, 15), (4, 12), (5, 10), (6, 8), (7, 6), (8, 4), (9, 2), (10, 1))

print(f1_points[3])
print(f1_points[3][1])
print(f1_points[4][1])  # Index 2 of tuple at index 3
print(f1_points[5][1])  # Index 2 of tuple at index 4


ucl_points = (("Barca", 10), ("PSG", 8), ("Inter", 6), ("Bayern", 3))

print(ucl_points[1])
print(ucl_points[1][0])
print(ucl_points[2][1])
print(ucl_points[3][1])


prem_points = (("United", 12), ("City", 10), ("Arsenal", 8), ("Chelsea", 6), ("Spurs", 4), ("Liverpool", 2))

print(prem_points[0])
print(prem_points[0][0])    
print(prem_points[1][1])
print(prem_points[2][1])
print(prem_points[3][1])
print(prem_points[4][1])
print(prem_points[5][1])


country_prefixes = (("Kenya", "+254"), ("Uganda", "+256"), ("Tanzania", "+255"), ("Rwanda", "+250"), ("Burundi", "+257"))

print(country_prefixes[0])
print(country_prefixes[0][1])
print(country_prefixes[1][1])
print(country_prefixes[2][1])
print(country_prefixes[3][1])
print(country_prefixes[4][1])
print(country_prefixes[2][0])
print(country_prefixes[3][0])
print(country_prefixes[4][0])
print(country_prefixes[1][0])
print(country_prefixes[0][0])