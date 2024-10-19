# Longest Common Prefix

# strs1 = ["cir","car"]
# strs2 = ["dog","racecar","car"]

# def checkPrefix(list) -> str:
#     cmnPrefix, prefix = None, ""
        
#     for word in list: 
#         if cmnPrefix == None: cmnPrefix = word 
#         else: 
#             for ind in range(min(len(cmnPrefix), len(word))): 
#                 if cmnPrefix[ind] == word[ind]: prefix += word[ind]
#                 else: break
#             cmnPrefix, prefix = prefix, ""   
    
#     if cmnPrefix == "": return "None"
#     return cmnPrefix

# if __name__ == "__main__":
#     print(f"\nCommon Prefix #1: {checkPrefix(strs1)}")
#     print(f"Common Prefix #2: {checkPrefix(strs2)}\n")

# Efficient Code V

strs1 = ["cir", "car"]
strs2 = ["dog", "racecar", "car"]

def checkPrefix(words) -> str:
    if not words: return "None"
    
    cmnPrefix = words[0]
    for word in words[1:]:
        while not word.startswith(cmnPrefix):
            cmnPrefix = cmnPrefix[:-1]
            if not cmnPrefix: return "None"
    
    return cmnPrefix

if __name__ == "__main__":
    print(f"\nCommon Prefix #1: {checkPrefix(strs1)}")
    print(f"Common Prefix #2: {checkPrefix(strs2)}\n")