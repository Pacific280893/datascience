from itertools import groupby
for i,j in groupby(input()):
    print((len(list(j)),int(i)),end=" ")

#this end will give result in one row otherwise it will come in 4 rows and 1 column
# and after equal sign value will work as eperator

"""or"""
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])   