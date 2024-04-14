stack = []

def push(val):
    stack.append(val)

def pop() :
    val = stack[-1]
    del stack[-1]
    return val

push(7)
push(8)
push(2)

print(stack)

print(pop())
print(pop())
print(pop())