class CustomAgent:
	def __init__(self, mem_size):
		self.memory = []
		self.operations = []
		self.src = []

		self.x_to = []
		self.y_from = []

		for i in range(mem_size):
			self.memory.append(0)

	def is_noun(self, noun):
		n = True
		try:
			int(noun)
			if int(noun) < 0:
				n = False
		except:
			n = False
		return n

	def add_src(self, line):
		self.src.append(line)

	def set_src(self, lines):
		self.src = lines

	def add_input(self, memory):
		self.x_to.append(memory)

	def add_output(self, memory):
		self.y_from.append(memory)

	def extract(self, phrase):
		nouns = []
		states = [-1, -1]
		
		level = 0
		for w in phrase:
			if self.is_noun(w):
				if level == 0:
					if states[0] == 0:
						nouns.append(int(w))
					elif states[0] == 1:
						nouns.append(int(w))
				elif level == 1:
					if states[1] == 0:
						nouns[len(nouns)-1].append(int(w))
			else:
				if w == '.' and states[0] == -1:
					states[0] = 0
				elif w == '[' and states[1] == -1:
					level = 1
					states[1] = 0
					nouns.append([])
				elif w == ']' and states[1] == 0:
					level = 0
					states[1] = -1
				elif w == ':' and states[0] == 0:
					states[0] == 1
		return nouns

	def compute(self, action):
		try: 
			self.memory[action[2]] = self.operations[action[0]].f(self.memory[action[1][0]])
			return self.memory[action[2]]
		except:
			return 0

	def f(self, inputs):
		for i in range(len(self.x_to)):

			self.memory[self.x_to[0]] = inputs[i]

		for phrase in self.src:
			action = self.extract(phrase)
			self.compute(action)
		
		outputs = []
		for i in range(len(self.y_from)):
			outputs.append(self.memory[self.y_from[i]])
		return outputs
