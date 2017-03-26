# Numerical Agents

class Sub :

	def f (self, x, z):
		return x - z

class Add :

	def f (self, x, z):
		return x + z

class Mult :

	def f (self, x, z):
		return x * z

# Comparision Agents

class Less :

	def f (self, x, z):
		return x < z

class Equal :

	def f (self, x, z):
		return x == z

class More :

	def f (self, x, z):
		return x > z

# Logic Agents

class Not :

	def f (self, x):
		return x == 0

class Or :

	def f (self, x, z):
		return x == 1 or z == 1 

class And :

	def f (self, x, z):
		return x == 1 and z == 1
