# ransomware

# Criptografia Simples de Arquivos em Python

Este projeto consiste em dois scripts Python que permitem criptografar e descriptografar arquivos usando a criptografia simétrica AES. O projeto é ideal para quem deseja entender como funciona a criptografia de arquivos de forma simples e segura.

## Requisitos

- Python 3.x
- Biblioteca `cryptography` instalada

Você pode instalar a biblioteca `cryptography` executando o seguinte comando:

```bash
pip install cryptography
Arquivos do Projeto
encrypter.py: Script responsável por criptografar arquivos.
decrypter.py: Script responsável por descriptografar arquivos previamente criptografados.
Como Usar
1. Criptografando um Arquivo
Para criptografar um arquivo, execute o script encrypter.py. Ele requer dois parâmetros:

O caminho do arquivo que você deseja criptografar.
A senha utilizada para gerar a chave de criptografia.
Exemplo:
bash
Copiar código
python encrypter.py arquivo.txt minhasenha
Este comando irá criptografar o arquivo arquivo.txt usando a senha minhasenha e gerar um novo arquivo chamado arquivo.txt.enc contendo os dados criptografados.

2. Descriptografando um Arquivo
Para descriptografar um arquivo criptografado, execute o script decrypter.py. Ele requer dois parâmetros:

O caminho do arquivo criptografado.
A mesma senha utilizada para criptografar o arquivo.
Exemplo:
bash
Copiar código
python decrypter.py arquivo.txt.enc minhasenha
Este comando irá descriptografar o arquivo arquivo.txt.enc e gerar um novo arquivo chamado arquivo.txt.dec com o conteúdo original.

#Como Funciona
#Criptografia
O script encrypter.py realiza a criptografia do arquivo utilizando o algoritmo AES no modo CBC (Cipher Block Chaining). A senha fornecida pelo usuário é usada para gerar uma chave de 16 bytes (128 bits) que é utilizada para a criptografia. Além disso, um vetor de inicialização (IV) aleatório é gerado para garantir a segurança da criptografia.

O arquivo é então criptografado, e o IV é armazenado no início do arquivo criptografado, juntamente com os dados criptografados.

#Descriptografia
O script decrypter.py realiza a descriptografia do arquivo criptografado. Ele começa extraindo o IV do início do arquivo criptografado, utiliza a mesma chave derivada da senha fornecida e descriptografa os dados. Após a descriptografia, o preenchimento (padding) utilizado durante a criptografia é removido, e o arquivo original é restaurado.

Observações
Segurança: O uso de uma chave derivada diretamente da senha pode não ser seguro para aplicações reais. Em um cenário de produção, recomenda-se o uso de um salt mais robusto e técnicas de derivação de chave mais seguras, como PBKDF2 ou bcrypt.
Limitações: Este exemplo não implementa funcionalidades de gerenciamento de erros ou validação de entrada, sendo um exemplo simples e didático.
Uso Ético: A criptografia deve ser utilizada para proteger dados de forma ética e legal.
