from sys import stdin

tc = int(stdin.readline())
stack = list()


def push(n):
    stack.append(n)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()


def size():
    print(len(stack))


def empty():
    print(1 if len(stack) == 0 else 0)


def top():
    r = -1 if len(stack) == 0 else stack[-1]
    print(r)


for _ in range(tc):
    order = stdin.readline().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'top':
        top()
