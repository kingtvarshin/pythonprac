def process_solution(a,result):
    dic = dict()
    for i in range(1,27):
        dic[str(i)] = chr(ord('a') + i - 1)
    result.append( ''.join([ dic[x] for x in a ]) )

def construct_candidates(s):
    candidates = []
    candidates.append(s[0])
    if len(s) > 1:
        candidates.append(s[0:2])
    return candidates

def backtrack(a,s,result):
    if len(s) == 0:
        process_solution(a,result)
    else:
        candidates = construct_candidates(s)
        for candidate in candidates:
            a.append(candidate)
            backtrack(a,s[len(candidate):],result)
            a.pop()

def get_encodings(s):
    a = []
    result = []
    backtrack(a,s,result)
    return result

r = input()
if(int(r) <= 0):
    print()
elif(int(r)!=0):
    s = get_encodings(r)
    print("[",end="")
    for x in range(len(s)):
        if x==len(s)-1:
            print(s[x],end="")
        else:
            print(s[x]+",",end=" ")
    print("]",end="")
    