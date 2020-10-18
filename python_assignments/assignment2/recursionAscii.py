def subseq(s, i, string1):
    if (i == len(string1)):
        print(s,end=" ")
        return
    subseq(s, i + 1, string1)
    subseq(s + string1[i], i + 1, string1)
    subseq(s + str(ord(string1[i])),i + 1, string1)  
        
string1 = input()
subseq("", 0, string1)
print()
print(pow(3, len(string1)))