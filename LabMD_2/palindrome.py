def kmp_algorithm(string):
    n = len(string)
    lps = [None] * n
    l, lps[0], i = 0, 0, 1    while i < n:
        if string[i] == string[l]:
            l += 1            lps[i] = l
            i += 1        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0                i += 1    return lps


def minadded(string):
    revstr = string[::-1]
    big_str = string + '$' + revstr
    lps = kmp_algorithm(big_str)
    return len(string) - lps[-1]


s = input()
nr = minadded(s)
ans = s[-nr:] + s
print(ans)
