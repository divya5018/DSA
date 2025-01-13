def canPlaceFlowers( flowerbed, n: int) -> bool:
        count=0
        if flowerbed[0]==0:
            emptycount=1
        else:    emptycount=0
        if flowerbed[-1]==0:
            flowerbed.append(0)
            flowerbed.append(1)
        for i in flowerbed:
            if i ==1:
                temp=(((emptycount+1)//2)-1)
                if temp>0:
                   count=count+temp
                emptycount=0
                if count>=n:
                    return True
            else:
                emptycount+=1
        # temp=(((emptycount+1)//2)-1)
        # if temp>0:
        #     count=count+temp
        # emptycount=0
        # if count>=n:
        #     return True        
        return False 

flowerbed=eval(input().strip())
n=int(input())
print(canPlaceFlowers(flowerbed,n)) 