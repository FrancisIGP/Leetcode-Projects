# Roman to Integer
dict = {
    'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C' : 100, 
    'XC' : 90, 'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 
    'V' : 5, 'IV' : 4, 'I' : 1
}

val = str("MCMXCVI")
output = int(0)
        
while val.strip() != "":
    if val[0:2] in dict:
        output += dict[val[0:2]]
        val = val[2:]
    else:
        output += dict[val[0:1]]
        val = val[1:]
    
print(output)