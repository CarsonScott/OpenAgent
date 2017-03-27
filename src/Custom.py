class CustomAgent:

	def __init__(self, mem_size):
		self.memory = []
		self.operations = []
		self.src = []
		self.x_to = []
		self.y_from = []

		for i in range(mem_size):
			self.memory.append(0)

	def is_noun(self, word):
		noun = False
		try:
			if int(word) >= 0:
				noun = True
		except:
			noun = False
		return noun

	def add_action(self, action):
		self.src.append(action)

	def add_input(self, memory):
		self.x_to.append(memory)

	def add_output(self, memory):
		self.y_from.append(memory)

	def add_agent(self, agent):
		self.operations.append(agent)

	def extract(self, phrase):
		nouns = []
		level = 0
		states = [-1, -1]
		
		for w in phrase:
			if self.is_noun(w):
				if level == 0:
					if states[0] == 0:
						nouns.append(int(w))
					elif states[0] == 1:
						nouns.append(int(w))
				elif level == 1:

					nouns[len(nouns)-1].append(int(w))
			else:
				if w == '.' and states[0] == -1:
					states[0] = 0
				elif w == '[' and states[1] == -1:
					level = 1
					states[1] = 0
					nouns.append([])
				elif w == ',' and states[1] == 0:
					level = 1
					states[1] = 1
				elif w == ']':
					level = 0
					states[1] = -1
				elif w == ':' and states[0] == 0:
					states[0] == 1
		return nouns

	def compute(self, action):
			o = action[0]
			x = action[1]
			y = action[2]

			inputs = []
			for i in x:
				inputs.append(self.memory[i])
			self.memory[y] = self.operations[o].f(inputs)
			
	def f(self, inputs):
		for i in range(len(self.x_to)):
			self.memory[self.x_to[i]] = inputs[i]
		
		for phrase in self.src:
			self.compute(self.extract(phrase))
			
		
		outputs = []
		for i in range(len(self.y_from)):
			outputs.append(self.memory[self.y_from[i]])
		return outputs


