def alcohol(age, money):

    if (age >=18) and (money >=500):
        return "Tunapiga Drink"
    elif ( age >=18) and (money <500):
        return "Come Back with more Ps"
    elif (age <18) and (money > 500):
        return "Haha!!Nice Try Kiddo!!!!"
    else:
        return "Just go home Kid."

print(alcohol(21, 1000))
print(alcohol(30, 300))
print(alcohol(17, 1500))
print(alcohol(15, 4000))


def votes(age, voterCard, choice,):
    if (age>=18) and (voterCard==True) and (choice==True):
        return "You can participate in elections.. Welcome in!!"
    elif (age<18) and (voterCard==True) and (choice==True):
        return "Go back home kid. You're not old enough"
    elif (age>=18) and (voterCard==False) and (choice==True):
        return "!!YOU DO NOT HAVE A VOTER'S CARD!!!!"
    elif (age>=18) and (voterCard==True) and (choice==False):
        return "You really don't like this candidate!! Haha!!"
    else:
        return "Try again...."
    
print(votes(50, True, False))
print(votes(14, True, True))
print(votes(10, False, False))


def volume (l, w, h):
    if (l<=0) or (w<=0) or (h<=0):
        return "Dimensions must be greater than zero"
    else:
        return l * w * h
print(volume(2, 3, 6))
print(volume(2, -3, 6))
print(volume(0, 3, 6))
print(volume(2, 3, 0))
print(volume(2, 3, -6))


