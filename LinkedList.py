
#Program implementing the Linked List

import numpy as np

#Linked List Node Class
class DSAListNode():

	#initializing the constructor
	def __init__(self,inValue):
		self.value = inValue
		self.next = None
		self.prev = None
	
	#return the value of the node
	def getValue(self):
		return self.value
	
	#change the value of the node
	def setValue(self,inValue):
		self.value = inValue

	#return the Next value of the node
	def getNext(self):
		return self.next
	
	#return the Prev value of the node
	def getPrev(self):
		return self.prev
	
	#set the Next node value
	def setNext(self,newNext):
		self.next = newNext
	
	#set the Prev node value
	def setPrev(self,newPrev):
		self.prev = newPrev
	

#Linked List implementation class
class DSALinkedList():
	head = DSAListNode(None)
	tail = DSAListNode(None)

	#initializing the constructor
	def __init__(self):
		self.head = None
		self.tail = None
	
	#check if the list is empty
	def isEmpty(self):
		return self.head == None
	
	#inserting into the top of the list
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
	
	#inserting into the bottom of the list
	def insertLast(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self.head = newNd
			self.tail = newNd
		else:
			self.tail.setNext(newNd)
			newNd.setPrev(self.tail)
			self.tail = newNd
	
	#return the first node of the list
	def peekFirst(self):
		if self.isEmpty():
			print("The List is empty")
		else:
			return self.head.getValue()
	
	#return the last node of the list
	def peekLast(self):
		if self.isEmpty():
			print("The List is empty")
		else:
			return self.tail.getValue()
	
	#remvoing the first node of the list
	def removeFirst(self):
		if self.isEmpty():
			print("The List is empty")
		else:
			if self.head.getNext() == None:
				rmNd = self.head.getValue()
				self.head = None
			else:
				rmNd = self.head.getValue()
				self.head = self.head.getNext()
				self.head.setPrev(None)
			return rmNd
	
	#removing the last node of the list
	def removeLast(self):
		if self.isEmpty():
			print("The list is empty")
		else:
			rmNd = self.tail.getValue()
			self.tail = self.tail.getPrev()
			self.tail.setNext(None)
			return rmNd
	
	#remvoing the input value from the list
	def remove(self, inValue):
		if self.isEmpty():
			print("The List is empty")
		else:
			rmNd = self.head
			while(rmNd != None):
				if rmNd.getValue() == inValue:
					rmNd.getPrev().setNext(rmNd.getNext())
				rmNd = rmNd.getNext()
			return rmNd
	
	#iterate the elements of the list
	def __iter__(self):
		self.cur = self.head
		return self
	
	#showing the next element in the list
	def __next__(self):
		i = 1
		currNd = None
		if self.cur == None:
			print("The list is empty")
		else:
			currNd = self.cur.getValue()
			print(currNd)
			self.cur = self.cur.getNext()
	
	# displaying the items of the list
	def display(self):
		currNd = self.head
		while(currNd != None):
			print(currNd.getValue(), end=' ')
			currNd = currNd.getNext()
		print()
	
	# returning a list of the items in linked list
	def listOfValues(self):
		ll = []
		currNd = self.head
		if not (self.isEmpty()):
			while(currNd != None):
				ll.append(currNd.getValue())
				currNd = currNd.getNext()
		return ll

	# check if a value exists in the linked list
	def search(self, value):
		isFound = False
		currNd = self.head
		if not(self.isEmpty()):
			while(currNd != None):
				if currNd.getValue() == value:
					isFound = True
					currNd = currNd.getNext()
		return isFound
	
	# Finding a value in the linked list
	def find(self, value):
		retrunValue = None
		if not(self.isEmpty()):
			currNd = self.head
			while(currNd != None):
				if currNd.getValue() == value:
					retrunValue = currNd.getValue()
				currNd = currNd.getNext()
		return retrunValue
	
	# count of values that exist in the linked list
	def count(self):
		c = 0
		currNd = self.head
		if not(self.isEmpty()):
			while(currNd != None):
				c += 1
				currNd = currNd.getNext()
		return c

if __name__=='__main__':
	ll = DSALinkedList()
	ll.insertLast(2)
	k = ll.find(2)
	print(k)







			

			

		





			

			

		
