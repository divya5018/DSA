def mergeAlternately( word1: str, word2: str) -> str:
        i,j=0,0
        s=""
        while i<len(word1) and j<len(word2):
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        if len(word1)>len(word2):
            s+=word1[i:]
        else:
            s+=word2[j:]
        return s  
word1=input().strip()
word2=input().strip()
print(mergeAlternately(word1,word2))