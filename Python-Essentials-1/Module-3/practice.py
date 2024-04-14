for i in range(-1, 1):
    print("#")

myList = [0 for i in range(1,3)]
print(myList)

my_list = [[0,1,2,3] for i in range(2)]
print(my_list[2][0])

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s+=t[i][i]
print(s)

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

i = 0
while i<=5:
    i+=1
    if i % 2 == 0:
        break
    print("*")