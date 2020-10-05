from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))

"""or"""
from itertools import permutations
S, k = input().split(" ")
permutations = list(permutations(S,int(k)))
permutations.sort()

[print("".join(i)) for i in permutations]

"""or"""
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')