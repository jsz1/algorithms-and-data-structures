class BinHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	def perc_up(self, i):
		while i // 2 > 0:
			if self.heap_list[i] < self.heap_list[i // 2]:
				tmp = self.heap_list[i // 2]
				self.heap_list[i // 2] = self.heap_list[i]
				self.heap_list[i] = tmp

	def perc_down(self, i):
		while (i * 2) <= self.current_size:
			current_min_child = self.min_child(i)
			if self.heap_list[i] > self.heap_list[current_min_child]:
				tmp = self.heap_list[i]
				self.heap_list[i] = self.heap_list[current_min_child]
				self.heap_list[current_min_child] = tmp
			i = current_min_child

	def min_child(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2
		else:
			if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def delete_min(self):
		return_value = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size = self.current_size - 1
		self.heap_list.pop()
		self.perc_down(1)
		return return_value

	def insert(self, k):
		self.heap_list.append(k)
		self.current_size = self.current_size + 1
		self.perc_up(self.current_size)

	def build_heap(self, alist):
		i = len(alist) // 2
		self.current_size = len(alist)
		self.heap_list = [0] + alist[:]
		while i > 0:
			self.perc_down(i)
			i = i - 1