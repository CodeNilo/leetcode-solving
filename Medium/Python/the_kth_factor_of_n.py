class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_of_n = []
        for factor_number in range(1, n + 1):
            if n % factor_number == 0:
                factors_of_n.append(factor_number)
        factors_of_n.sort()

        if k > len(factors_of_n):
            return -1
        else:
            return factors_of_n[k-1]
