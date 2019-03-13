#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    def majorityElement(self, nums) -> int:
        n=len(nums)
        count=0
        for x in nums:
            if(count==0):
                res=x
                count=1
            else:
                if(res==x):
                    count+=1
                else:
                    count-=1
        return res



def main():
    nums=[3,2,2]
    ans=Solution().majorityElement(nums)
    print(ans)

if __name__=='__main__':
    main()
