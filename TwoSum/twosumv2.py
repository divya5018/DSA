def twoSum( nums, target) :
        d={}
        n=len(nums)
        for i in range(n):
            ans=target-nums[i]
            if ans in d:
                return [i,d[ans]]
            d[nums[i]]=i 


nums=eval(input().strip())
target=int(input())
print(twoSum(nums, target))

