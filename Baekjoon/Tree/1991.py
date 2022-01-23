from sys import stdin

level = int(stdin.readline())
tree = dict()

for lv in range(level):
    root, left, right = stdin.readline().split()
    tree[root] = [left, right]


def preorder(node):
    # . 은 자식이 없다는 의미이므로 종료
    if node == ".":
        return

    # 줄바꿈되지 않게 출력시키고자 함. 줄바꿈 없으면 % 가 출력됨
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])


def inorder(node):
    if node == ".":
        return

    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])


def postorder(node):
    if node == ".":
        return

    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
