# sys and argparse to implement argument parsing
import sys
import argparse
import numpy as np
import pickle
# importing copy to perform deep copy of classes
import copy
# importing csv to read the csv file
import csv
# Minh Dao - Tutor Sophie Lee-Goh
# Using the Graph class which I made during the practicals - Modified for the assignment
from DSAGraph import DSAGraph
from Asset import AssetObject
import json

# Setting up the argument parser
ap = argparse.ArgumentParser()
# Adding the argument for interactive test enviornment
ap.add_argument("-i", "--interactive", help='interactive testing enviornment', action='store_true')
# Adding the argument for report mode
ap.add_argument("-r", "--report", nargs='+', help='report mode')

# Getting the argument variables
args = vars(ap.parse_args())

# Function to load the exchange data (asset data)
def loadAssetData():
	for i, row in enumerate(asset_data):
		if i != 0 and i != 1:
			circulatingSupply = None
			if row[7] == '?':
				circulatingSupply = '0'
			else:
				circulatingSupply = row[7]
			volume = None
			if row[8] == '$?':
				volume = '0'
			else:
				volumeSplit = row[8][1:].strip().split(',')
				volume = ''
				for val in volumeSplit:
					volume += val
			if i < 10:
				priceSplit = row[5][1:].strip().split(',')
				price = ''
				for val in priceSplit:
					price += val
			assets.addAsset(row[1].strip(), row[2].strip(), row[4].strip(), price, circulatingSupply.strip(), volume, row[9][:-1].strip(), row[10][:-1].strip(), row[11][:-1].strip())

# Function to load the trade data
def loadTradeData():
	for data in exchange_data['symbols']:
		baseAsset = data['baseAsset']
		quoteAsset = data['quoteAsset']
		status = data['status']
		if not graph.hasVertex(baseAsset):
			graph.addVertex(baseAsset, 0)
		if not graph.hasVertex(quoteAsset):
			graph.addVertex(quoteAsset, 0)
		graph.addEdge(baseAsset, quoteAsset, status)
	
	for data in trade_data:
		tradeName = data['symbol']
		tradeEdge = graph.getTradeEdge(tradeName)
		fromVertex = tradeEdge.getFromVertex()
		priceChange = data['priceChange']
		priceChangePercent = data['priceChangePercent']
		volume = data['volume']
		count = data['count']
		weightedAvgPrice = data['weightedAvgPrice']
		# Adding data to the node class
		fromVertex.addVolume(volume)
		fromVertex.addPriceChangePercent(priceChangePercent)
		fromVertex.addPriceChange(priceChange)
		fromVertex.addCount(count)
		fromVertex.addWeightedAvgPrice(weightedAvgPrice)
		quoteVolume = data['quoteVolume']
		lowPrice = data['lowPrice']
		highPrice = data['highPrice']
		openPrice = data['openPrice']
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

# Function to show the data loading options
def getLoadOptions():
	choice = 0
	while(choice != 4):
		print('\n(1) Asset data\n(2) Trade data\n(3) Serialised Data\n(4) Exit')
		choice = int(input())
		if choice == 1:
			loadAssetData()
			print('Asset data has been loaded')
		elif choice == 2:
			loadTradeData()
			print('Trade data has been loaded')
		elif choice == 3:
			readFromSerializedFile()
		elif choice == 4:
			print('Exitting to the main menu\n')
		else:
			print('Wrong input, please try again\n')

# Function to display details related to the trade
def displayTradeDetails():
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

# Function to display the details related to the asset
def displayAssetDetails():
	print("Input the asset name")
	assetName = input()
	if assets.hasAsset(assetName):
		asset = assets.getAsset(assetName)
		print('Name:', asset.getName())
		print('Market Cap:', asset.getMarketCap())
		print('Price:', asset.getPrice())
		print('Circulating Supply:', asset.getCirculatingSupply())
		print('Volume:', asset.getVolume())
		print('One Hour Percent:'+asset.getOneHourPercent()+'%')
		print('Twenty Four Hour Percent:'+asset.getTwentyFourHourPercent()+'%')
		print('Seven Day Percent:'+asset.getSevenDayPercent()+'%')
	else:
		print("\nAsset doesn't exist\n")

# Function to compute and display the trade paths 
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

# Function to read from serialized file
def readFromSerializedFile():
	try:
		with open('serializedCrytoGraph.txt', 'rb') as dataFile:
			#loading the file 
			inGraph = pickle.load(dataFile)
			graph = inGraph
			print("Graph has been read from the Serialized File")
	except:
		print("Error: object file does not exist")

# Function to write to file with serialization
def writeToSerializedFile():
	try:
		# Writing in the serialized file
		with open('serializedCrytoGraph.txt', 'wb') as dataFile:
			pickle.dump(filterGraph, dataFile)
			print('Graph has been written into the serialized file')
	except:
		print("Error: problem pickling object!")

# Function to filter an asset
def assetFilter():
	choice = 0
	# Getting the input from the user
	print('\nEnter 1 for including an asset and 2 for ignoring an asset')
	while(choice != 1 and choice != 2):
		choice = int(input())
		if choice!= 1 and choice!= 2:
			print('Wrong input, please try again\n')
	print('Enter the asset name')
	asset = input()
	if choice == 1:
		# checking if the asset is already present, else adding it back
		if graph.hasVertex(asset):
			print(f'{asset} already present in the graph')
		else:
			graph.addAsset(asset)
			print(f'{asset} has been included in the graph')
	else:
		# ignoring the asset and its edges if it is present in the graph
		if graph.hasVertex(asset):
			graph.ignoreAsset(asset)
			print(f'{asset} has been ignored from the graph')
		else:
			print(f'{asset} already ignored from the graph')



# Entering the interactive mode
if args['interactive']:

	# declaring the graph object
	graph = DSAGraph()
	# declaring the asset object
	assets = AssetObject()

	asset_file =  open('asset_info.csv') 
	# Reading the csv
	asset_data = csv.reader(asset_file)
	# Reading trade files and converting to json
	tradeFile = open('trade_file.json')
	exchangeFile = open('asset_file.json')
	trade_data = json.load(tradeFile)
	exchange_data = json.load(exchangeFile)

	# selecting the choice from the menu driven options
	choice = 0
	while(choice != 9):
		print('\n----------Trade Menu----------\n(1) Load Data\n\t-Asset data\n\t-Trade data\n\t-Serialised Data\n(2) Find and display asset\n(3) Find and display trade details\n(4) Find and display potential trade paths\n(5) Set asset filter\n(6) Asset overview\n(7) Trade overview\n(8) Save data (serialised)\n(9) Exit')
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
			assetFilter()
		elif choice == 6:
			assets.getAssetOverview()
		elif choice == 7:
			graph.getTradeOverview()
		elif choice == 8:
			writeToSerializedFile()
		elif choice == 9:
			print('Goodbye')
		else:
			print('\nInvalid choice, please try again')
			

# Entering the report mode
elif args['report']:

	# declaring the graph object
	graph = DSAGraph()

	# Converting to json
	tradeFile = open(args['report'][1])
	exchangeFile = open(args['report'][0])
	trade_data = json.load(tradeFile)
	exchange_data = json.load(exchangeFile)
	loadAssetData()
	loadTradeData()
	print("\nAsset Overview")
	graph.getAssetOverview()
	print("\nTrade Overview")
	graph.getTradeOverview()
	
# Showing the usage information
else:
	ap.print_help(sys.stderr)
	sys.exit(1)

