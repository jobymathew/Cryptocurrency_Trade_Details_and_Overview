"""
FILE: UnitTestCryptoGraph.py 
AUTHOR: Joby Mathew
UNIT: COMP5008 Data Structures and Algorithms
PURPOSE: Provides a Test Harness for Linked List 
REFERENCE: Lecture Slides
Last Mod: 25th October, 2020
"""
from LinkedList import DSALinkedList

# Initializing the list
testList = DSALinkedList()

# Adding to the list
assets = ['BNB', 'ETH', 'BTC', 'USDT', 'PAX', 'USD', 'BCC', 'GAS', 'UTC', 'BNT']
for val in assets:
	testList.insertFirst(val)

print('List empty: ', testList.isEmpty())

print('\nDisplaying the values in the list')
print(testList.listOfValues())

print('\nNumber of elements in the list:', testList.count())


print('\nDisplaying the first value in the list:', testList.peekFirst())

print('\nDisplaying the last value in the list:', testList.peekLast())

print('\nAdding UNT to the end of the list')
testList.insertLast('UNT')
print('Displaying the last value in the list:', testList.peekLast())

print('\nRemoving the first element')
testList.removeFirst()
print('Displaying the first value in the list:', testList.peekFirst())

print('\nRemoving the last element')
testList.removeLast()
print('Displaying the last value in the list:', testList.peekLast())

print('\nRemoving PAX')
testList.remove('PAX')
print('Checking if PAX exists in the list: ', testList.hasNode('PAX'))
