a = 121
b = -121

def palindrome(num):
    reversed_val = str(num)[::-1]
    if(str(num) == reversed_val):
        return True
    return False
    
print(f"Result A: {palindrome(a)}")
print(f"Result B: {palindrome(b)}")
