# huffman-encode
A python package to compress data based on character frequency

This repository contains files for huffman package and test files for it in `tests/` directory.

## Installation

Clone the repo:

```bash
git clone git@github.com:M4verickFr/huffman-project.git
```

Then install the dependencies and install the package:

```bash
pip3 install -r requirements.txt
pip3 install huffman-project
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

You can find usage exemple in folder test.

## Todo

- Export to binary file
- Comment code
- Determine compression rate
- Average number of storage bits of a character

## License

This project is under the Apache 2.0 License.