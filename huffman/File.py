import os

class File():
	def __init__(self, path):
		self.path = path

	def read(self):
		fs = open(self.path)
		text = fs.read()
		fs.close()
		return text

