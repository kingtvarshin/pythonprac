def TowerOfHanoi(n , from_rod, to_rod, aux_rod,count=0):
    if n == 1:
        print("Move 1th disc from T"+str(from_rod)," to T"+str(to_rod))
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod,count+1)
    print ("Move "+str(n)+"th disc from T"+str(from_rod)+" to T"+str(to_rod))
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod,count+1) 

def required_steps(n):
    if n == 1:
        return 1
    return 1 + 2 * required_steps(n-1)
          
# Driver code 
n = int(input())
TowerOfHanoi(n, 1, 2, 3,0)
print(required_steps(n))