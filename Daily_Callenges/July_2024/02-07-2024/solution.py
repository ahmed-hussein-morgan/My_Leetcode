class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_dict = {}
        for num in nums1:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        result = []
        
        for num in nums2:
            if num in count_dict and count_dict[num] > 0:
                result.append(num)
                count_dict[num] -= 1
        
        return result
