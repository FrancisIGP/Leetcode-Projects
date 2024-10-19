import random
import timeit

start = timeit.default_timer()

num = [2, 7, 11, 15, 3, 2, 4]

def twoSum(arr):
    sum = None
    target = int(18)
    arr_len = len(arr) - 1
            
    while sum != target:
        
        rand_one = random.randint(0, arr_len)
        rand_two = random.randint(0, arr_len)
        sum = num[rand_one] + num[rand_two]
        
        if (sum == target):
            print(f"Indices: [{rand_one}, {rand_two}] = {sum}")
            break
        
twoSum(num)

stop = timeit.default_timer()
print('Time: ', round(stop - start, 5)) 