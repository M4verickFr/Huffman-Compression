from .File import File
from .Tree import Tree
from .Encodage import Encodage
from .Frequency import Frequency
from .Ratio import Ratio
from .HuffmanInterface import HuffmanInterface

class Huffman(HuffmanInterface):
   """Encode data into smaller bits according to their frequencies of occurance.
   """
   def compressFile(self, path:str):
      """Overrides HuffmanInterface.compressFile()

      Args:
          path (str): path of the file to compress

      Returns:
          Frequency: Frequency of characters in file
          Str: Binary text of the compressed file
          Float: Percentage reduction
          Float: Average number of bits to encode a character
      """
      file = File(path)
      text = file.read()
      frequency, compressedText, ratio, averageBitsForChar = self.compress(text)
      file.export(frequency, compressedText)
      return frequency, compressedText, ratio, averageBitsForChar

   def compress(self, text:str):
      """Overrides HuffmanInterface.compress()

      Args:
          text (str): text to compress

      Returns:
          Frequency: Frequency of characters in file
          Str: Binary text of the compressed file
          Float: Percentage reduction
          Float: Average number of bits to encode a character
      """
      frequency = Frequency(text)
      tree = Tree(frequency.get_freq())
      encodage = Encodage(tree.get_root())
      compressedText = "".join([encodage.get_table()[char] for char in text]).encode()
      ratio = Ratio(frequency.get_freq(), encodage.get_table())
      return frequency.get_freq(), compressedText, ratio.getRatio(), ratio.getAveragageBitsForChar()