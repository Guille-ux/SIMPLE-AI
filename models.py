#nodo de decisión
import random

class DecissionNode:
	def __init__(self, train_data, min=0, max=1000):
		self.max = max
		self.train_data = train_data #los resultados de los datos deben ser 1 o 0
		self.cut = min
		self.error = 0
		self.minerror = max
		self.min = min
	def train(self):
		for z in range(self.min, self.max):
			self.error = 0
			for i in self.train_data:
				x = i[0]
				y = i[1]
				if x < z:
					value = 0
				else:
					value = 1
				if y != value:
					self.error += 1
			if self.error <= self.minerror:
				self.minerror = self.error
				self.cut = z
		return (self.minerror/self.max, self.cut)
	def use(self, input):
		if input < self.cut:
			return 0
		else:
			return 1
#Cadena de markov
class MarkovChain:
	def __init__(self, corpus):
		self.corpus = corpus
		self.vocablo = []
		self.ret = ""
		self.counted = 0
	def train(self):
		esekas = []
		for sentence in self.corpus:
			sp = sentence.split(" ")
			print(str(sp))
			sk = []
			keys = []
			key = []
			for i in sp:
				if i in sk:
					pass
				else:
					sk.append(i)
			print(str(sk))
			for i in sk:
				for x in sp:
					if i + " " + x in sentence:
						key.append(x)
				keys.append((i, key))
				key = []
			esekas.append(keys)
		current = []
		claves = []
		for i in esekas:
			for x in i:
				clave = x[0]
				valor = x[1]
				if clave in claves:
					for y in range(len(current)):
						if current[y][0] == clave:
							current[y][1].extend(valor)
				else:
					claves.append(clave)
					current.append((clave, valor))
		print(str(current))
		self.vocablo = current
	def gen(self, seed):
		self.counted -= 1
		for i in self.vocablo:
			if i[0] == seed:
				self.ret += " " + seed
				if self.counted == 0:
					return seed
				try:
					current = self.gen(random.choice(i[1]))
				except Exception:
					current = seed
				return current
	def ultigen(self, seed, counted):
		self.counted = counted
		self.ret = ""
		self.gen(seed)
		return self.ret
