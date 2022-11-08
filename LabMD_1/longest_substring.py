def countTimesOfSubstringInString(substrn, strng):
    m = len(substrn)
    n = len(strng)
    number = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if strng[i + j] != substrn[j]:
                break
            j += 1
        if j == m:
            number += 1
    return number


test_str = "xxxx"

res = [test_str[i: j] for i in range(len(test_str))
       for j in range(i + 1, len(test_str) + 1)]

words = set()

for x in res:
    chars = []
    strn = ''
    for y in x:
        if y in chars:
            res.remove(x)
            break
        else:
            chars.append(y)
            strn += y
        words.add(strn)

nr_times = {}
for x in words:
    nr_times[x] = countTimesOfSubstringInString(x, test_str)

max_length = 0
for x in words:
    if len(x) > max_length:
        max_length = len(x)

max_occurence = 0
for x in words:
    if nr_times[x] > max_occurence:
        max_occurence = nr_times[x]
print("First program output: ")
print("Longest duplicated substrings:")
for x in words:
    if nr_times[x] > 1 and len(x) == max_length:
        print(x)
print("Second program output: ")
print("Length of longest substring:")
print(max_length)
