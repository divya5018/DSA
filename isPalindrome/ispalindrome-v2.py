def isPalindrome( x: int) -> bool:
        c=x
        number=0
        while(c>0):
            m=c%10
            number=number*10+m
            c=c//10
        if number==x:
            return True
        else:return False 

x=int(input())
print(isPalindrome(x))        