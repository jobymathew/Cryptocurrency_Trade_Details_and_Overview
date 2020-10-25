"""
FILE: UnitTestDSAGraph.py 
AUTHOR: Joby Mathew
UNIT: COMP5008 Data Structures and Algorithms
PURPOSE: Provides a Test Harness for DSAGraph 
REFERENCE: Lecture Slides
Last Mod: 25th October, 2020
"""

from DSAGraph import DSAGraph

print("------------Graphs-----------\n")
# Initializing the graph
graph = DSAGraph()


assets = ['BNB', 'ETH', 'BTC', 'USDT', 'PAX', 'USD', 'BCC', 'GAS', 'UTC', 'BNT']
# Inserting into the graph vertices
for i in range(len(assets)):
	graph.addVertex(assets[i], i)


# Inserting the edges into the graph
quotes = ['UTC', 'BTC', 'USDT', 'BNT', 'BCC', 'GAS']
for i in range(len(quotes)):
	graph.addEdge(assets[i], quotes[i], 'TRADING')

# Checking if a vertex is present
print('Checking if the graph has vertex BNB: ', graph.hasVertex('BNB'))
print('Checking if the graph has vertex BNC: ', graph.hasVertex('BNC'))


# Finding the adjacent of a vertex
adjancetA = graph.getAdjacent('BTC')
print('Adjacent vertices of BTC')
print(adjancetA)

# Finding the adjacent edges of the vertex
print('Adjacent Edges of BTC')
adjacentEdgesA = graph.getAdjacentE('BTC')
print(adjacentEdgesA)


# Checking if adjacent
print('Checking if USDT is adjacent to BTC')
print(graph.isAdjacent('BTC','USDT'))

# Finding the edge and vertex count of the graph
vertexCount = graph.getVertexCount()
edgeCount = graph.getEdgeCount()
print('Showing the count of the vertices and edges')
print('Number of vertices:', vertexCount)
print('Number of edges:', edgeCount)

# Displaying the graph
print('\nDisplaying the graph')
graph.display()


