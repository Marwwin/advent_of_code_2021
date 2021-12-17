# %%
from typing import List, Tuple


class PriorityQueue:
	def __init__(self,queue = None) -> None:
		if not queue:
			self.heap = []
		else:		
			self.heap = queue

	def is_empty(self) -> bool:
		return True if self.heap == [] else False

	def insert(self, element: Tuple[int, int]) -> None:
		if not element in self.heap:
			self.heap.append(element)
			self.heapify_up()

	def pop(self) -> Tuple[int, int]:
		if not self.is_empty():
			item = self.heap[0]
			self.heap[0] = self.heap[len(self.heap)-1]
			self.heap = self.heap[:-1]
			self.heapify_down()
			return item
		else:
			return False

	def heapify_up(self) -> None:
		idx = len(self.heap)-1
		while idx != 0 and self.heap[idx] < self.get_parent(idx):
			self.swap(idx,self.get_parent_idx(idx))
			idx = self.get_parent_idx(idx)

	def heapify_down(self) -> None:
		idx = 0
		while self.has_left_child(idx):
			smaller_child = self.get_left_idx(idx)
			if self.has_right_child(idx) and self.get_right(idx) < self.get_left(idx):
				smaller_child = self.get_right_idx(idx)
			if self.heap[idx] < self.heap[smaller_child]:
				break
			else:
				self.swap(idx,smaller_child)

	def get_left(self,index:int)-> int:
		return self.heap[2*index+1] 
	
	def get_right(self,index:int) -> int:
		return self.heap[2*index+2]

	def get_left_idx(self,index:int)-> int:
		return 2*index+1
	
	def get_right_idx(self,index:int) -> int:
		return 2*index+2

	def has_left_child(self,index) -> bool:
		return (2*index+1) < self.length()

	def has_right_child(self,index) -> bool:
		return (2*index+2) < self.length()

	def get_parent(self,index: int) -> int:
		return self.heap[(index -1) // 2]

	def get_parent_idx(self,index:int) -> int:
		return (index -1) // 2

	def swap(self,first: int,second: int) -> None:
		temp = self.heap[first]
		self.heap[first] = self.heap[second]
		self.heap[second] = temp

	def length(self):
		return len(self.heap)

	def print_queue(self):
		for x in self.heap:
			print(x)

def solve() -> None:
	matrix = open_file("test_day15.txt")
	queue = PriorityQueue()
	paths = []
	current_node = (matrix[0][0],(0,0))
	queue = add_possible_nodes(current_node,queue,paths,matrix)
	end = (len(matrix)-1,len(matrix[0])-1)
	while current_node[1] != end:
		current_node, paths, queue = step(queue,paths,current_node,matrix)
	print(paths)

def step(queue,paths,current_node,matrix):
	new_node = queue.pop()
	if new_node == False:
		print(paths)
	paths.append(current_node)
	current_node = new_node
	#print(current_node)
	queue = add_possible_nodes(current_node,queue,paths,matrix)
	return current_node,paths,queue


def add_possible_nodes(current_node,queue,paths,matrix):
	current_value = matrix_value(current_node[1],matrix)
	if current_node[1][0] != 0:
		new_node = (current_node[1][0]-1,current_node[1][1])
		if new_node not in [path[1] for path in paths]:
			queue.insert((current_value+matrix_value(new_node,matrix),new_node))
	if current_node[1][0] != len(matrix)-1:
		new_node = (current_node[1][0]+1,current_node[1][1])
		if new_node not in [path[1] for path in paths]:
			queue.insert((current_value+matrix_value(new_node,matrix),new_node))
	if current_node[1][1] != 0:
		new_node = (current_node[1][0],current_node[1][1]-1)
		if new_node not in [path[1] for path in paths]:
			queue.insert((current_value+matrix_value(new_node,matrix),new_node))
	if current_node[1][1] != len(matrix[0])-1:
		new_node = (current_node[1][0],current_node[1][1]+1)
		if new_node not in [path[1] for path in paths]:
			queue.insert((current_value+matrix_value(new_node,matrix),new_node))		
	return queue

def matrix_value(node,matrix):
		return matrix[node[0]][node[1]]

def print_matrix(matrix):
	for row in matrix:
		print(row)

def open_file(filename: str) -> List[str]:
	with open(filename) as f:
			return([[int(n) for n in line.strip()] for line in f.readlines()])

solve()


# %%

True if [1, 2] else False
