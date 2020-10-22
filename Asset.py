
import numpy as np

class Asset():

	# initializing the constructor
	def __init__(self, inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent):
		self.name = inName
		self.label = inLabel
		self.marketCap = inMarketCap
		self.price = inPrice
		self.circulatingSupply = inCirculatingSupply
		self.volume = inVolume
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
		self.marketCap = inMarketCap
	
	def getMarketCap(self):
		return self.marketCap
	
	def setPrice(self, inPrice):
		self.price = inPrice
	
	def getPrice(self):
		return self.price
	
	def setCirculatingSupply(self, inCirculatingSupply):
		self.circulatingSupply = inCirculatingSupply
	
	def getCirculatingSupply(self):
		return self.circulatingSupply
	
	def setVolume(self, inVolume):
		self.volume = inVolume
	
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
	

class assetObject():

	# initializing the constructor
	def __init__(self):
		self.assetList = DSALinkedList()
	
	# Adding an asset
	def addAsset(self, inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent):
		newAsset = Asset(inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent)
		assetList.insertLast(newAsset)
	
	# returning an asset
	def getAsset(self, inLabel):
		retAsset = None
		currAsset = self.assetList.head
		isFound = False
		if not currAsset.isEmpty():
			while(currAsset.getValue() != None and not isFound):
				if currAsset.getValue().getLabel() == inLabel:
					retAsset = currAsset.getValue()
					isFound = True 
				currAsset = currAsset.getNext()
		return retAsset
	

	def getAssetOverview(self):
		# Getting the list of assets
		assets = self.assetList.listOfVertices()
		# initializing the arrays
		highestMarketCap = np.empty(10, dtype=object)
		highestMarketCapLabels = np.empty(10, dtype=object)
		highestPrice = np.empty(10, dtype=object)
		highestPriceLabels = np.empty(10, dtype=object)
		highestCirculatingSupply = np.empty(10, dtype=object)
		highestCirculatingSupplyLabels = np.empty(10, dtype=object)
		highestVolume = np.empty(10, dtype=object)
		highestVolumeLabels = np.empty(10, dtype=object)
		highestOneHourPercent = np.empty(10, dtype=object)
		highestOneHourPercentLabels = np.empty(10, dtype=object)
		highestTwentyFourHourPercent = np.empty(10, dtype=object)
		highestTwentyFourHourPercentLabels = np.empty(10, dtype=object)
		highestSevenDayPercent = np.empty(10, dtype=object)
		highestSevenDayPercentLabels = np.empty(10, dtype=object)

		for asset in assets:
			label = asset.getLabel()
			self.insertHighValue(label, asset.getMarketCap(), highestMarketCap, highestMarketCapLabels)
			self.insertHighValue(label, asset.getPrice(), highestPrice, highestPriceLabels)
			self.insertHighValue(label, asset.getCirculatingSupply(), highestCirculatingSupply, highestCirculatingSupplyLabels)
			self.insertHighValue(label, asset.getVolume(), highestVolume, highestVolumeLabels)
			self.insertHighValue(label, asset.getOneHourPercent(), highestOneHourPercent, highestOneHourPercentLabels)
			self.insertHighValue(label, asset.getTwentyFourHourPercent(), highestTwentyFourHourPercent, highestTwentyFourHourPercentLabels)
			self.insertHighValue(label, asset.getSevenDayPercent(), highestSevenDayPercent, highestSevenDayPercentLabels)
		
		# Printing out the top 10 values
		print('\nTop 10 Market Caps')
		self.displayOverview(highestMarketCapLabels, highestMarketCap)
		print('\nTop 10 Price')
		self.displayOverview(highestPriceLabels, highestPrice)
		print('\nTop 10 Circulating Supply')
		self.displayOverview(highestCirculatingSupplyLabels, highestCirculatingSupply)
		print('\nTop 10 Total Volume')
		self.displayOverview(highestVolumeLabels, highestVolume)
		print('\nTop 10 1 Hour percent change')
		self.displayOverview(highestOneHourPercentLabels, highestOneHourPercent)
		print('\nTop 10 24 Hour percent change')
		self.displayOverview(highestTwentyFourHourPercentLabels, highestTwentyFourHourPercent)
		print('\nTop 10 7 Day percent change')
		self.displayOverview(highestSevenDayPercentLabels, highestSevenDayPercent)

	
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
