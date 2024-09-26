from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = ""
        second_word = ""

        for x in word1:
            first_word += x

        for y in word2:
            second_word += y
        
        if first_word == second_word:
            print("true")
            return True
        else:
            print("false")
            return False


answer = Solution()
answer.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
answer.arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
answer.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])