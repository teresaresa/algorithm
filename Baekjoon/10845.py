from sys import stdin


def push(q, x):
    q.append(x)


def pop(q, delete=True):
    if len(q) == 0:
        print("-1")
    else:
        print(q[0])
        if delete:
            del q[0]


def size(q):
    print(len(q))


def empty(q):
    if len(q) == 0:
        print("1")
    else:
        print("0")


def front(q):
    return pop(q, delete=False)


def back(q):
    if len(q) == 0:
        print("-1")
    else:
        print(q[-1])


queue = list()
tc = int(stdin.readline())
for _ in range(tc):
    req = stdin.readline().split()

    if req[0] == "push":
        push(queue, int(req[1]))
    elif req[0] == "front":
        front(queue)
    elif req[0] == "pop":
        pop(queue)
    elif req[0] == "back":
        back(queue)
    elif req[0] == "size":
        size(queue)
    elif req[0] == "empty":
        empty(queue)
