# CRC Encoder and Decoder

This Python script implements a CRC (Cyclic Redundancy Check) encoder and decoder. CRC is an error-detecting code used in digital networks and storage devices to detect accidental changes to raw data.

## Features

- **Encoding**: Encode input data using CRC with a specified key.
- **Decoding**: Decode encoded data and check for errors using CRC.
- **Codeword Retrieval**: Retrieve the codeword after encoding for further analysis.
- **Readability**: Code is written with readability in mind, making it easy to understand and modify.

## Usage

1. **Installation**: Clone this repository or download the `crc.py` file.

2. **Usage**: Run the script in a Python environment. You will be prompted to enter the data and key for encoding.

    ```
    python crc.py
    ```

3. **Output**: After encoding, the script will display the remainder and the encoded data. Then, it will decode the encoded data and check for errors. Finally, it will print the encoded data for reference.

## Requirements

- Python 3.x

## Example

```python
Enter your Data : 10111011
Enter your Key  : 1101
---------------
Remainder:  010
Data:  10111011010
---------------
No Error
---------------
10111011010
```