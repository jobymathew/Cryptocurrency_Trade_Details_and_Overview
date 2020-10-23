# FILE: DSAGraph.py - Modified for the assignment
# AUTHOR: Joby Mathew
# UNIT: COMP5008 Data Structures and Algorithms
# PURPOSE: Provides a class for Graph Implementation which is to be used as cryptoGraph
# REFERENCE: Lecture Slides
# Last Mod: 18th September, 2020

from LinkedList import DSALinkedList
from StackQueue import DSAStack, DSAQueue
import numpy as np
# importing sys to increase the recursion limit
import sys
sys.setrecursionlimit(10**6) 
# importing copy to perform deep copy of classes
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
	
	# Function to return the label of the edge
	def getEdgeLabel(self):
		return self.fromVertex.getLabel()+self.toVertex.getLabel()
	
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
	def setOpenPrice(self, inOpenPrice):
		self.openPrice = inOpenPrice
	
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
		self.adjacents = DSALinkedList()
		self.visited = False
	
	# Returning the list of adjacents
	def getAdjacents(self):
		return self.adjacents

	# Returning the label of the graph node
	def getLabel(self):
		return self.label
	
	# Returning the value of the graph node
	def getValue(self):
		return self.value
	
	# Retuning the adjacent vertex list
	def getAdjacent(self):
		return self.adjacents.listOfValues()
	
	# Checking if the given vertex is adjacent
	def hasAdjacent(self, vertex):
		return self.adjacents.hasNode(vertex)
	
	# Adding an edge to the graph node
	def addAdjacent(self, vertex):
		if vertex != self.getLabel():
			self.adjacents.insertLast(vertex)
	
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
		self.filterAssets = DSALinkedList()
	
	# Finding a vertex in the graph
	def findVertex(self, value):
		vertex = None
		# Finding the vertex if it is present in the list of filtered assets
		if self.filterAssets.hasNode(value):
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
		# Finding the edge if it is present in the list of filterd assets
		if self.filterAssets.hasNode(fromValue.getLabel()) and self.filterAssets.hasNode(toValue.getLabel()):
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
		self.filterAssets.insertLast(label)

	# Adding an edge into the graph
	def addEdge(self, label1, label2, status):
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		vertex1.addAdjacent(label2)
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
	
	# Returning an edge in the graph
	def getEdge(self, label1, label2):
		edge = None
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		if vertex1 != None and vertex2 != None:
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
		isFound = False
		vertices = self.listOfFilterAssets()
		for label1 in vertices:
			if not isFound:
				for label2 in vertices:
					if (label1+label2) == tradeName:
						isFound = True
						edge = self.getEdge(label1, label2)
		return edge
	
	# Function to remove a vertex from a graph
	def removeVertex(self, inVertex):
		vertex = self.getVertex(inVertex)
		self.vertices.delete(vertex)
		# unfinished
	
	# ignore the given asset
	def ignoreAsset(self, inAsset):
		self.filterAssets.remove(inAsset);
	
	# re-add the given asset
	def addAsset(self, inAsset):
		self.filterAssets.insertLast(inAsset);
	
	# Function to check if the trade edge is tradeable
	def isTrading(self, tradeName):
		trading = False
		edge = self.getTradeEdge(tradeName)
		if edge and edge.getStatus() == 'TRADING':
			trading = True
		return trading
	
	# Function to find the exchange between the given assets - Note that this is a modified DFS 
	def _getDetails(self, labels, exchangeArray, pathExchange, quoteAsset):
		# Getting the last value from the labels list
		label = labels.peekLast()
		vertex = self.getVertex(label)
		# Marking the vertex as visited
		vertex.setVisited()
		adjData = self.getAdjacent(label) 
		# Checking if the adjacent list is not none and the trade path is not break            
		if adjData.size != 0 or self.isTrading(label+quoteAsset):
				for i, val in enumerate(adjData):
					if val == quoteAsset:
						# adding the quote asset to the path and appending to the trade list
						foundPath = copy.deepcopy(labels)
						foundPath.insertLast(quoteAsset)
						exchangeArray[0].insertLast(foundPath)
						# remove the quote asset from the list
						adjData = np.delete(adjData, i)
						# Adding the overall trade exchange
						edge = self.getEdge(label, quoteAsset)
						exchangeValue = edge.getPriceChange()
						pathExchange += float(exchangeValue)
						# exchangeList.insertLast(pathExchange)
						exchangeArray[1].insertLast(pathExchange)
						# Checking if it's the best exchange
						if pathExchange > float(exchangeArray[3]):
							exchangeArray[3] = pathExchange
							exchangeArray[2] = copy.deepcopy(foundPath)
					elif self.filterAssets.hasNode(val):
						newVertex = self.getVertex(val)
						# If the selected vertex is not visited, it is then added to the labels list and recursed for a new trade path
						if not newVertex.getVisited():
							# Making a copy of the label list for recursive looping
							newLabels = copy.deepcopy(labels)
							# Inserting the current label
							newLabels.insertLast(val)
							# Getting the edge
							edge = self.getEdge(label, val)
							# Getting the price change value of the edge
							exchangeValue = edge.getPriceChange()
							# Making a copy of the path exchange for recursive looping
							newPathExchange = copy.deepcopy(pathExchange)
							# Adding the current value to the path exchange
							newPathExchange += float(exchangeValue)
							exchangeArray = self._getDetails(newLabels, exchangeArray, newPathExchange, quoteAsset)
		return exchangeArray
	
	# Function to get the overall between two assets
	def getTradeDetails(self, baseAsset, quoteAsset):
		self.clearAllVisited()
		# Declaring an empty array
		resultArray = np.array([])
		# Getting the details if the nodes are not ignored
		if self.filterAssets.hasNode(baseAsset) and self.filterAssets.hasNode(quoteAsset):
			# List storing the overall exchange values of each trade
			exchangeList = DSALinkedList()
			# List of labels
			labelList = DSALinkedList()
			# List storing the various trade paths
			tradeList = DSALinkedList()
			# List storing the best trade path
			bestTrade = DSALinkedList()
			# Initializing the best trade and best exchange
			edge = self.getEdge(baseAsset, quoteAsset)
			if edge:
				bestExchange = edge.getPriceChange()
				bestTrade.insertLast(baseAsset)
				bestTrade.insertLast(quoteAsset)
			else:
				bestExchange = -1000.0 
			# Array storing the required inputs 
			exchangeArray = np.empty(4, dtype=object)
			exchangeArray[0] = tradeList
			exchangeArray[1] = exchangeList
			exchangeArray[2] = bestTrade
			exchangeArray[3] = bestExchange
			pathExchange = 0
			labelList.insertLast(baseAsset)
			# Calling the recursive function
			resultArray = self._getDetails(labelList, exchangeArray, pathExchange, quoteAsset)
		# returning the results
		return resultArray
	
	# Clearing all the visited vertices
	def clearAllVisited(self):
		vertices = self.filterAssets.listOfValues()
		for label in vertices:
			vertex = self.getVertex(label)
			vertex.clearVisited()

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
			edgesList = self.listOfEdgeValues()
			print(edgesList)
	
	# List of vertex labels in the graph
	def listOfVerticeLabels(self):
		vertexList = self.vertices.listOfValues()
		rtnList = np.empty(self.vertices.count(), dtype=object)
		if vertexList.size != 0:
			for i, val in enumerate(vertexList):
				rtnList[i] = val.getLabel()
		return rtnList
	
	# List of vertices in the graph
	def listOfVertices(self):
		return self.vertices.listOfValues()
	
	# List of filtered assets in the graph
	def listOfFilterAssets(self):
		return self.filterAssets.listOfValues()
	
	# List of filtered assets in the graph
	def listOfEdges(self):
		return self.edges.listOfValues()
	
	# List of edge values in the graph
	def listOfEdgeValues(self):
		edgeList = self.edges.listOfValues()
		rtnList = np.empty(self.edges.count(), dtype=object)
		if edgeList.size != 0:
			for i, edge in enumerate(edgeList):
				output = f'{edge.getFromVertex().getLabel()}{edge.getToVertex().getLabel()}'
				rtnList[i] = output
		return rtnList
	
	# Getting the first vertex of the graph
	def getFirstVertex(self):
		return self.vertices.peekFirst()

	# Shifting down values in the given array 
	def shiftDown(self, position, highValues, highLabels):
		for i in range(position+1, highValues.size):
			highValues[position], highValues[i] = highValues[i], highValues[position]
			highLabels[position], highLabels[i] = highLabels[i], highLabels[position]
	
	# Inserting the value into the array
	def insertHighValue(self, inLabel, inValue, highValues, highLabels):
		isInserted, i = False, 0
		while (not isInserted) and (i<highValues.size):
			if highValues[i] == None:
				highValues[i] = float(inValue)
				highLabels[i] = inLabel
				isInserted = True
			elif float(inValue) > highValues[i]:
				self.shiftDown(i, highValues, highLabels)
				highValues[i] = float(inValue)
				highLabels[i] = inLabel
				isInserted = True
			i += 1
	
	# Displaying the trade overview details
	def displayOverview(self, labels, values):
		for i in range(labels.size):
			print(f'{i+1}. {labels[i]} - {values[i]}')
		print()
					
	# Finding the Trade overview details
	def getTradeOverview(self):
		# Getting the list of edges
		edgeList = self.listOfEdges()
		# Initializing empty arrays for storing the top 10 values
		highestPriceChange = np.empty(10, dtype=object)
		highestPriceChangeLabels = np.empty(10, dtype=object)
		highestPriceChangePercent = np.empty(10, dtype=object)
		highestPriceChangePercentLabels = np.empty(10, dtype=object)
		highestWeightedAvgPrice = np.empty(10, dtype=object)
		highestWeightedAvgPriceLabels = np.empty(10, dtype=object)
		highestOpenPrice = np.empty(10, dtype=object)
		highestOpenPriceLabels = np.empty(10, dtype=object)
		highestHighPrice = np.empty(10, dtype=object)
		highestHighPriceLabels = np.empty(10, dtype=object)
		highestLowPrice = np.empty(10, dtype=object)
		highestLowPriceLabels = np.empty(10, dtype=object)
		highestVolume = np.empty(10, dtype=object)
		highestVolumeLabels = np.empty(10, dtype=object)
		highestQuoteVolume = np.empty(10, dtype=object)
		highestQuoteVolumeLabels = np.empty(10, dtype=object)
		highestCount = np.empty(10, dtype=object)
		highestCountLabels = np.empty(10, dtype=object)
		for edge in edgeList:
			label = edge.getEdgeLabel()
			fromVertex = edge.getFromVertex().getLabel()
			toVertex = edge.getToVertex().getLabel()
			# Inserting the highest values if it is not ignored
			if self.filterAssets.hasNode(fromVertex) and self.filterAssets.hasNode(toVertex):
				self.insertHighValue(label, edge.priceChange, highestPriceChange, highestPriceChangeLabels)
				self.insertHighValue(label, edge.priceChangePercent, highestPriceChangePercent, highestPriceChangePercentLabels)
				self.insertHighValue(label, edge.weightedAvgPrice, highestWeightedAvgPrice, highestWeightedAvgPriceLabels)
				self.insertHighValue(label, edge.openPrice, highestOpenPrice, highestOpenPriceLabels)
				self.insertHighValue(label, edge.highPrice, highestHighPrice, highestHighPriceLabels)
				self.insertHighValue(label, edge.lowPrice, highestLowPrice, highestLowPriceLabels)
				self.insertHighValue(label, edge.volume, highestVolume, highestVolumeLabels)
				self.insertHighValue(label, edge.quoteVolume, highestQuoteVolume, highestQuoteVolumeLabels)
				self.insertHighValue(label, edge.count, highestCount, highestCountLabels)
		# Printing out the top 10 values
		print('\nTop 10 Price Change')
		self.displayOverview(highestPriceChangeLabels, highestPriceChange)
		print('\nTop 10 Price Change Precent')
		self.displayOverview(highestPriceChangePercentLabels, highestPriceChangePercent)
		print('\nTop 10 Weighted Average Price')
		self.displayOverview(highestWeightedAvgPriceLabels, highestWeightedAvgPrice)
		print('\nTop 10 Open Price')
		self.displayOverview(highestOpenPriceLabels, highestOpenPrice)
		print('\nTop 10 High Price')
		self.displayOverview(highestHighPriceLabels, highestWeightedAvgPrice)
		print('\nTop 10 Low Price')
		self.displayOverview(highestLowPriceLabels, highestLowPrice)
		print('\nTop 10 Volume');
		self.displayOverview(highestVolumeLabels, highestVolume)
		print('\nTop 10 Quote Volume');
		self.displayOverview(highestQuoteVolumeLabels, highestQuoteVolume)
		print('\nTop 10 Count');
		self.displayOverview(highestCountLabels, highestCount)

