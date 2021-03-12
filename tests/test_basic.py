from huffman import Huffman 

pathFile = "tests/data/textesimple.txt"

h = Huffman()
h.compressFile(pathFile)

frequency, compressedText, ratio, averageBitsForChar = h.compress("Bonjour!!")