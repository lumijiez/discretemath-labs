def countSubstr(substrn, strng):
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


working_str = "banana"
substrings = [working_str[i: j] for i in range(len(working_str))
              for j in range(i + 1, len(working_str) + 1)]

words_repeating = set()
words_not_repeating = set()
nr_times_repeating = {}
nr_times_not_repeating = {}

for x in substrings:
    if countSubstr(x, working_str) > 1:
        words_repeating.add(x)

for x in substrings:
    chars = []
    strn = ''
    for y in x:
        if y in chars:
            substrings.remove(x)
            break
        else:
            chars.append(y)
            strn += y
        words_not_repeating.add(strn)

for x in words_repeating:
    nr_times_repeating[x] = countSubstr(x, working_str)

for x in words_not_repeating:
    nr_times_not_repeating[x] = countSubstr(x, working_str)

max_length_repeating = 0
max_length_not_repeating = 0

for x in words_repeating:
    if len(x) > max_length_repeating:
        max_length_repeating = len(x)

for x in words_not_repeating:
    if len(x) > max_length_not_repeating:
        max_length_not_repeating = len(x)

print("Longest duplicated substrings:")
for x in words_repeating:
    if nr_times_repeating[x] > 1 and len(x) == max_length_repeating:
        print(x)
print("Length of longest substring without repeating chars:")
print(max_length_not_repeating)
