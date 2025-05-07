class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
       
        while left <= right:
           
            mid = (left + right) // 2
            
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1                 
            else:
                right = mid - 1
        
        
        return -1
    
'''left = 0
right = num of len - 1
     while left <= right:
         mid = (left+rigt)//2
         
         if num[mid] == target:
            return mid
         elif nums[mid] < target:
             left = mid + 1
         else
             right = mid-1    

      return -1'''