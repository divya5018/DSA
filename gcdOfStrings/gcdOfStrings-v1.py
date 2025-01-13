def gcdOfStrings( str1: str, str2: str) -> str:
        res=""
        if str2 == "" :
            return str1
        elif str1 =="":
            return str2
        elif   str2.startswith(str1):
            res=str2[len(str1):]
            return  gcdOfStrings(str1, res)  
        elif  str1.startswith(str2):
            res=str1[len(str2):]
            return gcdOfStrings(str2, res) 
        else:   
            return "" 
a=input().strip()
b=input().strip()
print(gcdOfStrings(a,b))