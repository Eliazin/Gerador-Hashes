import hashlib

string = input("Digite o texto a ser transformado em hash: ")

menu = int (input(''' #### MENU - ESCOLHA O TIPO DE HASH ##### 
                1) MD5
                2) SHA1
                3) SHA224
                4) SHA256
                5) SHA384
                6) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("A hash MD5 da string", string, "é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("A hash SHA1 da string", string, "é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha224(string.encode('utf-8'))
    print("A hash SHA224 da string", string, "é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("A hash SHA256 da string", string, "é: ", resultado.hexdigest())
elif menu == 5:
    resultado = hashlib.sha384(string.encode('utf-8'))
    print("A hash SHA384 da string", string, "é: ", resultado.hexdigest())
elif menu == 6:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("A hash SHA512 da string", string, "é: ", resultado.hexdigest())
else:
    print("Opção inválida")
    exit()