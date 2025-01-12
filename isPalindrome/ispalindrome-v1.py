def isPalindrome( x: int) -> bool:
        original=str(x)
        modified=original[::-1]
        if original==modified :
            return True
        else:
            return False  
x=int(input()) 
print(isPalindrome(x))       