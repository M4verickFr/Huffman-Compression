# huffman-project
A python package to compress data based on character frequency

## Installation instructions

Clone the repo:

```sh
pip3 install huffman-project
```

## Installation instructions (dev)

Clone the repo:

```sh
git clone git@github.com:M4verickFr/huffman-project.git
```

Then install the dependencies and install the package:

```sh
pip3 install -r requirements.txt
pip3 install -e . 
```

## Usage

Import huffman package.

```python
from huffman import Huffman 
```

Then use methods compress or comrpessFile. 

```python
h = Huffman()

h.compress("Bonjour!!")
h.compressFile(pathFile)
```

For examples of use, see the test folder.

## Unit Test Case

You can run Unit Test Case with

```bash
python3 -m unittest tests/HuffmanTestCase.py
python3 -m unittest tests/TreeTestCase.py
```

All tests must be passed

## The development phases of the project

1. Learn information on the Huffman compression algorithm.
2. Learn how to develop a python package.
3. Determine the structure of the project. 
4. Read the text of the file and determine the frequency of each character.
5. Export frequency to a file.
6. Make the Huffman tree from the frequency.
7. Determine the encoding table from the Huffman tree.
8. Use the encoding table to encode text.
9. Export compressed (encoded) text.

## What difficulties I have encountered?

During the realisation of my project, I didn't have many difficulties.

The first difficulty I encountered was that when I generated the Huffman tree, I didn't know if the smallest node between the two smallest nodes should be the left or right child in the Huffman tree.

And the second difficulty comes when I wanted to send my package to pyPI because I didn't have a good setup.py and I didn't have a setup.cfg. After some research on Google, I found the solutions to the different problems related to my setup.py. The problem was due to the license in setup.py should contain only the name of the license and not the content of the LICENSE file.

## License

This project is under the Apache 2.0 License.

**Free Software, Hell Yeah!**
