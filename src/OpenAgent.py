from Agent import *

# Numerical Agents

class Sub (Agent):

	def f (self, x, z):
		return x - z

class Add (Agent):

	def f (self, x, z):
		return x + z

class Mult (Agent):

	def f (self, x, z):
		return x * z

# Comparision Agents

class Less (Agent):

	def f (self, x, z):
		return x < z

class Equal (Agent):

	def f (self, x, z):
		return x == z

class More (Agent):

	def f (self, x, z):
		return x > z

# Logic Agents

class Not (Agent):

	def f (self, x):
		return x == 0

class Or (Agent):

	def f (self, x, z):
		return x == 1 or z == 1 

class And (Agent):

	def f (self, x, z):
		return x == 1 and z == 1
