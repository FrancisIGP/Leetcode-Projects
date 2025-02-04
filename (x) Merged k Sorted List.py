# Merged k Sorted List
from itertools import chain
from typing import List

class Solution:
    given: List[List[int]] = [[1, 4, 5], [1, 3, 4], [2, 6]]
    
    def mergeKLists(self, lists: List[List[int]]) -> List[int]:
        temp: List[int] = sorted(chain(*lists))
        return temp

if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeKLists(solution.given))