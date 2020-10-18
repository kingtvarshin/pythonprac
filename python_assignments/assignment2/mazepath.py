def printresult(r,c,result):
    global count
    if(r==0 and c==0):
        for x in result:
            print(x,end="")
        count = count+1
        print(" ",end="")
        return
    if r>0:
        result.append("V")
        printresult(r-1,c,result)
        result.remove("V")
    if c>0:
        result.append("H")
        printresult(r,c-1,result)
        result.remove("H")
    if r>0 and c>0:
        result.append("D")
        printresult(r-1,c-1,result)
        result.remove("D")

r = int(input())
c = int(input())
result = []
count=0
printresult(r-1,c-1,result)
print()
print(count)




#mazepath2

def printresult(r,c,result):
    global count
    if(r==0 and c==0):
        for x in result:
            print(x,end="")
        count = count+1
        print(" ",end="")
        return
    if r>0:
        result.append("V")
        printresult(r-1,c,result)
        result.remove("V")
    if c>0:
        result.append("H")
        printresult(r,c-1,result)
        result.remove("H")
    if r>0 and c>0 and r==c:
        result.append("D")
        printresult(r-1,c-1,result)
        result.remove("D")

r = int(input())
result = []
count=0
printresult(r-1,r-1,result)
print()
print(count)