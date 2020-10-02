def gstr(s):
    for i in s:
        s = s.replace(i, i * 3)
        strlen = len(s)
        return [s, strlen]

str = "ab"
print(gstr(str))
