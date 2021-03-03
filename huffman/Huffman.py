from .File import File

"""class to encode data into smaller bits according to their 
   frequinces of occurance.
"""
class Huffman():
   def compressFile(self, path):
      file = File(path)
      text = file.read()
      self.compress(text)

   def compress(self, text):
      pass

