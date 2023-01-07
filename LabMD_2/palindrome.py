def palindrom(string):
    l, i = len(string), 0
    j = l - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


s, nr = input(), 0
s1 = s
while len(s) > 0:
    if palindrom(s):
        flag = 1
        break
    else:
        nr += 1
        s = s[:-1]

if nr == 0:
    print(s)
else:
    ans = s1[-nr:]
    ans = ans[::-1]
    ans = ans + s1
    print(ans)
