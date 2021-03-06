class Ratio():
	def __init__(self, frequency, encodage_table):
		self.frequency = frequency
		self.encodage_table = encodage_table

	def getRatio(self):
		nbChars = 0
		compressedBits = 0
		for char in self.frequency.items():
			nbChars += char[1]
			compressedBits += char[1]*len(self.encodage_table[char[0]])
		
		originalBits = nbChars * 8
		return 1 - compressedBits / originalBits		

