from Crypto.Cipher import AES
from Crypto import Random
import os
import hashlib
import time

class AESCipher():
	#constructor
    def __init__(self,filename):
        self.filename = filename
        self.file_ext = os.path.splitext(self.filename)
        self.out_filename = "{}_{}{}.enc".format(self.file_ext[0], hashlib.md5(str(time.time())).hexdigest(), self.file_ext[-1])
        self.bs = AES.block_size
        self.key = open("AESCipher/key.txt","rb").read()
        self.iv = open("AESCipher/iv.txt","rb").read()
        self.file_size = os.path.getsize(self.filename)
        self.chunk_size = 1024

    def encrypt(self):
        cipher = AES.new(self.key,mode=AES.MODE_OFB,IV=self.iv)
        
        with open(self.filename, "rb") as infile:
            with open(self.out_filename, "wb") as outfile:
                while True:
                    chunk = infile.read(self.chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % self.bs != 0:
                        chunk = self._pad(chunk)
                    outfile.write(cipher.encrypt(chunk))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
    
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
