from .File import File
from .Tree import Node

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
      root_node = self.make_tree(frequency)
      encodage_table = self.make_encodage_table(root_node)
      compressedText = "".join([encodage_table[char] for char in text])
      print(f"encodage table : {encodage_table}")
      print(f"compressedText : {compressedText}")

   def make_frequency(self, text):
      frequency = {}
      for character in text:
         if character in frequency:
            frequency[character] += 1
         else:
            frequency[character] = 1

      return dict(sorted(frequency.items(), key=lambda x: x[1]))

   def make_tree(self, frequency):
   	  # convert each characters in Node
      list_nodes = [Node(weight, character) for character,weight in frequency.items()]

      while len(list_nodes)>1:
         list_nodes = sorted(list_nodes, key=lambda x: x.get_weight())
         left_node = list_nodes.pop(0)
         right_node = list_nodes.pop(0)
         parent_node = Node(left_node.get_weight() + right_node.get_weight())
         parent_node.setChildren(left_node, right_node)
         list_nodes.append(parent_node)

      return list_nodes[0]

   def make_encodage_table(self, node, code=""):
      table_encodage = {}
      if node.char:
         if not code:
            table_encodage[node.char] = "0"
         else:
            table_encodage[node.char] = code
         return table_encodage
      else:
         table_encodage.update(self.make_encodage_table(node.get_left(), code+"0"))
         table_encodage.update(self.make_encodage_table(node.get_right(), code+"1"))
         return table_encodage