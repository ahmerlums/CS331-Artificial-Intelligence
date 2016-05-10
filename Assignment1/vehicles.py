class Vechicle:
	def __init__(self, arg1, arg2):
		self.Name = arg1
		self.Tyres= arg2
	def getName(self):
		return self.Name

class Car(Vechicle):

	def __init__(self,arg1,arg2):
		Vechicle.__init__(self, arg1, arg2)
		
	def getName(self):
		return self.Name
	def describeMe(self):
		print self.Name
		print self.Tyres

class Bike(Vechicle):

	def __init__(self,arg1,arg2):
		Vechicle.__init__(self, arg1, arg2)
		
	def getName(self):
		return self.Name
	def describeMe(self):
		print self.Name
		print self.Tyres

