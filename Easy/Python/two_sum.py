class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked_numbers = {}
        
        for i, num in enumerate(nums):
            restante = target - num

            if restante in checked_numbers:
                solution = [checked_numbers[restante], i]
                return solution

            checked_numbers[num] = i

        return []
