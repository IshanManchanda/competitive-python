def main():
    from sys import stdin, stdout
    rl = stdin.readline
    wl = stdout.write

    for _ in range(int(rl())):
        s = rl().strip()
        a = [-1] * 26
        for i, x in enumerate(s[::-1]):
            if a[ord(x) - ord('a')] == -1:
                a[ord(x) - ord('a')] = i
        m = max(a)
        wl(s[len(s) - m - 1:] + '\n')


main()
