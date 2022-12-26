
# Class to solve Dijkstra's algorithm
class Graph:
    total = 0

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, spt_set):
        min_i = 1e7
        for v in range(self.V):
            if dist[v] < min_i and spt_set[v] == False:
                min_i = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        spt_set = [False] * self.V
        for c in range(self.V):
            u = self.minDistance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        spt_set[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        total = 0
        for node in range(self.V):
            total += dist[node]
        return total


matrixList = []
names = []
names_friends_counted = {}
matrixRefactored = []
matrixForDijkstra = []
names_id = {}

# Reads all matrix data into the initial list
with open("matrix.txt", "r", encoding="utf-8") as matrixData:
    for line in matrixData:
        matrixList.append(line.split())

# Transforms the initial list into a less idiotic adjacency matrix, using ID's instead of names
for i in range(len(matrixList[0]) - 1):
    name = matrixList[0][i] + matrixList[0][i + 1]
    if "|" not in name:
        names.append(name)
    i += 2
for i in range(len(names)):
    names_id[i + 1] = names[i]
matrixRefactored.append([[0]] + [[x] for x in names_id])
for i in range(1, len(matrixList)):
    temp = [[i]]
    for x in range(2, len(matrixList[i])):
        if matrixList[i][x] != '|':
            temp.append([int(matrixList[i][x])])
    matrixRefactored.append(temp)

# Counts friends for each person and outputs it
for i in range(1, len(matrixRefactored[0])):
    count = 0
    for x in range(1, len(matrixRefactored[i])):
        if matrixRefactored[i][x] == [1]:
            count += 1
    names_friends_counted[names_id[i]] = count
print("==================================")
print("People sorted by amount of friends")
print("==================================")
names_friends_counted = dict(sorted(names_friends_counted.items(), key=lambda item: item[1], reverse=True))
for x in names_friends_counted:
    print(x, " ", names_friends_counted[x])

# Transforms the less idiotic matrix into an EVEN less idiotic matrix so Dijkstra can understand it
for i in range(1, len(matrixRefactored[0])):
    temp = []
    for j in range(1, len(matrixRefactored[i])):
        temp.append(matrixRefactored[i][j][0])
    matrixForDijkstra.append(temp)

# Method call for Dijkstra and summation of all node values, plus output
g = Graph(len(matrixForDijkstra[0]))
g.graph = matrixForDijkstra
rating_by_id = {}
for i in range(len(matrixForDijkstra)):
    rating_by_id[i + 1] = g.dijkstra(i)
print("===============")
print("People's rating")
print("===============")
people_by_initial_rating = {}
for i in range(len(matrixForDijkstra)):
    people_by_initial_rating[names_id[i + 1]] = rating_by_id[i + 1]
people_by_initial_rating = dict(sorted(people_by_initial_rating.items(), key=lambda item: item[1], reverse=True))
for x in people_by_initial_rating:
    print(x, " ", people_by_initial_rating[x])

# Reads the influence file and stores all the shit into a useful list
people_influence = []
with open("influence.txt", "r", encoding="utf-8") as influence:
    for x in influence:
        temp = x.split()
        people_influence.append(temp[-1])

# Evaluates the final rating by the [friends] * (0.5 * [influence]) formula
people_final_rating = {}
for i in range(len(matrixForDijkstra)):
    people_final_rating[i + 1] = float(names_friends_counted[names_id[i + 1]]) * (float(people_influence[i]) * 0.5)
print("==========================")
print("People sorted by influence")
print("==========================")
people_final_rating = dict(sorted(people_final_rating.items(), key=lambda item: item[1], reverse=True))
for i in people_final_rating:
    print(names_id[i], " ", people_final_rating[i])

# Reads and stores the list of interests onto a list
interests_list = []
with open("interests.txt", "r", encoding="utf-8") as interests:
    for x in interests:
        interests_list.append(x.split()[0])

# Checks the matching topics from the phrase
print("=============================")
print("Book is marketable by topics:")
print("=============================")
topics = []
phrase = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats."
for x in interests_list:
    if x in phrase:
        topics.append(x)
        print(x)

# Reads the interests from each person and stores them in a dictionary
people_interests_list = {}
people_matching_interests = {}
people_matching_interests_name_final_rating = {}
with open("people_interests.txt", "r", encoding="utf-8") as people_interests:
    id = 1
    for line in people_interests:
        people_interests_list[id] = line.split()[3:]
        id += 1

# Counts how many matching interests do people have with the phrase for later use
for x in people_interests_list:
    count = 0
    for i in topics:
        if i in people_interests_list[x]:
            count += 1
    people_matching_interests[x] = count
for x in people_matching_interests:
    # Calculates the rating by the formula 0.2 * [matching interests] * [rating]
    rating = 0.2 * people_matching_interests[x] * people_final_rating[x]
    people_matching_interests_name_final_rating[names_id[x]] = rating

# Outputs the fitting rating for book publishing
print("====================================")
print("People ranked by most fitting rating")
print("====================================")
people_matching_interests_name_final_rating = dict(
    sorted(people_matching_interests_name_final_rating.items(), key=lambda item: item[1], reverse=True))
x = 0
for i in people_matching_interests_name_final_rating:
    if x < 5:
        print(i, " ", people_matching_interests_name_final_rating[i])
    x += 1
