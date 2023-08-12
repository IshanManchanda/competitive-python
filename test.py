def beauty_sum(a):
    n = len(a)
    beauty = [0] * n
    print('hihi')
    for i in range(n):
        min_val = a[i]
        second_min = -1
        for j in range(i + 1, n):
            if a[j] < min_val:
                


def main():
    from sys import stdin, stdout
    rl = stdin.readline
    wl = stdout.write
    int1 = int
    str1 = str

    for _ in range(int(rl())):
        n = int(rl())
        a = list(map(int, rl().strip().split()))
        print('here')
        wl(str(beauty_sum(a)))


main()
