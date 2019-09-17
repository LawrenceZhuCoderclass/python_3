def max_van_3(a,b,c):
    if a > b and a > c:
        grootgetal = a
    if b > a and b > c:
        grootgetal = b
    if c > a and c > b:
        grootgetal = c
    return grootgetal
print (max_van_3(14, 5, 98))




