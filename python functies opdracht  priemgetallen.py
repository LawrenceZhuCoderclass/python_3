priemgetallen = 0

def is_priemgetal(x):
    if x>= 2:
        for y in range (2,x):
            if not (x%y):
                return False
    else:
        return False
    return True
for i in range(int(input("hoeveel nummer wil je checken: "))):
    if is_priemgetal(i):
        priemgetallen += 1
        print (i)
print ("we hebben " + str(priemgetallen ) + " priemgetallen gevonden")















