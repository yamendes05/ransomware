from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_path, password):
    # Gerar uma chave de 16 bytes a partir da senha
    key = password.encode()[:16]  # Ajusta para 16 bytes (128 bits)
    
    # Gerar um vetor de inicialização (IV) aleatório
    iv = os.urandom(16)
    
    # Configurar o algoritmo AES no modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Preencher os dados para que o tamanho seja múltiplo de 16
    padding = 16 - len(data) % 16
    data += bytes([padding]) * padding
    
    # Criptografar os dados
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    
    # Escrever o arquivo criptografado com IV
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)  # Salvar o IV no início do arquivo
    
    print(f"Arquivo criptografado com sucesso: {encrypted_file_path}")

# Exemplo de uso
encrypt_file('arquivo.txt', 'minhasenha')
