import sys, queue

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = [] # pairs of (id, cost)

    def addNeighbour(self, name, cost):
        self.neighbours.append((name, cost))

    def getNeighbours(self):
        return self.neighbours

    def getName(self):
        return self.name

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, name):
        self.nodes[name] = Node(name)

        return self.nodes[name]

    def getNode(self, name):
        return self.nodes[name]

    def getAllNodes(self):
        return self.nodes

def readMatrix(file):
    matrix = []
    for line in file:
        row = []
        for num in line.split(','):
            row.append(int(num))
        matrix.append(row)
    return matrix

def dijkstra(graph, start):
    pqueue = queue.PriorityQueue()

    pqueue.put((0, start.getName()))

    visited = {}

    while not pqueue.empty():
        costSoFar, nodeName = pqueue.get()

        if nodeName == 'end':
            return costSoFar
        
        if nodeName in visited: continue
        visited[nodeName] = True
        
        node = graph.getNode(nodeName)
        for name, nextCost in node.getNeighbours():
            pqueue.put((costSoFar + nextCost, name))

    print("Couldn't find end node!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python p082.py path_to_matrix.txt")
        exit()

    with open(sys.argv[1]) as file:
        matrix = readMatrix(file)
        rows = len(matrix)
        cols = len(matrix[0])

        print("Read matrix; rows: {}, cols: {}".format(rows, cols))
        
        graph = Graph()

        for i in range(cols):
            for j in range(rows):
                name = (i, j)
                node = graph.addNode(name)

                if i > 0:
                    node.addNeighbour((i - 1, j), matrix[i - 1][j])
                if i < cols - 1:
                    node.addNeighbour((i + 1, j), matrix[i + 1][j])
                if j < rows - 1:
                    node.addNeighbour((i, j + 1), matrix[i][j + 1])
                if j > 0:
                    node.addNeighbour((i, j - 1), matrix[i][j - 1])

        start = graph.addNode('start')
        end = graph.addNode('end')
        
        start.addNeighbour((0, 0), matrix[0][0])
        graph.getNode((rows - 1, cols - 1)).addNeighbour(end.getName(), 0)
        
        # find minimum cost path using Dijkstra's algorithm
        print(dijkstra(graph, start))
