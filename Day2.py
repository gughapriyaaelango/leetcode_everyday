'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        result = []
        if str1+str2 != str2+str1:
            return ""
        def gcd(len1, len2):
            min_val = min(len1,len2)
            for i in range(min_val,0,-1):
                if len1 % i == 0 and len2 % i ==0:
                    return i
            return 1
        return str1[:gcd(len(str1),len(str2))]
'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list_len = len(candies)
        max_kid = max(candies)
        result = []
        for i in range(list_len):
            if (candies[i]+extraCandies >= max_kid):
                result.append(True)
            else:
                result.append(False)
        return result
                
