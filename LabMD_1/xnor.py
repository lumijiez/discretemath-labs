a, b = int(input()), int(input())
print(bool((a or not b) and (not a or b)))
