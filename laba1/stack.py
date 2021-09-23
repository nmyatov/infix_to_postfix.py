from LinkedList import LinkedList

class Stack: # стэк на основе связанного списка
	def __init__(self):
		self.arr = LinkedList()
		
	def push(self, data):
		return self.arr.push(data)
	
	def print_arr(self):
		self.arr.print_list()
		
	def pop(self):
		return self.arr.pop()

	def peek(self):
		if self.arr.head:
			node = self.arr.head
			if node.next_node:
				node = node.next_node
			return node.data
		return None
		
	def isEmpty(self) -> bool:
		return self.arr.length == 0


if __name__ == '__main__':
	stack = Stack()
	stack.push(10)
	stack.push(30)
	stack.pop()
	stack.pop()
	print(stack.isEmpty())
	stack.push(40)
	stack.print_arr()
	print(stack.isEmpty())

	
	

