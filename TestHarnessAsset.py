
from Asset import AssetObject
import numpy as np
import csv

assets = AssetObject()

file =  open('asset_info.csv', 'r') 
# Reading the csv
reader = csv.reader(file)
# Adding the data to the class object
for i, row in enumerate(reader):
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

# Checking if an asset exists

print('BTC exists:', assets.hasAsset('BTC'))
print('ETH exists:', assets.hasAsset('ETH'))
print('USDT exists:', assets.hasAsset('USDT'))
print('PAX exists:', assets.hasAsset('PAX'))

# Getting the details from a given asset

print('\nDisplaying the details of BTC')
assetValue = assets.getAsset('BTC')
print('Name:', assetValue.getName())
print('Market Cap:', assetValue.getMarketCap())
print('Price:', assetValue.getPrice())
print('Circulating Supply:', assetValue.getCirculatingSupply())
print('Volume:', assetValue.getVolume())
print('One Hour Percent:'+assetValue.getOneHourPercent()+'%')
print('Twenty Four Hour Percent:'+assetValue.getTwentyFourHourPercent()+'%')
print('Seven Day Percent:'+assetValue.getSevenDayPercent()+'%')

print('\nDisplaying the details of THX')
assetValue = assets.getAsset('THX')
print('Name:', assetValue.getName())
print('Market Cap:', assetValue.getMarketCap())
print('Price:', assetValue.getPrice())
print('Circulating Supply:', assetValue.getCirculatingSupply())
print('Volume:', assetValue.getVolume())
print('One Hour Percent: '+assetValue.getOneHourPercent()+'%')
print('Twenty Four Hour Percent: '+assetValue.getTwentyFourHourPercent()+'%')
print('Seven Day Percent: '+assetValue.getSevenDayPercent()+'%')

# Asset Report

print('\n Asset Report \n')

assets.getAssetOverview()

# Ignore asset

print('Ignoring BTC')
assets.ignoreAsset('BTC')

print('BTC exists: ', assets.hasAsset('BTC'))

# Asset Report

print('\n Asset Report \n')

assets.getAssetOverview()


