import pickle
import os
import platform
import sys
from cryptography.fernet import Fernet

PYOUTPUTNAME = 'o.py'

def LOAD_KEY():
    """
    Load the previously generated key
    """
    return open("KEY.key", "rb").read()

def SAVE_AS_BIN(INPUTNAME, OUTPUTNAME = "output.bin"):
    with open(INPUTNAME, 'r') as INPUTFILE:
        with open(OUTPUTNAME, 'wb') as OUTPUTFILE:
            key = LOAD_KEY()
            encoded_content = ''.join(INPUTFILE.readlines()).encode()
            f = Fernet(key)
            encrypted_content = f.encrypt(encoded_content)

            pickle.dump(encrypted_content, OUTPUTFILE)

def SAVE_AS_PY(INPUTNAME):
    
    with open(INPUTNAME, 'rb') as INPUTFILE:
        with open(PYOUTPUTNAME, 'w') as OUTPUTFILE:
            
            key = LOAD_KEY()
            f = Fernet(key)
            encrypted_content = pickle.load(INPUTFILE)
            decrypted_content = f.decrypt(encrypted_content)
            decoded_content = decrypted_content.decode()
            OUTPUTFILE.writelines(decoded_content)

def RUN_BIN(INPUTNAME):
    SAVE_AS_PY(INPUTNAME)
    os.system(PYOUTPUTNAME + ' 1')
    os.remove(PYOUTPUTNAME)

if __name__ == '__main__':
    try:
        OPERATION_TYPE = sys.argv[1]
        OPERATION_PATH = sys.argv[2]
        OPERATION_FILENAME = sys.argv[3]
        if OPERATION_TYPE == '1':
            OPERATION_PATHTARGET = sys.argv[4]
            OPERATION_FILENAMETARGET = sys.argv[5]
    except:
        raise Exception('Missing parameters')

    if platform.system() == 'Windows':
        INPUTFULLNAME = OPERATION_PATH + "\\" + OPERATION_FILENAME
    else:
        INPUTFULLNAME = OPERATION_PATH + "//" + OPERATION_FILENAME

    if OPERATION_TYPE == '1':
        ''' Save as bin '''
        if platform.system() == 'Windows':
            OUTPUTFULLNAME = OPERATION_PATHTARGET + "\\" + OPERATION_FILENAMETARGET
        else:
            OUTPUTFULLNAME = OPERATION_PATHTARGET + "//" + OPERATION_FILENAMETARGET
        SAVE_AS_BIN(INPUTFULLNAME, OUTPUTFULLNAME)
    elif OPERATION_TYPE == '2':
        ''' Run bin formatted file. Generates o.py then executes it '''
        RUN_BIN(INPUTFULLNAME)
    else:
        raise Exception('Invalid operation type')