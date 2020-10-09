import numpy as np
import requests
# Minh Dao - Tutor Sophie Lee-Goh
# Using the Graph class which I made during the practicals
from DSAGraph import DSAGraph
from LinkedList import DSALinkedList
import json

graph = DSAGraph()

# Converting to json
tradeFile = open('tradeInfo.json')
exchangeFile = open('exchangeInfo.json')
trade_data = json.load(tradeFile)
exchange_data = json.load(exchangeFile)
# tokenTrades_data = tokenTrades.json()


# count = {}
# for data in exchange_data['symbols']:
# 	count[data['quoteAsset']] = 0
# for data in exchange_data['symbols']:
# 	count[data['quoteAsset']] += 1

# print('Count of assets')
# for data in count:
# 	print(data, count[data])

# count = {}
# for data in trade_data:
# 	count[data['symbol']] = 0
# for data in trade_data:
# 	count[data['symbol']] += 1

# print('Count of trades')
# for data in count:
# 	print(data, count[data])

for data in exchange_data['symbols']:
	baseAsset = data['baseAsset']
	quoteAsset = data['quoteAsset']
	status = data['status']
	if not graph.hasVertex(baseAsset):
		graph.addVertex(baseAsset, 0)
	if not graph.hasVertex(quoteAsset):
		graph.addVertex(quoteAsset, 0)
	graph.addEdge(baseAsset, quoteAsset, status)
print('Asset data has been loaded')

for data in trade_data:
	tradeName = data['symbol']
	tradeEdge = graph.getTradeEdge(tradeName)
	fromVertex = tradeEdge.getFromVertex()
	priceChange = data['priceChange']
	fromVertex.addPriceChange(priceChange)
	priceChangePercent = data['priceChangePercent']
	fromVertex.addPriceChangePercent(priceChangePercent)
	volume = data['volume']
	fromVertex.addVolume(volume)
	count = data['count']
	fromVertex.addCount(count)
	weightedAvgPrice = data['weightedAvgPrice']
	tradeEdge.setVolume(volume)
	tradeEdge.setCount(count)
	tradeEdge.setWeightedAvgPrice(weightedAvgPrice)
print('Trade data has been loaded')

# for _ in range(5):
print("Input the asset name")
assetName = input()
if graph.hasVertex(assetName):
	vertex = graph.getVertex(assetName)
	print('\n24H Price Change:', vertex.getTotalPriceChange())
	print('24H Average Price Change:', vertex.getAveragePriceChange())
	print('24H Average Price Percent Change:', vertex.getAveragePriceChangePercent())
	print('24H Volume traded:', vertex.getTotalVolume())
	print('24H Average Volume traded:', vertex.getAverageVolume())
	print('24H Total Count traded:', vertex.getTotalCount())
	print('24H Average Count traded:', vertex.getAverageCount())
	print()
else:
	print("\nAsset doesn't exist\n")



# # getting the base asset and quote asset from the user
# print("Enter the base asset")
# baseAsset = input()
# print("Enter the quote asset")
# quoteAsset = input()
# # Getting the trade list
# tradeList = graph.getTradePaths(baseAsset, quoteAsset)
# # Displaying the trade paths if present, else displaying no trade paths
# if tradeList.isEmpty():
# 	print('\nNo Trade Paths\n')
# else:
# 	print("\nTrade paths\n")
# 	tradePath = tradeList.head
# 	while(tradePath != None):
# 		trade = tradePath.getValue().head
# 		while(trade != None):
# 			print(trade.getValue(), end=' ')
# 			trade = trade.getNext()
# 		print()
# 		tradePath = tradePath.getNext()	

