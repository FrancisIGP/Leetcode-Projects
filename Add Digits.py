# 258. Add Digits

num = int(382)

class Solution:
    def addDigits(num) -> int:
        while len(str(num)) != 1:
            temp = int(0)
            for ctr in map(int, str(num)): temp += int(ctr)
            num = temp
        return num

    print(addDigits(num))