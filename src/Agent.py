class Store:

	def create(self, s):
		self.data = [0] * s
		self.size = s

	def set(self, i, x):
		self.data[i] = x

	def get(self, i):
		return self.data[i]

class Agent:

	def __init__(self):
		self.create(0)

	def create(self, capacity):
		self.memory = Store()
		self.memory.create(capacity)

	def f(self, x):
		return x