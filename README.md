# Cryptocurrency Trade Details and Overview

The main aim of this program is to collect , analyze and show the data of the different cryptocurrency transactions, various characteristics such as an asset's details, a trade 's details, the different direct and indirect trading paths between two assets and an overview of the assets and trades. I have used a graph data structure to store the assets and the different trades associated with the assets. 

The assets would act as the vertices of the graph and the trades would act as the edges in the graph. All the details concerning a trade such as its weighted average price, volume, count etc. has been stored along with  the  edge between  the  two  assets. Although  the  vertices  of  the  graph  denotes  the  assets,  the  details regarding a particular asset has been stored in another class named assetObject,which stores an asset and its details. It does not have any reference to the graph or the trades, it reads from the asset_info.csv and displays the information when requested. 

## Requirements

Python 3.0 or higher

Numpy version 1.19.1

## Data 

asset_file.json: Exchange information of tradeable tokens. [Source](https://www.binance.com/api/v3/exchangeInfo)

trade_file.json: Trade information for last 24 hours. [Source](https://www.binance.com/api/v3/ticker/24hr)

asset_info.csv: Data for the assets in crypto currency trading. [Source](https://coinmarketcap.com/all/views/all)

## Licence

MIT License

Copyright (c) 2020 Joby Mathew

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
