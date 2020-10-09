import numpy as np
import requests
# Minh Dao - Tutor Sophie Lee-Goh
# Using the Graph class which I made during the practicals
from DSAGraph import DSAGraph
from LinkedList import DSALinkedList
import json

graph = DSAGraph()

# Converting to json
tradeFile = open('trade_file.json')
exchangeFile = open('asset_file.json')
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
	priceChangePercent = data['priceChangePercent']
	volume = data['volume']
	count = data['count']
	# Adding data to the node class
	fromVertex.addVolume(volume)
	fromVertex.addPriceChangePercent(priceChangePercent)
	fromVertex.addPriceChange(priceChange)
	fromVertex.addCount(count)
	quoteVolume = data['quoteVolume']
	lowPrice = data['lowPrice']
	highPrice = data['highPrice']
	openPrice = data['openPrice']
	weightedAvgPrice = data['weightedAvgPrice']
	# Adding data to the edge class
	tradeEdge.setVolume(volume)
	tradeEdge.setPriceChange(priceChange)
	tradeEdge.setPriceChangePercent(priceChangePercent)
	tradeEdge.setQuoteVolume(quoteVolume)
	tradeEdge.setLowPrice(lowPrice)
	tradeEdge.setHighPrice(highPrice)
	tradeEdge.setOpenPrice(openPrice)
	tradeEdge.setCount(count)
	tradeEdge.setWeightedAvgPrice(weightedAvgPrice)
print('Trade data has been loaded')

# for _ in range(5):
print("Input the asset name")
assetName = input()
if graph.hasVertex(assetName):
	vertex = graph.getVertex(assetName)
	if (vertex.getTotalPriceChange() == 0):
		print('No data as there is no trading')
	else:
		print('\n24H Total Price Change :', vertex.getTotalPriceChange())
		print('24H Average Price Change :', vertex.getAveragePriceChange())
		print('24H Average Price Percent Change : ', vertex.getAveragePriceChangePercent())
		print('24H Total Volume traded :', vertex.getTotalVolume())
		print('24H Average Volume traded :', vertex.getAverageVolume())
		print('24H Total Count traded :', vertex.getTotalCount())
		print('24H Average Count traded :', vertex.getAverageCount())
		print()
else:
	print("\nAsset doesn't exist\n")

# Getting the input from the user
print("Input the trade name")
tradeName = input()
# Checking if trade edge exists
if graph.hasTradeEdge(tradeName):
	graphEdge = graph.getTradeEdge(tradeName)
	# Getting the two assets 
	baseAsset = graphEdge.getFromVertex()
	quoteAsset = graphEdge.getToVertex()
	# Displaying the trade details
	print('\nStatus :', graphEdge.getStatus())
	if graphEdge.getStatus() == 'TRADING':
		print('24H Price :', graphEdge.getWeightedAvgPrice())
		print(f'24H Price Change :', graphEdge.getPriceChange())
		print(f'24H Price Change Percent :', graphEdge.getPriceChangePercent())
		print(f'24H High Price :', graphEdge.getHighPrice())
		print(f'24H Low Price :', graphEdge.getLowPrice())
		print(f'24H Volume ({baseAsset.getLabel()}) : {graphEdge.getVolume()}')
		print(f'24H Volume ({quoteAsset.getLabel()}) : {graphEdge.getQuoteVolume()}')
		print(f'24H Count :', graphEdge.getCount())
	else:
		print('No data as there is no trading')
else:
	print("Trade doesn't exist")


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

