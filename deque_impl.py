from data_structures.deque import Deque

# d = Deque()
# print d.isEmpty()
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print d.size()
# print d.isEmpty()
# d.addRear(8.4)
# print d.removeRear()
# print d.removeFront()

def palendrome_checker(a_word):
	char_deque = Deque()

	for ch in a_word:
		char_deque.addRear(ch)

	still_equal = True

	while char_deque.size() > 1 and still_equal:
		first = char_deque.removeFront()
		last = char_deque.removeRear()
		if first != last:
			still_equal = False

	return still_equal

print palendrome_checker("Jacob")
print palendrome_checker("racecar")
print palendrome_checker("go hang a salami im a lasagna hog")