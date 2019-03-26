class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n=len(nums)
        res=str(nums[0])
        if n==1:
            return res
        if n==2:
            return res+ "/" + str(nums[1]);
        res+= "/(" + str(nums[1]);
        for i in range(2,n):
            res += "/" + str(nums[i]);
        res+=")";
        return res;
