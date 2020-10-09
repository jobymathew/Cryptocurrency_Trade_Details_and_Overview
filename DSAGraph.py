# FILE: DSAGraph.py
# AUTHOR: Joby Mathew
# UNIT: COMP5008 Data Structures and Algorithms
# PURPOSE: Provides a class for Graph Implementation
# REFERENCE: Lecture Slides
# Last Mod: 18th September, 2020

from LinkedList import DSALinkedList
from StackQueue import DSAStack, DSAQueue
# importing sys to increase the recursion limit
import sys
sys.setrecursionlimit(10**6) 
import copy


class DSAGraphEdge():
	
	# initializing the constructor
	def __init__(self, fromVertex, toVertex, status):
		self.fromVertex = fromVertex
		self.toVertex = toVertex
		self.status = status
		self.volume = 0
		self.quoteVolume = 0
		self.count = 0
		self.weightedAvgPrice = 0
		self.openPrice = 0
		self.highPrice = 0
		self.lowPrice = 0
		self.priceChange = 0
		self.priceChangePercent = 0
	
	# Function to return the value of from vertex
	def getFromVertex(self):
		return self.fromVertex
	
	# Function to return the value of to vertex
	def getToVertex(self):
		return self.toVertex
	
	# Function to return the status of the trade
	def getStatus(self):
		return self.status
	
	# Function to set the volume of the trade
	def setVolume(self, inVolume):
		self.volume = inVolume
	
	# Function to set the count of the trade
	def setCount(self, inCount):
		self.count = inCount
	
	# Function to set the weightedAvgPrice of the trade
	def setWeightedAvgPrice(self, inWeightedAvgPrice):
		self.weightedAvgPrice = inWeightedAvgPrice

	# Function to return the volume of the trade
	def getVolume(self):
		return self.volume
	
	# Function to return the count of the trade
	def getCount(self):
		return self.count
	
	# Function to return the weightedAvgPrice of the trade
	def getWeightedAvgPrice(self):
		return self.weightedAvgPrice
	
	# Function to set the quote volume of the trade
	def setQuoteVolume(self, inQuoteVolume):
		self.quoteVolume = inQuoteVolume
	
	# Function to return the quote volume of the trade
	def getQuoteVolume(self):
		return self.quoteVolume
	
	# Function to set the open price of the trade
	def setOpenPrice(self, inQuoteVolume):
		self.quoteVolume = inQuoteVolume
	
	# Function to return the open price of the trade
	def getOpenPrice(self):
		return self.openPrice
	
	# Function to set the high price of the trade
	def setHighPrice(self, inHighPrice):
		self.highPrice = inHighPrice
	
	# Function to return the high price of the trade
	def getHighPrice(self):
		return self.highPrice
	
	# Function to set the low price of the trade
	def setLowPrice(self, inLowPrice):
		self.lowPrice = inLowPrice
	
	# Function to return the low price of the trade
	def getLowPrice(self):
		return self.lowPrice
	
	# Function to set the price change of the trade
	def setPriceChange(self, inPriceChange):
		self.priceChange = inPriceChange
	
	# Function to return the price change of the trade
	def getPriceChange(self):
		return self.priceChange
	
	# Function to set the price change percent of the trade
	def setPriceChangePercent(self, inPriceChangePercent):
		self.priceChangePercent = inPriceChangePercent
	
	# Function to return the low price of the trade
	def getPriceChangePercent(self):
		return self.priceChangePercent


class DSAGraphNode():

	# initializing the graph
	def __init__(self, inLabel, inValue):
		self.label = inLabel
		self.value = inValue
		self.edges = DSALinkedList()
		self.visited = False
		self.priceChange = DSALinkedList()
		self.totalPriceChange = 0
		self.priceChangePercent = DSALinkedList()
		self.totalPriceChangePercent = 0
		self.volume = DSALinkedList()
		self.totalVolume = 0
		self.count = DSALinkedList()
		self.totalCount = 0
	
	# Adding the price change to the list
	def addPriceChange(self, inPriceChange):
		self.priceChange.insertLast(inPriceChange)
		self.totalPriceChange += float(inPriceChange)
	
	# Getting the total price change 
	def getTotalPriceChange(self):
		return self.totalPriceChange
	
	# Getting the average price change
	def getAveragePriceChange(self):
		countOfItems = self.priceChange.count()
		return self.totalPriceChange/countOfItems

	# Adding the price change percent to the list
	def addPriceChangePercent(self, inPriceChangePercent):
		self.priceChangePercent.insertLast(inPriceChangePercent)
		self.totalPriceChangePercent += float(inPriceChangePercent)
	
	# Getting the total price change 
	def getTotalPriceChangePercent(self):
		return self.totalPriceChangePercent
	
	# Getting the average price change precent
	def getAveragePriceChangePercent(self):
		countOfItems = self.priceChangePercent.count()
		return self.totalPriceChangePercent/countOfItems
	
	# Adding the volume to the list
	def addVolume(self, inVolume):
		self.volume.insertLast(inVolume)
		self.totalVolume += float(inVolume)

	# Getting the total volume
	def getTotalVolume(self):
		return self.totalVolume
	
	# Getting the average volume
	def getAverageVolume(self):
		countOfItems = self.volume.count()
		return self.totalVolume/countOfItems

	# Adding the count to the list
	def addCount(self, inCount):
		self.count.insertLast(inCount)
		self.totalCount += int(inCount)
	
	# Getting the total count
	def getTotalCount(self):
		return self.totalCount
	
	# Getting the average count
	def getAverageCount(self):
		countOfItems = self.count.count()
		return int(self.totalCount/countOfItems)

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
	def addEdge(self, label1, label2, status):
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		vertex1.addEdge(label2)
		# vertex2.addEdge(label1)
		# edge = (label1, label2)
		edge = DSAGraphEdge(vertex1, vertex2, status)
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
	
	# Function to check if there is a trade edge in the graph
	def hasTradeEdge(self, tradeName):
		isFound = False
		if self.getTradeEdge(tradeName):
			isFound = True
		return isFound
	
	# Function to find the edge connecting the two assets
	def getTradeEdge(self, tradeName):
		edge = None
		vertices = self.listOfVertices()
		for label1 in vertices:
			for label2 in vertices:
				if (label1+label2) == tradeName:
					edge = self.getEdge(label1, label2)
		return edge
	
	# Function to check if the trade edge is tradeable
	def isTrading(self, tradeName):
		trading = False
		edge = self.getTradeEdge(tradeName)
		if edge and edge.getStatus() == 'TRADING':
			trading = True
		return trading
	
	# Function to find the trade path between the given assets - Note that this is a modified DFS 
	def _getPaths(self, labels, tradeList, quoteAsset):
		# Getting the last value from the labels list
		label = labels.peekLast()
		vertex = self.getVertex(label)
		# Marking the vertex as visited
		vertex.setVisited()
		adjData = self.getAdjacent(label)  
		# Checking if the adjacent list is not none and the trade path is not break            
		if adjData != None and self.isTrading(label+quoteAsset):
			if quoteAsset in adjData:
				# adding the quote asset to the path and appending to the trade list
				foundPath = copy.deepcopy(labels)
				foundPath.insertLast(quoteAsset)
				tradeList.insertLast(foundPath)
				# remove the quote asset from the list
				adjData.remove(quoteAsset)
			for val in adjData:
				newVertex = self.getVertex(val)
				# If the selected vertex is not visited, it is then added to the labels list and recursed for a new trade path
				if not newVertex.getVisited():
					newLabels = copy.deepcopy(labels)
					newLabels.insertLast(val)
					tradeList = self._getPaths(newLabels, tradeList, quoteAsset)
		return tradeList
	
	# Function to get the indirect trade path between two assets
	def getTradePaths(self, baseAsset, quoteAsset):
		# Initializing the list
		tradeList = DSALinkedList()
		labelList = DSALinkedList()
		labelList.insertLast(baseAsset)
		# Calling the recursive function
		resList = self._getPaths(labelList, tradeList, quoteAsset)
		# returning the list
		return resList

	# Retruning the list of adjacent vertices of the vertex - returns the label
	def getAdjacent(self, label):
		adjacentVertex = []
		vertex = self.findVertex(label)
		if vertex:
			adjacentVertex = vertex.getAdjacent()
		return adjacentVertex
	
	# Retruning the list of adjacent vertices of the vertex - returns the label
	def displayAdjacent(self, label):
		adjacentVertex = self.getAdjacent(label)
		print(adjacentVertex)
		

	# Retruning the list of adjacent vertices of the vertex - return the edge class
	def getAdjacentE(self, label1):
		adjacentEdges = []
		vertex1 = self.findVertex(label1)
		if vertex1:
			adjacentVertices =  vertex1.getAdjacent()
			if adjacentVertices:
				for label2 in adjacentVertices:
					if self.hasEdge(label1, label2):
						# print(vertex2.getLabel())
						val = self.getEdge(label1, label2)
						adjacentEdges.append(val)
		return adjacentEdges
	
	def displayAdjacentE(self, label):
		edges = self.getAdjacentE(label)
		displayList = []
		for edge in edges:
			displayList.append(f'{edge.getFromVertex().getLabel()}{edge.getToVertex().getLabel()}')
		print(displayList)
	
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
			output = f'{edge.getFromVertex().getLabel()}{edge.getToVertex().getLabel()}'
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
	
	# Implementing Depth First Search
	def depthFirstSearch(self, vertex):
		# Transactions
		T = []
		# The order of DFS
		old = []
		# Initializing the stack
		stack = DSAStack()
		# Setting the first vertex as visited
		vertex.setVisited()
		# Pushing the vertex into the DFS List
		stack.push(vertex.getLabel())
		old.append(vertex.getLabel())
		while not stack.isEmpty():
			# Getting all the adjacent vertices that are not visited in the graph
			while self.getNotVisitedVertices(vertex.getAdjacent()) != []:
				notVisitedVertices = self.getNotVisitedVertices(vertex.getAdjacent())
				notVisitedValue = notVisitedVertices[0].getLabel()
				# Adding the transaction into the list of transactions
				T.append((vertex.getLabel(), notVisitedValue))
				if notVisitedValue == quoteAsset:
					tradeList.append(old)
					old = [vertex.getLabel()]
				# Setting the vertex as visited
				notVisitedVertices[0].setVisited()
				# Pushing the vertex into the stack
				stack.push(notVisitedValue)
				# Adding the vertex into the DFS List
				old.append(notVisitedValue)
				vertex = notVisitedVertices[0]
			# Popping the next item from the stack
			vertex = self.find(stack.pop())
		return old
	
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
			print(f'Adjacent of {vertex.getLabel()} is {self.getAdjacent(vertex.getLabel())}')
			if self.getNotVisitedVertices(self.getAdjacent(vertex.getLabel())) != []:
				adjacentList = self.getNotVisitedVertices(self.getAdjacent(vertex.getLabel()))
				print(f'Not Visited Adjacent List of {vertex.getLabel()} is')
				for adjVertex in adjacentList:
					# Adding the transaction into the list
					T.append((vertex.getLabel(), adjVertex.getLabel()))
					print(adjVertex.getLabel())
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