import unittest
from huffman import Huffman 

class HuffmanTestCase(unittest.TestCase):
    def setUp(self):
        compressedData = Huffman().compress("Bonjour!!")
        self.frequency = compressedData['frequency']
        self.compressedTest = compressedData['compressedText']
        self.ratio = compressedData['ratio']
        self.averageBitsForChar = compressedData['averageBitsForChar']
        
    def test_frequency(self):
        self.assertEqual(self.frequency, {'B': 1, 'n': 1, 'j': 1, 'u': 1, 'r': 1, 'o': 2, '!': 2})

    def test_compressedTest(self):
        self.assertEqual(self.compressedTest, b'0101110111001111011100000')

    def test_ratio(self):
        self.assertEqual(round(self.ratio,2), 0.65)

    def test_averageBitsForChar(self):
        self.assertEqual(round(self.averageBitsForChar, 2), 2.86)

if __name__ == '__main__':
    unittest.main()
