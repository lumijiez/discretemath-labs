
from itertools import product as col

def generator(key, char, length):
    char_len = key.count(char)
    key_piece = key[:length - char_len:]
    list_keys = [key_piece + "".join(i) for i in list(col([chr(i) for i in range(65, 65 + 26)], repeat=char_len))]
    return list_keys

def vigenere(x, key):
    lst_final = []
    code = list(x)
    j = 0
    for i, char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i + j) % len(key)]
            lst_final.append((ord(x[i]) - ord(code[i])) % 26)
        else:
            lst_final.append(ord(char))
            j -= 1
    for i, char in enumerate(code):
        if char.isalpha():
            lst_final[i] = chr(lst_final[i] + 65)
        else:
            lst_final[i] = chr(lst_final[i])
    return ''.join(lst_final)

phrase = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
possibleKeys = []
with open("english.txt", "r", encoding="utf-8") as dictionary:
    for key in dictionary:
        possibleKeys.append(key.strip("\n"))
i = 1
possibleAnswers = {}
answerToPossibleNr = {}
for x in possibleKeys:
    print("Attempt: ", i)
    i += 1
    value = 0
    decrypted = vigenere(phrase, x).replace("\n", "")
    for j in possibleKeys:
        if j in decrypted:
            value += len(j)
    possibleAnswers[x + "/" + decrypted] = value
possibleAnswers = dict(sorted(possibleAnswers.items(), key=lambda item: item[1], reverse=True))
with open("result.txt", "w", encoding="utf-8") as file:
    for x in possibleAnswers:
        file.write(x + " " + str(possibleAnswers[x]) + "\n")
