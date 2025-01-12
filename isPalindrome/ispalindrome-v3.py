def isPalindrome( x: int) -> bool:
        if x<0 or (x!=0 and x%10==0):
                return False
        else:
                number=0
                while(x>number):
                        number=number*10+x%10
                        x=x//10
        if number==x or number//10==x:
                return True
        else:return False                

x=int(input())
print(isPalindrome(x))        