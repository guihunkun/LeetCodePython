class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        digits[n-1]+=1
        i=n-1
        while(digits[i]==10 and i>0):
            digits[i]=0
            digits[i-1]+=1
            i-=1
        if(digits[0]==10):
            digits.append(0)
            digits[0]=1
        return digits
        # number = int(''.join(str(x) for x in digits)) + 1
        # new_list = [int(n) for n in str(number)]
        # return new_list
