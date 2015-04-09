from data_structures.lists import Node, UnorderedList

# temp = Node(93)

# print temp.get_data()

new_list = UnorderedList()

new_list.add(31)
new_list.add(77)
new_list.add(17)
new_list.add(93)
new_list.add(26)
new_list.add(54)

print new_list.size()
print new_list.search(93)
print new_list.search(100)

new_list.add(100)
print new_list.search(100)
print new_list.size()

new_list.remove(54)
print new_list.size()
new_list.remove(93)
print new_list.size()
new_list.remove(31)
print new_list.size()
print new_list.search(93)