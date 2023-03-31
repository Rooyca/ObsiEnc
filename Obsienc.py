import os, json, subprocess, sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime

from variables import *

from dotenv import load_dotenv
load_dotenv()

dec_dir = os.getenv('DEC_PATH')
enc_dir = os.getenv('ENC_PATH')

args = sys.argv

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        message = f.read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))

    return cipher.iv, ciphered_data


def main_encrypt():
	for dirpath, dirnames, filenames in os.walk(dec_dir):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)

			if ".git" not in dirpath:
				if not filename.endswith('.enc'):
					full_path = './EncryptRepo/'+'/'.join(dirpath.split('Obsidian')[1:])
					
					iv, ciphered_data = encrypt_file(file_path, password)

					if not os.path.exists(full_path):
						os.makedirs(full_path)

					output_file_path = os.path.join(full_path, filename + '.enc')
					with open(output_file_path, 'wb') as f:
						f.write(iv)
						f.write(ciphered_data)

	try:
		subprocess.Popen(f'cd EncryptRepo/ && git add . && git commit -m {datetime.now().date().isoformat()} > /dev/null', shell=True)
		print("Pleace go to './EncryptRepo' and PUSH your repository.")
	except:
		print("Pleace create a repository inside './EncryptRepo'")

	

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphered_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

    return data


def main_decrypt():
    for dirpath, dirnames, filenames in os.walk(enc_dir):
        for filename in filenames:
            if filename.endswith('.enc'):  

                file_path = os.path.join(dirpath, filename)
                full_path = dec_dir+'/'.join(dirpath.split('EncryptRepo')[1:])+'/'

                if not os.path.exists(full_path):
                    os.makedirs(full_path)

                output_file_path = os.path.join(full_path, filename[:-4])
                with open(output_file_path, 'wb') as f:
                    f.write(decrypt_file(file_path, password))

if __name__ == '__main__':
	if "dec" in args[1]:
		main_decrypt()

	if "enc" in args[1]:
		main_encrypt()
