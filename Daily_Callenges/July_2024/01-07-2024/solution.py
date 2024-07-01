class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        status = False
        odd_counter = 0
        for odd in arr:
            if odd % 2 == 1:
                odd_counter +=1
                if odd_counter == 3:
                    status = True
                    return status
            else:
                odd_counter = 0
        
        return status
