# FILE: DSAGraph.py
# AUTHOR: Joby Mathew
# UNIT: COMP5008 Data Structures and Algorithms
# PURPOSE: Provides a class for Graph Implementation
# REFERENCE: Lecture Slides
# Last Mod: 18th September, 2020

from LinkedList import DSALinkedList
from StackQueue import DSAStack, DSAQueue

# CLASS DSAGraphEdge
# FIELDS: from, to, label, value # can have label and/or value
# CONSTRUCTOR DSAGraphEdge IMPORTS fromVertex, toVertex, inLabel, inValue
# ACCESSOR getLabel IMPORTS NONE EXPORTS label
# ACCESSOR getValue IMPORTS NONE EXPORTS value
# ACCESSOR getFrom IMPORTS NONE EXPORTS vertex
# ACCESSOR getTo IMPORTS NONE EXPORTS vertex
# ACCESSOR isDirected IMPORTS NONE EXPORTS boolean
# ACCESSOR toString IMPORTS NONE EXPORTS string

class DSAGraphEdge():
	
	# initializing the constructor
	def __init__(self, fromVertex, toVertex, volume, count):
		self.fromVertex = fromVertex
		self.toVertex = toVertex
		self.volume = volume
		self.count = count
	
	# Function to return the value of from vertex
	def getFromVertex(self):
		return self.fromVertex
	
	# Function to return the value of to vertex
	def getToVertex(self):
		return self.toVertex

	# Function to return the volume of the trade
	def getVolume(self):
		return self.volume
	
	# Function to return the count of the trade
	def getCount(self):
		return self.count

class DSAGraphNode():

	# initializing the graph
	def __init__(self, inLabel, inValue):
		self.label = inLabel
		self.value = inValue
		self.edges = DSALinkedList()
		self.visited = False
	
	# Returning the label of the graph node
	def getLabel(self):
		return self.label
	
	# Returning the value of the graph node
	def getValue(self):
		return self.value
	
	# Retuning the adjacent vertex list
	def getAdjacent(self):
		if self.edges.isEmpty():
			val = None
		else:
			val = self.edges.listOfValues()
		return val
	
	# Adding an edge to the graph node
	def addEdge(self, vertex):
		self.edges.insertLast(vertex)
	
	# Setting the graph node as visited
	def setVisited(self):
		self.visited = True
	
	# Clearing the graph node as visited
	def clearVisited(self):
		self.visited = False
	
	# Checking if the graph node is visited or not
	def getVisited(self):
		return self.visited


class DSAGraph():

	# Initializing the graph
	def __init__(self):
		self.vertices = DSALinkedList()
		self.edges = DSALinkedList()
	
	# Finding a vertex in the graph
	def findVertex(self, value):
		vertex = None
		currVertex = self.vertices.head
		if not(self.vertices.isEmpty()):
			while(currVertex != None):
				if currVertex.getValue().getLabel() == value:
					vertex = currVertex.getValue()
				currVertex = currVertex.getNext()
		return vertex
	
	# Finding an edge in the graph
	def findEdge(self, fromValue, toValue):
		edge = None
		currEdge = self.edges.head
		if not(self.edges.isEmpty()):
			while(currEdge != None):
				if currEdge.getValue().getFromVertex() == fromValue and currEdge.getValue().getToVertex() == toValue:
					edge = currEdge.getValue()
				currEdge = currEdge.getNext()
		return edge

	# Adding a vertex into the graph
	def addVertex(self, label, value):
		vertex = DSAGraphNode(label, value)
		self.vertices.insertLast(vertex)

	# Adding an edge into the graph
	def addEdge(self, label1, label2, volume, count):
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		vertex1.addEdge(label2)
		# vertex2.addEdge(label1)
		# edge = (label1, label2)
		edge = DSAGraphEdge(vertex1, vertex2, volume, count)
		self.edges.insertLast(edge)

	# Searching for a vertex in the graph
	def hasVertex(self, label):
		k = self.findVertex(label)
		isPresent = True
		if k == None:
			isPresent = False
		return isPresent
	
	# Searching for an edge in the graph
	def hasEdge(self, label1, label2):
		isPresent = True
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		edge = self.findEdge(vertex1, vertex2)
		if edge == None:
			isPresent = False
		return isPresent
	
	# Finding the vertex count
	def getVertexCount(self):
		return self.vertices.count()
	
	# Finding the edge count
	def getEdgeCount(self):
		return self.edges.count()
	
	# Returning a vertex in the graph
	def getVertex(self, label):
		vertex = self.findVertex(label)
		return vertex
	
	# Returning a vertex in the graph
	def getEdge(self, label1, label2):
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		edge = self.findEdge(vertex1, vertex2)
		return edge
	
	# Retruning the list of adjacent vertices of the vertex - returns the label
	def getAdjacent(self, label):
		vertex = self.findVertex(label)
		return vertex.getAdjacent()
	
	# Retruning the list of adjacent vertices of the vertex - return the edge class
	def getAdjacentE(self, label1):
		adjacentEdges = []
		vertex1 = self.findVertex(label1)
		adjacentVertices =  vertex1.getAdjacent()
		for label2 in adjacentVertices:
			if self.hasEdge(label1, label2):
				# print(vertex2.getLabel())
				val = self.getEdge(label1, label2)
				adjacentEdges.append(val)
		return adjacentEdges
	
	# Checking if a vertex is adjacent to the other
	def isAdjacent(self, label1, label2):
		isAnEdge = False
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		if self.hasEdge(label1, label2):
			isAnEdge = True
		return isAnEdge
	
	# Displaying the graph
	def display(self):
		if not self.vertices.isEmpty():
			print('Vertices of the graph')
			ll = self.listOfVertices()
			print(ll)
			
		if not self.edges.isEmpty():
			print('Edges of the graph')
			edgesList = self.listOfEdges()
			print(edgesList)
	
	# List of vertices in the graph
	def listOfVertices(self):
		vertexList = self.vertices.listOfValues()
		ll = []
		for val in vertexList:
			ll.append(val.getLabel())
		return ll
	
	# List of vertices in the graph
	def listOfEdges(self):
		edgeList = self.edges.listOfValues()
		ll = []
		for edge in edgeList:
			output = f'{edge.getFromVertex().getLabel()}-{edge.getToVertex().getLabel()}'
			ll.append(output)
		return ll
	
	# Getting the first vertex of the graph
	def getFirstVertex(self):
		return self.vertices.peekFirst()
	
	# Finding a not visited vertex in the adjacent list
	def getNotVisitedVertices(self, adjacent):
		ll = []
		if adjacent:
			for val in adjacent:
				vertex = self.findVertex(val)
				if not vertex.getVisited():
					ll.append(vertex)
		return ll
	
	# Implementing breadth First Search
	def breadthFirstSearch(self):
		# Transactions
		T = []
		# The order of BFS
		old = []
		# Initializing the queue
		queue = DSAQueue()
		# Getting the fist vertex from the graph
		vertex = self.getFirstVertex()
		# Setting the first vertex as visited
		vertex.setVisited()
		# Pushing the vertex into the BFS List
		old.append(vertex.getLabel())
		queue.enqueue(vertex.getLabel())
		while not queue.isEmpty():
			# Getting the vertex form the queue
			vertex = self.findVertex(queue.dequeue())
			if self.getAdjacent(vertex.getLabel()) != None:
				adjacentList = self.getNotVisitedVertices(self.getAdjacent(vertex.getLabel()))
				for adjVertex in adjacentList:
					# Adding the transaction into the list
					T.append((vertex.getLabel(), adjVertex.getLabel()))
					# Setting the vertex as visited
					adjVertex.setVisited()
					# Adding it to the BFS List
					old.append(adjVertex.getLabel())
					# Adding it to the queue
					queue.enqueue(adjVertex.getLabel())
		return old


if __name__ == '__main__':
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

	# BFS
	print('\nBreadth First Search\n')
	dfs = graph.breadthFirstSearch()
	print(dfs)