# put your python code here
x, y, z = map(str, input().split())
a = x.ljust(4, "0")
b = y.ljust(4, "0")
c = z.ljust(4, "0")
print(a)
print(b)
print(c)