from typing import List

class UnionFind:
    # Lifted the find and union from online pseudocode
    def __init__(self, size):

        # Initialize the parent array with each element as its own representative
        self.parent = list(range(size))
        # Initial size of each group is 1
        self.size = [1 for _ in range(size)]

    def find(self, i):
        # If i itself is root or representative
        if self.parent[i] == i:
            return i

        # Else recursively find the representative of the parent
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):

        irep = self.find(i)
        jrep = self.find(j)

        # unioning by size improves balance on tree and also give the answer to problem
        if irep != jrep:
            if self.size[irep] < self.size[jrep]:
                self.parent[irep] = jrep
                self.size[jrep] += self.size[irep]
            else:
                self.parent[jrep] = irep
                self.size[irep] += self.size[jrep]

    def get_size(self, i):
        return (self.find(i), self.size[self.find(i)])
    

class Point:
    def __init__(self, x:int, y:int, z:int, group:int):
        self.x = x
        self.y = y
        self.z = z
        self.group = group
    
    def get_distance(self, other_point):    # squared distance works the same and no slow sqrt
        return ((self.x - other_point.x)**2 +
                (self.y - other_point.y)**2 +
                (self.z - other_point.z)**2)
    
    def __repr__(self) -> str:
        return f"id: {self.group}, x: {self.x}, y: {self.y}, z: {self.z}"


def solve(point_array: List[Point], uf: UnionFind, num_pairs):

    # calculate all distances first
    dp = [[-1 for _ in range(len(point_array))] for __ in range(len(point_array))]

    queue = []
    for i in range(len(point_array)):
        for j in range(i + 1, len(point_array)):
            if dp[j][i] != -1:
                dist = dp[i][j]
            else:
                dist = point_array[i].get_distance(point_array[j])
                dp[i][j] = dist
                dp[j][i] = dist
            queue.append((dist, point_array[i], point_array[j]))

    # sort on distances
    queue.sort(key= lambda x: x[0], reverse=False)

    connected = [[-1 for _ in range(len(point_array))] for __ in range(len(point_array))]

    for _ in range(num_pairs):
        shortest_points = []
        shortest_distance = -1
        for i, element in enumerate(queue):
            (dist, first, second) = element

            if dist < shortest_distance or shortest_distance == -1:
                if connected[first.group][second.group] == -1:
                    shortest_distance = dist
                    shortest_points = [first, second]
                    del queue[i]    # once connected we will not use this pair anymore
                    break

        # add connection on matrix
        connected[shortest_points[0].group][shortest_points[1].group] = 1

        # union the groups
        uf.union(shortest_points[0].group, shortest_points[1].group)

    sizes = {}
    for i in range(len(point_array)):
        id, size = uf.get_size(i)
        sizes[id] = size

    vals = list(sizes.values())
    vals.sort(reverse=True)

    return vals[0] * vals[1] * vals[2]


with open('Day 8/data.txt') as f:
    lines = f.read().splitlines()

    ponint_arr = []
    for i, line in enumerate(lines):
        splited_line = line.split(",")
        x, y, z = int(splited_line[0]), int(splited_line[1]), int(splited_line[2])
        ponint_arr.append(Point(x, y, z, i))

    uf = UnionFind(len(ponint_arr))
    #print(uf.parent)
    sum = solve(ponint_arr, uf, 1000)
    
    print(f"Sum is: {sum}")
    