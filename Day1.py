'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        while i < m or j < n:
            if i < m:
                result.append(word1[i])
                i = i+1
            if j < n:
                result.append(word2[j])
                j = j+1
        return "".join(result)



