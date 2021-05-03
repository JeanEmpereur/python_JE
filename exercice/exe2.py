import sys

n = 0
res = ""
for arg in sys.argv:
    res += (arg + " ") * n
    n += 1

print (res)
