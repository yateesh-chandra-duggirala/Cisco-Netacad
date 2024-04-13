import time 

current = time.asctime()
print(current)

timestamp = 1620372941
st = time.gmtime(timestamp)
print(time.asctime(st))

print(time.mktime(st))