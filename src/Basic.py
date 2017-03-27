class Sub:
	def f (self, inputs):
		return inputs[0] - inputs[1]

class Add:
	def f (self, inputs):
		return inputs[0] + inputs[1]

class Mult:
	def f (self, inputs):
		return inputs[0] * inputs[1]

class Less:
	def f (self, inputs):
		return inputs[0] < inputs[1]

class Equal:
	def f (self, inputs):
		return inputs[0] == inputs[1]

class More:

	def f (self, inputs):
		return inputs[0] > inputs[1]

class Not:
	def f (self, inputs):
		return inputs[0] == 0

class Or:
	def f (self, inputs):
		return inputs[0] == 1 or inputs[1] == 1 

class And:
	def f (self, inputs):
		return inputs[0] == 1 and inputs[1] == 1
