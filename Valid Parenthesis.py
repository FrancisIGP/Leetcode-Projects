# Valid Parenthesis

given1, given2, given3 = str("(]"), str("(([]){})"), str("[")

def isValid(s):
    dictionary = { "{" : "}", "(" : ")", "[" : "]" }
    stack = []
    
    for char in s:
        if char in dictionary.keys(): 
            stack.append(char) 
        else: 
            if not stack or dictionary.get(stack[-1]) != char: return False
            stack.pop()
    if len(stack) != 0: return False 
    return True

print(f"Output 1: {isValid(given1)}")
print(f"Output 2: {isValid(given2)}")
print(f"Output 3: {isValid(given3)}")