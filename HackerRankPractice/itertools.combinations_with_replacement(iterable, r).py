from itertools import combinations_with_replacement
S, k = input().split(" ")
out = list(combinations_with_replacement(sorted(S), int(k)))
#out = list(out)
[print("".join(i)) for i in out]