from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as f:
        data = f.read()
    
    # Extrair o IV do início do arquivo criptografado
    iv = data[:16]
    encrypted_data = data[16:]
    
    # Gerar a chave a partir da senha
    key = password.encode()[:16]
    
    # Configurar o algoritmo AES no modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Descriptografar os dados
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remover o preenchimento
    padding = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding]
    
    # Escrever o arquivo descriptografado
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)
    
    print(f"Arquivo descriptografado com sucesso: {decrypted_file_path}")

# Exemplo de uso
decrypt_file('arquivo.txt.enc', 'minhasenha')
