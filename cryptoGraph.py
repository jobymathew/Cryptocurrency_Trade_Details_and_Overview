import sys
import argparse
import numpy as np
import requests
# Minh Dao - Tutor Sophie Lee-Goh
# Using the Graph class which I made during the practicals
from DSAGraph import DSAGraph
from LinkedList import DSALinkedList
import json

# Getting the data from the API
# tradeInfo = requests.get('https://www.binance.com/api/v3/ticker/24hr')
# exchangeInfo = requests.get('https://www.binance.com/api/v3/exchangeInfo')
# tokenTrades = requests.get('https://www.binance.com/api/v3/trades?symbol=ETHBTC')

# declaring the graph object
graph = DSAGraph()

# Converting to json
tradeFile = open('tradeInfo.json')
exchangeFile = open('exchangeInfo.json')
trade_data = json.load(tradeFile)
exchange_data = json.load(exchangeFile)
# tokenTrades_data = tokenTrades.json()


# Setting up the argument parser
ap = argparse.ArgumentParser()
# Adding the argument for interactive test enviornment
ap.add_argument("-i", "--interactive", help='interactive testing enviornment', action='store_true')
# Adding the argument for report mode
ap.add_argument("-r", "--report", help='report mode', action='store_true')

# Getting the argument variables
args = vars(ap.parse_args())

# Function to load the exchange data (asset data)
def loadAssetData():
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

def loadTradeData():
	for data in trade_data:
		tradeName = data['symbol']
		tradeEdge = graph.getTradeEdge(tradeName)
		volume = data['volume']
		count = data['count']
		weightedAvgPrice = data['weightedAvgPrice']
		tradeEdge.setVolume(volume)
		tradeEdge.setCount(count)
		tradeEdge.setWeightedAvgPrice(weightedAvgPrice)
	print('Trade data has been loaded')

def getLoadOptions():
	choice = 0
	while(choice != 4):
		print('\n(1) Asset data\n(2) Trade data\n(3) Serialised Data\n(4) Exit')
		choice = int(input())
		if choice == 1:
			loadAssetData()
		elif choice == 2:
			loadTradeData()
		elif choice == 3:
			print('Serialized data')
		elif choice == 4:
			print('Exitting to the main menu\n')
		else:
			print('Wrong input, please try again\n')

# Function to display details related to the trade
def displayTradeDetails():
	print("Input the trade name")
	tradeName = input()
	if graph.hasTradeEdge(tradeName):
		graphEdge = graph.getTradeEdge(tradeName)
		print('\nStatus:', graphEdge.getStatus())
		print('Volume:', graphEdge.getVolume())
		print('Count:', graphEdge.getCount())
		print('Weighted Average Price:', graphEdge.getWeightedAvgPrice())
	else:
		print("Trade doesn't exist")

# Function to display the details related to the asset
def dispalyAssetDeatils():
	print("Input the asset name")
	assetName = input()
	if graph.hasVertex(assetName):
		vertex = graph.getVertex(assetName)
		print('\nTotal Price Change:', vertex.getTotalPriceChange())
		print('Average Price Change:', vertex.getAveragePriceChange())
		print('Average Price Percent Change:', vertex.getAveragePriceChangePercent())
		print('Total Volume traded:', vertex.getTotalVolume())
		print('Average Volume traded:', vertex.getAverageVolume())
		print('Total Count traded:', vertex.getTotalCount())
		print('Average Count traded:', vertex.getAverageCount())
		print()
	else:
		print("\nAsset doesn't exist\n")

def displayTradePaths():
	# getting the base asset and quote asset from the user
	print("Enter the base asset")
	baseAsset = input()
	print("Enter the quote asset")
	quoteAsset = input()
	# Getting the trade list
	tradeList = graph.getTradePaths(baseAsset, quoteAsset)
	# Displaying the trade paths if present, else displaying no trade paths
	if tradeList.isEmpty():
		print('\nNo Trade Paths\n')
	else:
		print("\nTrade paths\n")
		tradePath = tradeList.head
		while(tradePath != None):
			trade = tradePath.getValue().head
			while(trade != None):
				print(trade.getValue(), end=' ')
				trade = trade.getNext()
			print()
			tradePath = tradePath.getNext()

	
# Entering the interactive mode
if args['interactive']:
	print('Entering interactive mode')
	# selecting the choice from the menu driven options
	choice = 0
	while(choice != 9):
		print('\n(1) Load Data\n\t-Asset data\n\t-Trade data\n\t-Serialised Data\n(2) Find and display asset\n(3) Find and display trade details\n(4) Find and display potential trade paths\n(5) Set asset filter\n(6) Asset overview\n(7) Trade overview\n(8) Save data (serialised)\n(9) Exit')
		choice = int(input())
		if choice == 1:
			getLoadOptions()
		elif choice == 2:
			displayAssetDetails()
		elif choice == 3:
			displayTradeDetails()
		elif choice == 4:
			displayTradePaths()
		elif choice == 5:
			print('asset filter')
		elif choice == 6:
			print('asset overview')
		elif choice == 7:
			print('Trade overview')
		elif choice == 8:
			print('Save data serailized')
		elif choice == 9:
			print('Exitting')
		else:
			print('\nInvalid choice, please try again')
			

# Entering the report mode
elif args['report']:
	print('Entering report mode')
	

	


# Showing the usage information
else:
	ap.print_help(sys.stderr)
	sys.exit(1)

