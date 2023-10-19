#task6 classes
import math
nums=input().split()
nums=list(map(int, nums))
prime=list(filter(lambda x: x>1 and all(x%i!=0 for i in range(2, int(math.sqrt(x))+1)) ,nums))
print(*prime)


