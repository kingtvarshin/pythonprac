def subsequence(q,a):
    if (len(q)==0):
        print(a+ " ",end =" ")
        return 
    subsequence(q[1:],a)
    subsequence(q[1:],a+q[0])
    
x = "abcd"
subsequence(x,"")
print()
print(pow(2,len(x)))

