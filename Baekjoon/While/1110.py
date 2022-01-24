num = input()
num = num.zfill(2)


def make_new_digit(arg):
    arg = list(map(int, arg))

    first = arg[-1]
    last = str(sum(arg))[-1]

    return f'{first}{last}'


cycle = 0
new_num = num
while True:
    cycle += 1

    new_num = make_new_digit(new_num)
    if new_num == num:
        break

print(cycle)
