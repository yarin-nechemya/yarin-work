
def prepare_for_encryption(text:str) -> str:
    return ''.join(
        char for char in text.upper()
        if 'A' <= char <= 'Z'
    )

def encrypt(msg:str, key:int) -> str:
    msg = prepare_for_encryption(msg)
    encrypted = ""
    for letter in msg:
        encrypted += chr((ord(letter)-ord("A")+key)%26 + ord("A") )
    return encrypted

def decrypt(msg:str, key:int) -> str:
    decrypted = ""
    for letter in msg:
        decrypted += chr((ord(letter)-ord("A")-key)%26 + ord("A"))
    return decrypted
