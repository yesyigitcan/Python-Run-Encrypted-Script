The scripts in this repository is used to transfer a python script to another path safely and run it in that path

Steps that you need to follow:

1) Use KEY_GENERATOR.py script to generate your own key for encryption and decryption
2) You can either use CONVERTER.py script directly or use CONVERTER.exe on your Windows pc

How to call in terminal:

For encryption
> CONVERTER 1 INPUT_PATH INPUT_FILENAME OUTPUT_PATH OUTPUT_FILENAME.BIN

For decryption and run
> CONVERTER 2 INPUT_PATH INPUT_FILENAME.BIN

Process order

For encryption

1) It encodes the content of the input file
2) Then encrypts the encoded content
3) Creates a new file by your parameter and save the encrypted content in that file

For decryption

1) It decryptes the content of the encrypted file
2) Decodes the decrypted content
3) Creates a new python file and save the decrypted content in that file
4) Executes the python script
5) Delete this script after it is already executed
