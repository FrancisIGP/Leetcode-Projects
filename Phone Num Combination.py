# Letter Combination of a Phone Number
import itertools

class Solution:
    # Dictionary of phone number mapping
    phone_map = { 1 : [],
                2 : ['a', 'b', 'c'],
                3 : ['d', 'e', 'f'],
                4 : ['g', 'h', 'i'],
                5 : ['j', 'k', 'l'],
                6 : ['m', 'n', 'o'],
                7 : ['p', 'q', 'r', 's'],
                8 : ['t', 'u', 'v'],
                9 : ['w', 'x', 'y', 'z'] }
    
    def letterCombinations(self, digits: str) -> list[str]:           
        if not digits: return [] # If argument is empty, return an empty list
        map_list: list[list] = [self.phone_map[int(digit)] for digit in digits]  # Stores values in combinations according to digits
        combinations: list[str] = itertools.product(*map_list)  # Unpacks all list then generate all possible combinations
        
        return ['{}'.format("".join(combo)) for combo in combinations]  # Convert tuples to strings and formats output

if __name__ == "__main__":
    solution = Solution()
    result = solution.letterCombinations("")
    print(result)
