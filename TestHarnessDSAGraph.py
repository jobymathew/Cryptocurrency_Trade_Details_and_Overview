from DSAGraph import DSAGraph

print("------------Graphs-----------\n")
# Initializing the graph
graph = DSAGraph()

# Inserting into the graph vertices
graph.addVertex('A',12)
graph.addVertex('B',13)
graph.addVertex('C',25)
graph.addVertex('D',65)
graph.addVertex('E',17)
graph.addVertex('F',39)
graph.addVertex('G',24)

# Inserting the edges into the graph
graph.addEdge('A','B', 12, 3)
graph.addEdge('A','C', 14, 5)
graph.addEdge('A','D', 16, 2)
graph.addEdge('A','E', 21, 44)
graph.addEdge('B','E', 45, 12)
graph.addEdge('D','F', 3, 3)
graph.addEdge('C','D', 23, 67)
graph.addEdge('E','F', 12, 45)
graph.addEdge('E','G', 12, 89)
graph.addEdge('F','G', 86, 27)

# Displaying the graph
graph.display()

# Finding the adjacent of a vertex
adjancetA = graph.getAdjacent('A')
print('Adjancent vertices of A')
print(adjancetA)

# Finding the adjacent edges of the vertex
print('Adjacent Edges of A')
adjacentEdgesA = graph.getAdjacentE('A')
print(adjacentEdgesA)


# Checking if adjacent
print(graph.isAdjacent('E','G'))

# Finding the edge and vertex count of the graph
vertexCount = graph.getVertexCount()
edgeCount = graph.getEdgeCount()
print(vertexCount)
print(edgeCount)

# Checking if a vertex is present
print(graph.hasVertex('E'))

# # DFS
# print('\nDepth First Search\n')
# dfs = graph.depthFirstSearch()
# print(dfs)

# # Clearing visited in the vertices
# for val in graph.listOfVertices():
# 	vertex = graph.findVertex(val)
# 	vertex.clearVisited()
