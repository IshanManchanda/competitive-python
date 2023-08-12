def main():
    from sys import stdin, stdout
    rl = stdin.readline
    wl = stdout.write

    for _ in range(int(rl())):
        m1 = m2 = -1
        n = int(rl())
        a = map(int, rl().split())
        for x in a:
            if x > m1:
                m2 = m1
                m1 = x
            elif x > m2:
                m2 = x
        wl(str(m1 + m2) + '\n')


main()
