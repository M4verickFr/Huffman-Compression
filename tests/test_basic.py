from huffman import Huffman 

pathFile = "./tests/data/textesimple.txt"

h = Huffman()
h.compressFile(pathFile)

compressedData = h.compress("Bonjour!!")