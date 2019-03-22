#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums):
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        psum=nums[0] 
        maxsum=nums[0]
        i=1;
        while i<len(nums):
            if psum>0:
                psum+=nums[i]
            else:
                psum=nums[i]
            maxsum=max(maxsum,psum)
            i=i+1
        return maxsum
            

def main():
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    ans=Solution().maxSubArray(nums)
    print(ans)

if __name__=='__main__':
    main()
