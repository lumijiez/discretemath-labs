evalStr = input()
newStr = evalStr.replace("!", " not ").replace("*", " and ").replace("+", " or ")
variables = []
for x in evalStr:
    if x.isalpha() and not(x in variables):
        variables.append(x)
n = len(variables)
for x in variables:
    print("|", x, end=" ")
print("|", evalStr, "|")
for x in range(0, 2**n):
    temp = []
    for i in range(n):
        temp.append(0)
    k = x
    j = n - 1
    while k:
        temp[j] = k & 1
        k = k >> 1
        j = j - 1
    for x in range(n):
        stm = newStr
        for i in range(len(variables)):
            stm = stm.replace(variables[i], str(temp[i]))
    for x in temp:
        print("|", x, end=" ")
    print("|", end=" ")
    print(int(eval(stm)))
