def reverse(s): 
    return s[::-1] 
  
def is_Palindrome(s): 
    
    rev = reverse(s) 
 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "hallo"
ans = is_Palindrome(s) 
  
if ans == 1: 
    print("ja ") 
else: 
    print("Nee ") 














