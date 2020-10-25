"""
FILE: Asset.py 
AUTHOR: Joby Mathew
UNIT: COMP5008 Data Structures and Algorithms
PURPOSE: Provides a class implementation for handling the assets and its details 
REFERENCE: Lecture Slides
Last Mod: 25th October, 2020
"""


import numpy as np
from LinkedList import DSALinkedList

class Asset():

	"""
	* DEFAULT Constructor.
    * IMPORT: inName (String), inLabel (String), inMarketCap (String), inPrice (String), inCirculatingSupply (String), inVolume (String), inOneHourPercent (String), inTwentyFourHourPercent (String), inSevenDayPercent (String).
    * EXPORT: none.
	* USAGE: Initiaizing the asset with the given values.
	"""
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
	
	"""
	* METHOD: setName.
    * IMPORT: inName (String).
    * EXPORT: none.
	"""
	def setName(self, inName):
		self.name = inName
	
	"""
	* METHOD: getName.
    * IMPORT: none.
    * EXPORT: name (String).
	"""
	def getName(self):
		return self.name

	"""
	* METHOD: setLabel.
    * IMPORT: inLabel (String).
    * EXPORT: none.
	"""
	def setLabel(self, inLabel):
		self.label = inLabel
	
	"""
	* METHOD: getLabel.
    * IMPORT: none.
    * EXPORT: label (String).
	"""
	def getLabel(self):
		return self.label
	
	"""
	* METHOD: setMarketCap.
    * IMPORT: inMarketCap (String).
    * EXPORT: none.
	"""
	def setMarketCap(self, inMarketCap):
		self.marketCap = float(inMarketCap)
	
	"""
	* METHOD: getMarketCap.
    * IMPORT: none.
    * EXPORT: marketCap (float).
	"""
	def getMarketCap(self):
		return self.marketCap
	
	"""
	* METHOD: setPrice.
    * IMPORT: inPrice (String).
    * EXPORT: none.
	"""
	def setPrice(self, inPrice):
		self.price = float(inPrice)
	
	"""
	* METHOD: getPrice.
    * IMPORT: none.
    * EXPORT: price (float).
	"""
	def getPrice(self):
		return self.price
	
	"""
	* METHOD: setCirculatingSupply.
    * IMPORT: inCirculatingSupply (String).
    * EXPORT: none.
	"""
	def setCirculatingSupply(self, inCirculatingSupply):
		self.circulatingSupply = float(inCirculatingSupply)
	
	"""
	* METHOD: getCirculatingSupply.
    * IMPORT: none.
    * EXPORT: circulatingSupply (float).
	"""
	def getCirculatingSupply(self):
		return self.circulatingSupply
	
	"""
	* METHOD: setVolume.
    * IMPORT: inVolume (String).
    * EXPORT: none.
	"""
	def setVolume(self, inVolume):
		self.volume = float(inVolume)
	
	"""
	* METHOD: getVolume.
    * IMPORT: none.
    * EXPORT: volume (float).
	"""
	def getVolume(self):
		return self.volume
	
	"""
	* METHOD: setOneHourPercent.
    * IMPORT: inOneHourPercent (String).
    * EXPORT: none.
	"""
	def setOneHourPercent(self, inOneHourPercent):
		self.oneHourPercent = inOneHourPercent
	
	"""
	* METHOD: getOneHourPercent.
    * IMPORT: none.
    * EXPORT: OneHourPercent (String).
	"""
	def getOneHourPercent(self):
		return self.oneHourPercent
	
	"""
	* METHOD: setTwentyFourHourPercent.
    * IMPORT: inTwentyFourHourPercent (String).
    * EXPORT: none.
	"""
	def setTwentyFourHourPercent(self, inTwentyFourHourPercent):
		self.twentyFourHourPercent = inTwentyFourHourPercent
	
	"""
	* METHOD: getTwentyFourHourPercent.
    * IMPORT: none.
    * EXPORT: twentyFourHourPercent (String).
	"""
	def getTwentyFourHourPercent(self):
		return self.twentyFourHourPercent
	
	"""
	* METHOD: setSevenDayPercent.
    * IMPORT: inSevenDayPercent (String).
    * EXPORT: none.
	"""
	def setSevenDayPercent(self, inSevenDayPercent):
		self.sevenDayPercent = inSevenDayPercent
	
	"""
	* METHOD: getSevenDayPercent.
    * IMPORT: none.
    * EXPORT: sevenDayPercent (String).
	"""
	def getSevenDayPercent(self):
		return self.sevenDayPercent
	

class AssetObject():

	"""
	* DEFAULT Constructor.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: Initilaizing the lists.
	"""
	def __init__(self):
		self.assetList = DSALinkedList()
		self.filterAssets = DSALinkedList()
	
	"""
	* METHOD: addAsset.
    * IMPORT: inName (String), inLabel (String), inMarketCap (String), inPrice (String), inCirculatingSupply (String), inVolume (String), inOneHourPercent (String), inTwentyFourHourPercent (String), inSevenDayPercent (String).
    * EXPORT: none.
	* USAGE: Adding an asset.
	"""
	def addAsset(self, inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent):
		newAsset = Asset(inName, inLabel, inMarketCap, inPrice, inCirculatingSupply, inVolume, inOneHourPercent, inTwentyFourHourPercent, inSevenDayPercent)
		self.assetList.insertLast(newAsset)
		self.filterAssets.insertLast(inLabel)
	
	"""
	* METHOD: getAsset.
    * IMPORT: inLabel (String).
    * EXPORT: none.
	* USAGE: Returning an asset.
	"""
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
	
	"""
	* METHOD: hasAsset.
    * IMPORT: inLabel (String).
    * EXPORT: none.
	* USAGE: Check if an asset exists.
	"""
	def hasAsset(self, inLabel):
		isFound = False
		if self.filterAssets.hasNode(inLabel):
			isFound = self.getAsset(inLabel) != None
		return isFound
	
	"""
	* METHOD: getAssetOverview.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: Finding the asset overview details
	"""
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
			if self.filterAssets.hasNode(label):
				self._insertHighValue(label, asset.getMarketCap(), highestMarketCap, highestMarketCapLabels)
				self._insertHighValue(label, asset.getPrice(), highestPrice, highestPriceLabels)
				self._insertHighValue(label, asset.getCirculatingSupply(), highestCirculatingSupply, highestCirculatingSupplyLabels)
				self._insertHighValue(label, asset.getVolume(), highestVolume, highestVolumeLabels)
		
		# Printing out the top 10 values
		print('\nTop 10 Market Caps\n')
		self.displayOverview(highestMarketCapLabels, highestMarketCap)
		print('\nTop 10 Price\n')
		self.displayOverview(highestPriceLabels, highestPrice)
		print('\nTop 10 Circulating Supply\n')
		self.displayOverview(highestCirculatingSupplyLabels, highestCirculatingSupply)
		print('\nTop 10 Total Volume\n')
		self.displayOverview(highestVolumeLabels, highestVolume)

	
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
	# Displaying the trade overview details
	def displayOverview(self, labels, values):
		for i in range(labels.size):
			print(f'{i+1}. {labels[i]} - {values[i]}')
		print()
	
	"""
	* METHOD: ignoreAsset.
    * IMPORT: inLabel (String).
    * EXPORT: none.
	* USAGE: Ignore the given asset
	"""
	def ignoreAsset(self, inLabel):
		self.filterAssets.remove(inLabel);
	
	"""
	* METHOD: addBackAsset.
    * IMPORT: inLabel (String).
    * EXPORT: none.
	* USAGE: Re-add the given asset
	"""
	def addBackAsset(self, inLabel):
		self.filterAssets.insertLast(inLabel);
