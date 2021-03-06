from .File import File
from .Tree import Tree
from .Frequency import Frequency
from .Ratio import Ratio

"""class to encode data into smaller bits according to their 
   frequinces of occurance.
"""
class Huffman():
   def compressFile(self, path):
      file = File(path)
      text = file.read()
      frequency, compressedText, ratio = self.compress(text)
      file.export(frequency, compressedText)

   def compress(self, text):
      frequency = Frequency(text)
      tree = Tree(frequency.get_freq())
      encodage_table = self.make_encodage_table(tree.get_root())
      compressedText = "".join([encodage_table[char] for char in text]).encode()
      ratio = Ratio(frequency.get_freq(), encodage_table)
      return frequency.get_freq(), compressedText, ratio.getRatio()

   def make_encodage_table(self, node, code=""):
      table_encodage = {}
      if node.get_char():
         if not code:
            table_encodage[node.get_char()] = "0"
         else:
            table_encodage[node.get_char()] = code
         return table_encodage
      else:
         table_encodage.update(self.make_encodage_table(node.get_left(), code+"0"))
         table_encodage.update(self.make_encodage_table(node.get_right(), code+"1"))
         return table_encodage