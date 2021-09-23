class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0
		
	class Node:
		def __init__(self, data):
			self.data = data
			self.next_node = None


	def push(self, data):
		self.length += 1
		if self.head is None:
			self.head = self.Node(data)
			return data
		
		node = self.head
		while node.next_node:
			node = node.next_node
		
		node.next_node = self.Node(data)
		return data
	
	def print_list(self) -> None:
			if self.head:
				node = self.head
				while node.next_node:
					print(node.data, end=' ')
					node = node.next_node
		
				print(node.data)
				
	def pop(self): # удаление последнего элемента
		if self.length == 1:
			self.length -= 1
			copy_node = self.head
			self.head = None
			self.next_node = None
			return copy_node.data
			
		elif self.head:
			self.length -= 1
			node = self.head
			prev_node = self.head
			while node.next_node:
				prev_node = node
				node = node.next_node
		
			prev_node.next_node = None
			return node.data


if  __name__ == '__main__':
	l_list = LinkedList()
	l_list.push(10)
	l_list.push(20)
	l_list.push(30)
	l_list.pop()
	l_list.pop()
	l_list.pop()
	l_list.push(70)
	l_list.print_list()

	