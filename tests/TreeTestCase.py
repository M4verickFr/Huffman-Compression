import unittest 
from huffman.Tree import Tree 

class TreeTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = Tree({'B': 1, 'n': 1, 'j': 1, 'u': 1, 'r': 1, 'o': 2, '!': 2})
        
    def test_root_weight(self):
        self.assertEqual(self.tree.get_root().get_weight(), 9)

    def test_leftChild_weight(self):
        self.assertEqual(self.tree.get_root().get_left().get_weight(), 4)

    def test_leftChild_leftChild_char(self):
        self.assertEqual(self.tree.get_root().get_left().get_left().get_char(), '!')

    def test_leftChild_leftChild_weight(self):
        self.assertEqual(self.tree.get_root().get_left().get_left().get_weight(), 2)

if __name__ == '__main__':
    unittest.main()
