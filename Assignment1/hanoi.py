from util import Stack

def hanoi (n, source, helper, target):
	
	
	if n==1:
		target.push(source.pop())
	else:

		hanoi(n-1,source,target,helper)
		target.push(source.pop())
		hanoi(n-1,helper,source,target)

	print "source " 
	print
	temp = Stack()
	while not source.isEmpty():
		t = source.pop()
		temp.push(t)
		print t
	while not temp.isEmpty():
		t = temp.pop()
		source.push(t)
	print "helper " 
	print
	temp = Stack()
	while not helper.isEmpty():
		t = helper.pop()
		temp.push(t)
		print t
	while not temp.isEmpty():
		t = temp.pop()
		helper.push(t)
	print "target"
	print
	temp = Stack()
	while not target.isEmpty():
		t = target.pop()
		temp.push(t)
		print t
	while not temp.isEmpty():
		t = temp.pop()
		target.push(t)
	print 
	print

	





if __name__ == '__main__':
	source = Stack()
	helper = Stack()
	target = Stack()
	
	source.push("___")
	source.push("__")
	source.push("_")

	

	hanoi (3,source,target,helper)