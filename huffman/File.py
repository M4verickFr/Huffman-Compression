import os

class File():
	def __init__(self, path):
		self.path = path

	def read(self):
		with open(self.path) as file:
			return file.read()

	def export(self, frequency, compressedText):
		dir = os.path.dirname(self.path)
		basename = os.path.splitext(os.path.basename(self.path))[0]

		with open(dir+"/"+basename+"_freq.txt", 'w') as file:
			file.write(str(len(frequency))+"\n")
			frequency=map(lambda x:str(x[0])+" "+str(x[1])+'\n', frequency.items())
			file.writelines(frequency)

		with open(dir+"/"+basename+"_comp.bin", 'wb') as file:
			file.write(compressedText)
