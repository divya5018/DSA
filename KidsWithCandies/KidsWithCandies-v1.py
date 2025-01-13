def kidsWithCandies( candies, extraCandies) :
        result=[]
        maxi=max(candies)
        for i in candies:
            if (extraCandies+i)>=maxi:
                result.append(True)
            else:result.append(False)
        return result

candies=eval(input().strip())
extraCandies=int(input())
print(kidsWithCandies(candies,extraCandies))