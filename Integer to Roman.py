# Integer to Roman

dict = {
    1000 : 'M',
    900  : 'CM',
    500  : 'D',
    400  : 'CD',
    100  : 'C',
    90   : 'XC',
    50   : 'L',
    40   : 'XL',
    10   : 'X',
    9    : 'IX',
    5    : 'V',
    4    : 'IV',
    1    : 'I'
}

val = int(81)
output = []
    
def convert(num, dict):
    while num != 0:
        for v in dict.keys():
            if v <= num:
                decimal_val, roman_num = v, dict[v]
                output.append(roman_num)
                print(num, v, roman_num)
                num -= v
                break
        
convert(val, dict)
print(''.join(str(ctr) for ctr in output))