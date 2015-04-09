from data_structures.stack import Stack

s = Stack()
# print s.isEmpty()
# s.push(4)
# s.push('dog')
# print s.peek()
# s.push(True)
# print s.size()
# print s.isEmpty()
# s.push(8.4)
# print s.pop()
# print s.pop()
# print s.size()

m = Stack()
# m.push('x')
# m.push('y')
# m.push('z')
# while not m.isEmpty():
# 	m.pop()
# 	m.pop()

def rev_string(test_str):
	string_stack = Stack()
	for ch in test_str:
		string_stack.push(ch)
	reverse_string = ''
	while not string_stack.isEmpty():
		reverse_string = reverse_string + string_stack.pop()
	return reverse_string

# print rev_string('apple')

def divide_by_2(dec_num):
	remstack = Stack()

	while dec_num > 0:
		rem = dec_num % 2
		remstack.push(rem)
		dec_num = dec_num // 2

	bin_string = ""
	while not remstack.isEmpty():
		bin_string = bin_string + str(remstack.pop())

	return bin_string

print divide_by_2(420)