
import numpy as np
from LinkedList import DSALinkedList

class Asset():

	# initializing the constructor
	def __init__(self, inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent):
		self.name = inName
		self.label = inLabel
		self.marketCap = float(inMarketCap)
		self.price = float(inPrice)
		self.circulatingSupply = float(inCirculatingSupply)
		self.volume = float(inVolume)
		self.oneHourPercent = inOneHourPercent
		self.twentyFourHourPercent = inTwentyFourHourPercent
		self.sevenDayPercent = inSevenDayPercent
	
	# Defining the getters and setters
	def setName(self, inName):
		self.name = inName
	
	def getName(self):
		return self.name

	def setLabel(self, inLabel):
		self.label = inLabel
	
	def getLabel(self):
		return self.label
	
	def setMarketCap(self, inMarketCap):
		self.marketCap = float(inMarketCap)
	
	def getMarketCap(self):
		return self.marketCap
	
	def setPrice(self, inPrice):
		self.price = float(inPrice)
	
	def getPrice(self):
		return self.price
	
	def setCirculatingSupply(self, inCirculatingSupply):
		self.circulatingSupply = float(inCirculatingSupply)
	
	def getCirculatingSupply(self):
		return self.circulatingSupply
	
	def setVolume(self, inVolume):
		self.volume = float(inVolume)
	
	def getVolume(self):
		return self.volume
	
	def setOneHourPercent(self, inOneHourPercent):
		self.oneHourPercent = inOneHourPercent
	
	def getOneHourPercent(self):
		return self.oneHourPercent
	
	def setTwentyFourHourPercent(self, inTwentyFourHourPercent):
		self.twentyFourHourPercent = inTwentyFourHourPercent
	
	def getTwentyFourHourPercent(self):
		return self.twentyFourHourPercent
	
	def setSevenDayPercent(self, inSevenDayPercent):
		self.sevenDayPercent = inSevenDayPercent
	
	def getSevenDayPercent(self):
		return self.sevenDayPercent
	

class AssetObject():

	# initializing the constructor
	def __init__(self):
		self.assetList = DSALinkedList()
	
	# Adding an asset
	def addAsset(self, inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent):
		newAsset = Asset(inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent)
		self.assetList.insertLast(newAsset)
	
	# returning an asset
	def getAsset(self, inLabel):
		retAsset = None
		currAsset = self.assetList.head
		isFound = False
		if not self.assetList.isEmpty():
			while(currAsset != None and not isFound):
				if currAsset.getValue().getLabel() == inLabel:
					retAsset = currAsset.getValue()
					isFound = True 
				currAsset = currAsset.getNext()
		return retAsset
	
	# returning an asset
	def hasAsset(self, inLabel):
		return self.getAsset(inLabel) != None
	

	def getAssetOverview(self):
		# Getting the list of assets
		assets = self.assetList.listOfValues()
		# initializing the arrays
		highestMarketCap = np.empty(10, dtype=object)
		highestMarketCapLabels = np.empty(10, dtype=object)
		highestPrice = np.empty(10, dtype=object)
		highestPriceLabels = np.empty(10, dtype=object)
		highestCirculatingSupply = np.empty(10, dtype=object)
		highestCirculatingSupplyLabels = np.empty(10, dtype=object)
		highestVolume = np.empty(10, dtype=object)
		highestVolumeLabels = np.empty(10, dtype=object)

		for asset in assets:
			label = asset.getLabel()
			self.insertHighValue(label, asset.getMarketCap(), highestMarketCap, highestMarketCapLabels)
			self.insertHighValue(label, asset.getPrice(), highestPrice, highestPriceLabels)
			self.insertHighValue(label, asset.getCirculatingSupply(), highestCirculatingSupply, highestCirculatingSupplyLabels)
			self.insertHighValue(label, asset.getVolume(), highestVolume, highestVolumeLabels)
		
		# Printing out the top 10 values
		print('\nTop 10 Market Caps\n')
		self.displayOverview(highestMarketCapLabels, highestMarketCap)
		print('\nTop 10 Price\n')
		self.displayOverview(highestPriceLabels, highestPrice)
		print('\nTop 10 Circulating Supply\n')
		self.displayOverview(highestCirculatingSupplyLabels, highestCirculatingSupply)
		print('\nTop 10 Total Volume\n')
		self.displayOverview(highestVolumeLabels, highestVolume)

	
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
