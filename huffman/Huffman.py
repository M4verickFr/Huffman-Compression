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
      frequency = self.make_frequency(text)
      print(frequency)

   def make_frequency(self, text):
      frequency = {}
      for character in text:
         if character in frequency:
            frequency[character] += 1
         else:
            frequency[character] = 1

      return dict(sorted(frequency.items(), key=lambda x: x[1]))

