# String to Integer (atoi)

s = "   -04-2"

def clamp_to_32bit_integer(value: int) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if value < INT_MIN: return INT_MIN
    elif value > INT_MAX: return INT_MAX
    return value

def myAtoi(s: str) -> int:
    final: str = "" 
    s = s.strip() # Removes whitespaces
    
    if len(s) > 1 and s[0] in ['+', '-']: # Checks signs
        final += s[0]
        s = s[1:]
        
    if len(s) > 1 and s[1] not in ['+', '-']: s = s.lstrip('0') # Removes leading zeroes
    
    # Adds remaining digits to final, breaks if a non-digit is encountered
    for ind, char in enumerate(s): 
        if not char.isdigit(): break
        final += char
    
    if len(final) == 1 and not final.isdigit(): final = ""
    
    return clamp_to_32bit_integer(int(final)) if final else 0

if __name__ == "__main__":
    print(f"\nOutput: {myAtoi(s)}\n")