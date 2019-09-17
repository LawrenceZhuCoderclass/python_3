def reverse_string(string):
    stringList = []
    counter = len(string)
    for i in range(len(string)):
        counter = counter - 1
        stringList.append(string[counter])
    newString = ''.join(stringList)
    return newString

print(reverse_string("hallo"))
    




