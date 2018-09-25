import sys


def gen(n, count_l, count_r, sequence):
    if count_l + count_r == n:
        if abs(count_r - count_l) % 4 == 0:
            print(sequence)
        return
    gen(n, count_l + 1, count_r, sequence + 'L')
    gen(n, count_l, count_r + 1, sequence + 'R')

sys.stdout = open("sequences.txt", "w")
for i in range(2, 17, 2):
    gen(i, 0, 0, "")


