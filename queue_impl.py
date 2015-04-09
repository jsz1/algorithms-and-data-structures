from data_structures.queue import Queue

# q = Queue()

# q.enqueue(4)
# q.enqueue('dog')

# print q.size()
# print q.isEmpty()
# q.enqueue(8.4)
# print q.dequeue()

# print q.size()

def hot_potato(namelist, num):
	sim_queue = Queue()
	for name in namelist:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())

		print "removing %s" % sim_queue.dequeue()

	return sim_queue.dequeue()

print hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)