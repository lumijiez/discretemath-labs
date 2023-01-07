
number_of_flights = int(input('number of flights:'))
start = int(input('start:'))
destination = int(input('destination:'))
k = int(input('k:'))
flights = [[0]*3]*number_of_flights


def cheapest_route(fl, st, dest, k):
    if st == dest:
        return 0
    if k < 0:
        return float('inf')
    cost = float('inf')

    for i in fl:
        if i[0] == st:
            new_cost = i[2] + cheapest_route(fl, i[1], dest, k-1)
            cost = min(cost, new_cost)
    if cost == float('inf'):
        return 'no route'
    else:
        return cost


for q in range(number_of_flights):
    flights[q] = [int(x) for x in input().split()]
ans = cheapest_route(flights, start, destination, k)

print(ans)
# 1 2 15
# 1 3 10
# 1 4 50
# 2 4 10
# 3 2 3
# 3 4 30
