class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        int_number = 0
        
        max = len(s)

        for i in range(max):
            if i < (max-1) and (roman_numbers[s[i]] < roman_numbers[s[i+1]]):
                int_number -= roman_numbers[s[i]]
            else:
                int_number += roman_numbers[s[i]] 

        return int_number
