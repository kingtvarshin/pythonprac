def arraysum(i,result):
    if "" not in result:
        print(str(result))
        return
    result[0]+=(str(i))
    arraysum(i,result)
    result[0].pop(str(i))
    result[1].append(str(i))
    arraysum(i,result)
    result[1].pop(str(i))
    

n = 3
x = [2,4,6]
result = ["",""]
result[0] += str(x[0])
print(str(result[0]))
#result[0] -= str(x[0])
print(str(result[0]))

#for i in x[1:]:
    #arraysum(i,result