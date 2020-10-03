numbers = (1,2,3,4,5)
result = map(lambda x : x*2, numbers )
print(list(result))

"""using normal function"""

def double(n):
    return n+n

result1 = map(double, numbers)
print(list(result1))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

arr = [[1, 2, 3],
       [4, 5, 6],
       [2, 1, 2]]




def findSum(arr):
    return sum(map(sum,arr))

print(findSum(arr))