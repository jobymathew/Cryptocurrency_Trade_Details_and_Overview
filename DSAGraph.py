"""
FILE: DSAGraph.py - Modified for the assignment
AUTHOR: Joby Mathew
UNIT: COMP5008 Data Structures and Algorithms
PURPOSE: Provides a class for Graph Implementation which is to be used as cryptoGraph
REFERENCE: Lecture Slides
Last Mod: 23rd October, 2020
"""

from LinkedList import DSALinkedList
import numpy as np
# importing sys to increase the recursion limit
import sys
sys.setrecursionlimit(10**6) 
# importing copy to perform deep copy of classes
import copy


class DSAGraphEdge():
	
	"""
	* Default Constructor.
    * IMPORT: fromVertex (DSAGraphNode), toVertex (DSAGraphNode), status (String).
    * EXPORT: none.
    * USAGE: Initializing the values.
	"""
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
	
	"""
	* METHOD: getFromVertex.
    * IMPORT: none.
    * EXPORT: fromVertex (DSAGraphNode).
    * ASSERTION: none.
	"""
	def getFromVertex(self):
		return self.fromVertex
	
	"""
	* METHOD: getToVertex.
    * IMPORT: none.
    * EXPORT: toVertex (DSAGraphNode).
    * ASSERTION: none.
	"""
	def getToVertex(self):
		return self.toVertex
	
	"""
	* METHOD: getEdgeLabel.
    * IMPORT: none.
    * EXPORT: label (String).
    * ASSERTION: none.
	"""
	def getEdgeLabel(self):
		return self.fromVertex.getLabel()+self.toVertex.getLabel()
	
	"""
	* METHOD: getStatus.
    * IMPORT: none.
    * EXPORT: status (String).
    * ASSERTION: none.
	"""
	def getStatus(self):
		return self.status
	
	"""
	* METHOD: setVolume.
    * IMPORT: inVolume (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setVolume(self, inVolume):
		self.volume = inVolume
	
	"""
	* METHOD: setCount.
    * IMPORT: inCount (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setCount(self, inCount):
		self.count = inCount
	
	"""
	* METHOD: setWeightedAvgPrice.
    * IMPORT: inWeightedAvgPrice (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setWeightedAvgPrice(self, inWeightedAvgPrice):
		self.weightedAvgPrice = inWeightedAvgPrice

	"""
	* METHOD: getVolume.
    * IMPORT: none.
    * EXPORT: volume (float).
    * ASSERTION: none.
	"""
	def getVolume(self):
		return self.volume
	
	"""
	* METHOD: getCount.
    * IMPORT: none.
    * EXPORT: count (float).
    * ASSERTION: none.
	"""
	def getCount(self):
		return self.count
	
	"""
	* METHOD: getWeightedAvgPrice.
    * IMPORT: none.
    * EXPORT: weightedAvgPrice (float).
    * ASSERTION: none.
	"""
	def getWeightedAvgPrice(self):
		return self.weightedAvgPrice
	
	"""
	* METHOD: setQuoteVolume.
    * IMPORT: inQuoteVolume (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setQuoteVolume(self, inQuoteVolume):
		self.quoteVolume = inQuoteVolume
	
	"""
	* METHOD: getQuoteVolume.
    * IMPORT: none.
    * EXPORT: quoteVolume (float).
    * ASSERTION: none.
	"""
	def getQuoteVolume(self):
		return self.quoteVolume
	
	"""
	* METHOD: setOpenPrice.
    * IMPORT: inOpenPrice (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setOpenPrice(self, inOpenPrice):
		self.openPrice = inOpenPrice
	
	"""
	* METHOD: getOpenPrice.
    * IMPORT: none.
    * EXPORT: openPrice (float).
    * ASSERTION: none.
	"""
	def getOpenPrice(self):
		return self.openPrice
	
	"""
	* METHOD: setHighPrice.
    * IMPORT: inHighPrice (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setHighPrice(self, inHighPrice):
		self.highPrice = inHighPrice
	
	"""
	* METHOD: getHighPrice.
    * IMPORT: none.
    * EXPORT: highPrice (float).
    * ASSERTION: none.
	"""
	def getHighPrice(self):
		return self.highPrice
	
	"""
	* METHOD: setLowPrice.
    * IMPORT: inLowPrice (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setLowPrice(self, inLowPrice):
		self.lowPrice = inLowPrice
	
	"""
	* METHOD: getLowPrice.
    * IMPORT: none.
    * EXPORT: lowPrice (float).
    * ASSERTION: none.
	"""
	def getLowPrice(self):
		return self.lowPrice
	
	"""
	* METHOD: setPriceChange.
    * IMPORT: inPriceChange (float).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setPriceChange(self, inPriceChange):
		self.priceChange = inPriceChange
	
	"""
	* METHOD: getPriceChange.
    * IMPORT: none.
    * EXPORT: priceChange (float).
    * ASSERTION: none.
	"""
	def getPriceChange(self):
		return self.priceChange
	
	"""
	* METHOD: setPriceChangePercent.
    * IMPORT: inPriceChangePercent.
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setPriceChangePercent(self, inPriceChangePercent):
		self.priceChangePercent = inPriceChangePercent
	
	"""
	* METHOD: getPriceChangePercent.
    * IMPORT: none.
    * EXPORT: priceChangePercent (float).
    * ASSERTION: none.
	"""
	def getPriceChangePercent(self):
		return self.priceChangePercent


class DSAGraphNode():

	"""
	* DEFAULT Constructor.
    * IMPORT: inLabel (String), inValue (int).
    * EXPORT: none.
    * ASSERTION: Initalizing all the values.
	"""
	def __init__(self, inLabel, inValue):
		self.label = inLabel
		self.value = inValue
		self.adjacents = DSALinkedList()
		self.visited = False
	
	"""
	* METHOD: getAdjacents.
    * IMPORT: none.
    * EXPORT: adjacents (DSALinkedList).
    * USAGE: Return the list of adjacent vertices.
	"""
	def getAdjacents(self):
		return self.adjacents

	"""
	* METHOD: getLabel.
    * IMPORT: none.
    * EXPORT: label (String).
    * ASSERTION: none.
	"""
	def getLabel(self):
		return self.label
	
	"""
	* METHOD: getValue.
    * IMPORT: none.
    * EXPORT: value (int).
    * ASSERTION: none.
	"""
	def getValue(self):
		return self.value
	
	"""
	* METHOD: getAdjacent.
    * IMPORT: none.
    * EXPORT: AdjacentList[] (String).
    * USAGE: Returns the list of labels.
	"""
	def getAdjacent(self):
		return self.adjacents.listOfValues()
	
	"""
	* METHOD: hasAdjacent.
    * IMPORT: vertex (String).
    * EXPORT: True/False (Boolean).
    * USAGE: Checking if the given vertex is adjacent.
	"""
	def hasAdjacent(self, vertex):
		return self.adjacents.hasNode(vertex)
	
	"""
	* METHOD: addAdjacent.
    * IMPORT: vertex (String).
    * EXPORT: none.
    * USAGE: Adding an edge to the graph node.
	"""
	def addAdjacent(self, vertex):
		if vertex != self.getLabel():
			self.adjacents.insertLast(vertex)
	
	"""
	* METHOD: setVisited.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Setting the vertex as visited.
	"""
	def setVisited(self):
		self.visited = True
	
	"""
	* METHOD: clearVisited.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Clearing the vertex visit.
	"""
	def clearVisited(self):
		self.visited = False
	
	"""
	* METHOD: getVisited.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Checking if the node is visited or not.
	"""
	def getVisited(self):
		return self.visited


class DSAGraph():

	"""
	* DEFAULT Constructor.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Initializing the graph.
	"""
	def __init__(self):
		self.vertices = DSALinkedList()
		self.edges = DSALinkedList()
		self.filterAssets = DSALinkedList()
	
	"""
	* METHOD: findVertex.
    * IMPORT: value (String).
    * EXPORT: none.
    * USAGE: Finding a vertex in the graph.
	"""
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
	
	"""
	* METHOD: findEdge.
    * IMPORT: fromValue (String), toValue (String).
    * EXPORT: none.
    * USAGE: Finding an edge in the graph.
	"""
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

	"""
	* METHOD: addVertex.
    * IMPORT: label (String), value (int).
    * EXPORT: none.
    * USAGE: Adding a vertex into the graph.
	"""
	def addVertex(self, label, value):
		vertex = DSAGraphNode(label, value)
		self.vertices.insertLast(vertex)
		self.filterAssets.insertLast(label)

	"""
	* METHOD: addEdge.
    * IMPORT: label1 (String), label2 (String), status (String).
    * EXPORT: none.
    * USAGE: Adding an edge into the graph.
	"""
	def addEdge(self, label1, label2, status):
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		vertex1.addAdjacent(label2)
		edge = DSAGraphEdge(vertex1, vertex2, status)
		self.edges.insertLast(edge)

	"""
	* METHOD: hasVertex.
    * IMPORT: label (String).
    * EXPORT: isPresent (Boolean).
    * USAGE: Checking if a vertex is present in the graph.
	"""
	def hasVertex(self, label):
		k = self.findVertex(label)
		isPresent = True
		if k == None:
			isPresent = False
		return isPresent
	
	"""
	* METHOD: hasEdge.
    * IMPORT: label1 (String), label2 (String).
    * EXPORT: isPresent (Boolean).
    * USAGE: Checking if an edge is present in the graph.
	"""
	def hasEdge(self, label1, label2):
		isPresent = True
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		edge = self.findEdge(vertex1, vertex2)
		if edge == None:
			isPresent = False
		return isPresent
	
	"""
	* METHOD: getVertexCount.
    * IMPORT: none.
    * EXPORT: count (int).
    * USAGE: Returns the number of vertices in the graph.
	"""
	def getVertexCount(self):
		return self.vertices.count()
	
	"""
	* METHOD: getEdgeCount.
    * IMPORT: none.
    * EXPORT: count (int).
    * USAGE: Returns the number of edges in the graph.
	"""
	def getEdgeCount(self):
		return self.edges.count()
	
	"""
	* METHOD: getVertex.
    * IMPORT: label (String).
    * EXPORT: vertex (DSAGraphNode).
    * USAGE: Find and return the vertex in the graph.
	"""
	def getVertex(self, label):
		vertex = self.findVertex(label)
		return vertex
	
	"""
	* METHOD: getVertex.
    * IMPORT: label1 (String), label2 (String).
    * EXPORT: edge (DSAGraphEdge).
    * USAGE: Find and return the edge in the graph.
	"""
	def getEdge(self, label1, label2):
		edge = None
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		if vertex1 != None and vertex2 != None:
			edge = self.findEdge(vertex1, vertex2)
		return edge
	
	"""
	* METHOD: hasTradeEdge.
    * IMPORT: tradeName (String).
    * EXPORT: isFound (Boolean).
    * USAGE: Check if the trade edge exists in the graph.
	"""
	def hasTradeEdge(self, tradeName):
		isFound = False
		if self.getTradeEdge(tradeName):
			isFound = True
		return isFound
	
	"""
	* METHOD: getTradeEdge.
    * IMPORT: tradeName (String).
    * EXPORT: edge (DSAGraphEdge).
    * USAGE: Get the trade edge from the graph.
	"""
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
	
	"""
	* METHOD: ignoreAsset.
    * IMPORT: inAsset (String).
    * EXPORT: none.
    * USAGE: ignore the given asset.
	"""
	def ignoreAsset(self, inAsset):
		self.filterAssets.remove(inAsset);
	
	"""
	* METHOD: addAsset.
    * IMPORT: inAsset (String).
    * EXPORT: none.
    * USAGE: Re-add the given asset.
	"""
	def addAsset(self, inAsset):
		self.filterAssets.insertLast(inAsset);
	
	"""
	* METHOD: isTrading.
    * IMPORT: tradeName (String).
    * EXPORT: trading (Boolean).
    * USAGE: Check if the edge is tradable.
	"""
	def isTrading(self, tradeName):
		trading = False
		edge = self.getTradeEdge(tradeName)
		if edge and edge.getStatus() == 'TRADING':
			trading = True
		return trading
	
	"""
	* METHOD: _getDetails.
    * IMPORT: labels (String[]), exchangeArray (Object[]), pathExchange (float), quoteAsset (String).
    * EXPORT: exchangeArray (Object[]).
    * USAGE: find the exchange between the given assets. This is a modified DFS.
	"""
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
	
	"""
	* METHOD: getTradeDetails.
    * IMPORT: baseAsset (String), quoteAsset (String).
    * EXPORT: resultArray (Object[]).
    * USAGE: Get the overall exchange between the two assets and their trade paths.
	"""
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
	
	"""
	* METHOD: clearAllVisited.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Clearing all the visited vertices.
	"""
	def clearAllVisited(self):
		vertices = self.filterAssets.listOfValues()
		for label in vertices:
			vertex = self.getVertex(label)
			vertex.clearVisited()

	"""
	* METHOD: getAdjacent.
    * IMPORT: label (String).
    * EXPORT: none.
    * USAGE: Retruning the list of adjacent vertices of the vertex - returns the labels.
	"""
	def getAdjacent(self, label):
		adjacentVertex = np.array([])
		vertex = self.findVertex(label)
		if vertex:
			adjacentVertex = vertex.getAdjacent()
		return adjacentVertex
	
	"""
	* METHOD: displayAdjacent.
    * IMPORT: label (String).
    * EXPORT: none.
    * USAGE: Print the list of adjacent vertices of the vertex - prints the labels.
	"""
	def displayAdjacent(self, label):
		adjacentVertex = self.getAdjacent(label)
		print(adjacentVertex)
		

	"""
	* METHOD: getAdjacentE.
    * IMPORT: labels (String).
    * EXPORT: none.
    * USAGE: Return the list of adjacent edges of the vertex.
	"""
	def getAdjacentE(self, label1):
		adjacentEdges = DSALinkedList()
		vertex1 = self.findVertex(label1)
		if vertex1:
			adjacentVertices =  vertex1.getAdjacent()
			if adjacentVertices:
				for label2 in adjacentVertices:
					if self.hasEdge(label1, label2):
						adjacentEdges.insertLast(label1+label2)
		return adjacentEdges.listOfValues()
	
	"""
	* METHOD: isAdjacent.
    * IMPORT: label1 (String), label2 (String).
    * EXPORT: isAnEdge (Boolean).
    * USAGE: Checking if a vertex is adjacent to the other.
	"""
	def isAdjacent(self, label1, label2):
		isAnEdge = False
		vertex1 = self.findVertex(label1)
		vertex2 = self.findVertex(label2)
		if self.hasEdge(label1, label2):
			isAnEdge = True
		return isAnEdge
	
	"""
	* METHOD: display.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Displaying the graph.
	"""
	def display(self):
		if not self.vertices.isEmpty():
			print('Vertices of the graph')
			verticesList = self.listOfVertices()
			for val in verticesList:
				print(val.getLabel(), end=" ")
			print()

		if not self.edges.isEmpty():
			print('Edges of the graph')
			edgesList = self.listOfEdgeValues()
			for val in edgesList:
				print(val, end=" ")
			print()	
	"""
	* METHOD: listOfVerticeLabels.
    * IMPORT: none.
    * EXPORT: rtnList[] (String).
    * USAGE: List of vertex labels in the graph.
	"""
	def listOfVerticeLabels(self):
		vertexList = self.vertices.listOfValues()
		rtnList = np.empty(self.vertices.count(), dtype=object)
		if vertexList.size != 0:
			for i, val in enumerate(vertexList):
				rtnList[i] = val.getLabel()
		return rtnList
	
	"""
	* METHOD: listOfVertices.
    * IMPORT: none.
    * EXPORT: verticesList[] (DSAGraphNode).
    * USAGE: List of vertices in the graph.
	"""
	def listOfVertices(self):
		return self.vertices.listOfValues()
	
	"""
	* METHOD: listOfFilterAssets.
    * IMPORT: none.
    * EXPORT: filterAssetsList[] (String).
    * USAGE: List of filtered assets in the graph.
	"""
	def listOfFilterAssets(self):
		return self.filterAssets.listOfValues()
	
	"""
	* METHOD: listOfEdges.
    * IMPORT: none.
    * EXPORT: filterAssetsList[] (DSAGraphEdge).
    * USAGE: List of edges in the graph.
	"""
	def listOfEdges(self):
		return self.edges.listOfValues()
	
	"""
	* METHOD: listOfEdgeValues.
    * IMPORT: none.
    * EXPORT: rtnList[] (String).
    * USAGE: List of edges Values in the graph.
	"""
	def listOfEdgeValues(self):
		edgeList = self.edges.listOfValues()
		rtnList = np.empty(self.edges.count(), dtype=object)
		if edgeList.size != 0:
			for i, edge in enumerate(edgeList):
				output = f'{edge.getFromVertex().getLabel()}{edge.getToVertex().getLabel()}'
				rtnList[i] = output
		return rtnList
	
	"""
	* METHOD: getFirstVertex.
    * IMPORT: none.
    * EXPORT: firstVertex (DSAGraphNode).
	"""
	def getFirstVertex(self):
		return self.vertices.peekFirst()

	"""
	* METHOD: _shiftDown.
    * IMPORT: position (int), highValues[] (float), highLabels[] (String).
    * EXPORT: none.
	* USAGE: Shifting down values in the given array
	"""
	def _shiftDown(self, position, highValues, highLabels):
		for i in range(position+1, highValues.size):
			highValues[position], highValues[i] = highValues[i], highValues[position]
			highLabels[position], highLabels[i] = highLabels[i], highLabels[position]
	
	"""
	* METHOD: _insertHighValue.
    * IMPORT: inLabel (String), inValue (float) ,highValues[] (float), highLabels[] (String).
    * EXPORT: none.
	* USAGE: Inserting the value into the array
	"""
	def _insertHighValue(self, inLabel, inValue, highValues, highLabels):
		isInserted, i = False, 0
		while (not isInserted) and (i<highValues.size):
			if highValues[i] == None:
				highValues[i] = float(inValue)
				highLabels[i] = inLabel
				isInserted = True
			elif float(inValue) > highValues[i]:
				self._shiftDown(i, highValues, highLabels)
				highValues[i] = float(inValue)
				highLabels[i] = inLabel
				isInserted = True
			i += 1
	
	"""
	* METHOD: displayOverview.
    * IMPORT: labels[] (String), values[] (float).
    * EXPORT: none.
	* USAGE: Displaying the trade overview details
	"""
	def displayOverview(self, labels, values):
		for i in range(labels.size):
			print(f'{i+1}. {labels[i]} - {values[i]}')
		print()
					
	"""
	* METHOD: getTradeOverview.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: Finding the trade overview details
	"""
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
				self._insertHighValue(label, edge.priceChange, highestPriceChange, highestPriceChangeLabels)
				self._insertHighValue(label, edge.priceChangePercent, highestPriceChangePercent, highestPriceChangePercentLabels)
				self._insertHighValue(label, edge.weightedAvgPrice, highestWeightedAvgPrice, highestWeightedAvgPriceLabels)
				self._insertHighValue(label, edge.openPrice, highestOpenPrice, highestOpenPriceLabels)
				self._insertHighValue(label, edge.highPrice, highestHighPrice, highestHighPriceLabels)
				self._insertHighValue(label, edge.lowPrice, highestLowPrice, highestLowPriceLabels)
				self._insertHighValue(label, edge.volume, highestVolume, highestVolumeLabels)
				self._insertHighValue(label, edge.quoteVolume, highestQuoteVolume, highestQuoteVolumeLabels)
				self._insertHighValue(label, edge.count, highestCount, highestCountLabels)
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

