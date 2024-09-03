from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_data(key, data):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decrypt_data(key, encrypted_data):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
