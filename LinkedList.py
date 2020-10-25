
"""
FILE: LinkedList.py 
AUTHOR: Joby Mathew
UNIT: COMP5008 Data Structures and Algorithms
PURPOSE: Provides a class implementing Linked List 
REFERENCE: Lecture Slides
Last Mod: 25th October, 2020
"""

import numpy as np

#Linked List Node Class
class DSAListNode():

	"""
	* Default Constructor.
    * IMPORT: inValue (Object).
    * EXPORT: none.
    * ASSERTION: value intialized as inValue, next and prev set as none.
	"""
	def __init__(self,inValue):
		self.value = inValue
		self.next = None
		self.prev = None
	
	"""
	* METHOD: getValue.
    * IMPORT: none.
    * EXPORT: value (Object).
    * ASSERTION: none.
	"""
	def getValue(self):
		return self.value
	
	"""
	* METHOD: setValue.
    * IMPORT: inValue (Object).
    * EXPORT: value.
    * ASSERTION: none.
	"""
	def setValue(self,inValue):
		self.value = inValue

	"""
	* METHOD: getNext.
    * IMPORT: none.
    * EXPORT: next (DSAListNode).
    * ASSERTION: none.
	"""
	def getNext(self):
		return self.next
	
	"""
	* METHOD: getPrev.
    * IMPORT: none.
    * EXPORT: prev (DSAListNode).
    * ASSERTION: none.
	"""
	def getPrev(self):
		return self.prev
	
	"""
	* METHOD: setNext.
    * IMPORT: newNext (DSAListNode).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setNext(self,newNext):
		self.next = newNext
	
	"""
	* METHOD: setPrev.
    * IMPORT: newPrev (DSAListNode).
    * EXPORT: none.
    * ASSERTION: none.
	"""
	def setPrev(self,newPrev):
		self.prev = newPrev
	

#Linked List implementation class
class DSALinkedList():
	head = DSAListNode(None)
	tail = DSAListNode(None)

	"""
	* Default Constructor.
    * IMPORT: none.
    * EXPORT: none.
    * ASSERTION: head and tail intialized as none.
	"""
	def __init__(self):
		self.head = None
		self.tail = None
	
	"""
	* METHOD: isEmpty.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: check if the list is empty.
	"""
	def isEmpty(self):
		return self.head == None
	
	"""
	* METHOD: insertFirst.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Inserting into the top of the list.
	"""
	def insertFirst(self,newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self.head = newNd
			self.head.setNext(None)
			self.head.setPrev(None)
			self.tail = newNd
			self.tail.setPrev(None)
			self.tail.setNext(None)
		else:
			newNd.setNext(self.head)
			self.head.setPrev(newNd)
			self.head = newNd
	
	"""
	* METHOD: insertLast.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Inserting into the bottom of the list.
	"""
	def insertLast(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self.head = newNd
			self.tail = newNd
		else:
			self.tail.setNext(newNd)
			newNd.setPrev(self.tail)
			self.tail = newNd
	
	"""
	* METHOD: peekFirst.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Returns the first element of the list.
	"""
	def peekFirst(self):
		retVal = None
		if not self.isEmpty():
			retVal = self.head.getValue()
		return retVal
	
	"""
	* METHOD: peekLast.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Returns the last element of the list.
	"""
	def peekLast(self):
		retVal = None
		if not  self.isEmpty():
			retVal = self.tail.getValue()
		return retVal
	
	"""
	* METHOD: removeFirst.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Removes the first element of the list.
	"""
	def removeFirst(self):
		if not self.isEmpty():
			if self.head.getNext() == None:
				rmNd = self.head.getValue()
				self.head = None
			else:
				rmNd = self.head.getValue()
				self.head = self.head.getNext()
				self.head.setPrev(None)
	
	"""
	* METHOD: removeLast.
    * IMPORT: none.
    * EXPORT: none.
    * USAGE: Removes the last element of the list.
	"""
	def removeLast(self):
		if not self.isEmpty():
			rmNd = self.tail.getValue()
			self.tail = self.tail.getPrev()
			self.tail.setNext(None)
	
	"""
	* METHOD: remove.
    * IMPORT: inValue (Object).
    * EXPORT: none.
    * USAGE: Removes the given element from the list.
	"""
	def remove(self, inValue):
		if not self.isEmpty():
			if self.head.getValue() == inValue:
				self.head = self.head.getNext() 
			rmNd = self.head
			while(rmNd.getNext() != None and rmNd.getValue() != inValue):
				prevNd = rmNd
				rmNd = rmNd.getNext()
			if rmNd.getValue() == inValue:
				prevNd.setNext(prevNd.getNext().getNext())
				if prevNd.getNext() != None:
					prevNd.getNext().setPrev(prevNd)
	
	"""
	* METHOD: iter.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: iteration. 
	"""
	def __iter__(self):
		self.cur = self.head
		return self
	
	"""
	* METHOD: next.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: returns next value of iteration. 
	"""
	def __next__(self):
		i = 1
		currNd = None
		if self.cur == None:
			print("The list is empty")
		else:
			currNd = self.cur.getValue()
			print(currNd)
			self.cur = self.cur.getNext()
	
	"""
	* METHOD: display.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: displaying the values in the list.
	"""
	def display(self):
		currNd = self.head
		while(currNd != None):
			print(currNd.getValue(), end=' ')
			currNd = currNd.getNext()
		print()
	
	"""
	* METHOD: listOfValues.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: returns the values in the list as an array.
	"""
	def listOfValues(self):
		size = self.count()
		rtnList = np.empty(size, dtype=object)
		currNd, i = self.head, 0
		if not (self.isEmpty()):
			while(currNd != None):
				rtnList[i] = currNd.getValue()
				i += 1
				currNd = currNd.getNext()
		return rtnList

	"""
	* METHOD: hasNode.
    * IMPORT: value (Object).
    * EXPORT: none.
	* USAGE: check if the element exists in the list. 
	"""
	def hasNode(self, value):
		isFound = False
		currNd = self.head
		if not(self.isEmpty()):
			while(currNd != None):
				if currNd.getValue() == value:
					isFound = True
				currNd = currNd.getNext()
		return isFound
	
	"""
	* METHOD: find.
    * IMPORT: value (Object).
    * EXPORT: none.
	* USAGE: find an element in the list. 
	"""
	def find(self, value):
		retrunValue = None
		if not(self.isEmpty()):
			currNd = self.head
			while(currNd != None):
				if currNd.getValue() == value:
					retrunValue = currNd.getValue()
				currNd = currNd.getNext()
		return retrunValue
	
	"""
	* METHOD: count.
    * IMPORT: none.
    * EXPORT: none.
	* USAGE: count of elements in the list. 
	"""
	def count(self):
		c = 0
		currNd = self.head
		if not(self.isEmpty()):
			while(currNd != None):
				c += 1
				currNd = currNd.getNext()
		return c








			

			

		





			

			

		
