## Text Splitter

**Scripts for encrypting and decrypting text files.**

### Description

Text Splitter reads in a plaintext file and produces two or more encrypted output files. Individually, the output files appear to consist entirely of random characters, but they can be combined to recover the original text.

### Download

Run `git clone https://github.com/YorickAndeweg/text_splitter.git`. No compilation necessary.

### Usage

**Encryption**:

Run `encrypt_text.py -f <input file>`. The input file is the plaintext file you want to encrypt, including the file extension. There are also several optional flags that can be included:
- -v, --verbose: Include this flag to output log of operations (default behavior: no output)
- -k, --keep: Include this flag to keep the original unencrypted file (default behavior: removes input file after encryption)
- -n, --number: Include this flag to change the number of output files (e.g. `-f 4`) (default behavior: produces 2 output files)

The output files produced by this script are named <input file>.part0, <input file>.part1, etc.

**Decryption**:

Run `decrypt_text.py -f <input file>`. The input file is the file that was encrypted by encrypt_text.py; do not include the ".part0", ".part1" suffixes. There are also several optional flags that can be included:
- -v, --verbose: Include this flag to output log of operations (default behavior: no output)
- -k, --keep: Include this flag to keep the original encrypted files (default behavior: removes input files after decryption)
- -n, --number: If the file you are decrypting has been split into more than 2 parts, specify the number of parts here (e.g. `-f 4`) (default behavior: uses 2 input files)
