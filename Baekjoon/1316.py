from sys import stdin

tc = int(stdin.readline())
group_count = 0

for _ in range(tc):
    word_list = list()

    prev = ''
    is_group = True
    word = stdin.readline().rstrip()
    for alphabet in word:
        if prev != alphabet:
            if alphabet in word_list:
                is_group = False
                break

            word_list.append(alphabet)
            prev = alphabet

    group_count += 1 if is_group else 0

print(group_count)
