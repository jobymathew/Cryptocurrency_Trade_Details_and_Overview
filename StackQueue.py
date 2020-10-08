#Program for implementing Stack and Queue using Linked List


import numpy as np
from LinkedList import *

# Stack Class
class DSAStack():

	# constructor
	def __init__(self):
		#intializing stack with Linked List
		self.stack = DSALinkedList()
	
	# condition if queue is empty 
	def isEmpty(self):
		if self.stack.isEmpty():
			return True
		else:
			return False
	
	# last element of the stack 
	def top(self):
		return self.stack[self.count-1]

	# inserting a value 
	def push(self,val):
		self.stack.insertFirst(val)

	# removing a value
	def pop(self):
		val = self.stack.removeFirst()
		return val
	
	#itertaing the list
	def iterator(self):
		iter(self.stack)
	
	#displaying all the items in the list
	def display(self):
		return self.stack.display()


# Queue Class
class DSAQueue():

	# constructor
	def __init__(self):
		# intializing queue as a linked list
		self.queue = DSALinkedList()
	
	# condition for empty queue 
	def isEmpty(self):
		if self.queue.isEmpty():
			return True
		else:
			return False
	
	# inserting into the queue
	def enqueue(self,val):
		self.queue.insertLast(val)
	
	# removing from the queue
	def dequeue(self):
		val = self.queue.removeFirst()
		return val
	
	#iterating the list
	def iterator(self):
		return iter(self.queue)
	
	#displaying the items of the list
	def display(self):
		return self.queue.display()


	

