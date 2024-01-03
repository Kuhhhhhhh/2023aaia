class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #把數字排好
        ans = [ [ nums[0] ] ] #把最前面、最小的數字放在兩層方括號裡
        repeat = 0
        N = len(nums) #有幾個數字
        for i in range(1,N): #想比較
            if nums[i] == nums[i-1]:
                repeat += 1
                if len(ans)<=repeat:
                    ans.append( [] )
            else: #沒有重複
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans
