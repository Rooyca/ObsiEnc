import os
from Crypto.Protocol.KDF import PBKDF2

from dotenv import load_dotenv
load_dotenv()

password = os.getenv('PSWD')

"""

!!! README !!!

Please update salt variable
Go to 'updateSalt.py'

"""

salt = b'Salt goes here' 

key = PBKDF2(password, salt, dkLen=32)