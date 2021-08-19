import hashlib

text = input("Digite o texto: ")

op = int(input(''' ---- MENU - ESCOLHA O TIPO DE HASH ----
1) MD5
2) SHA1
3) SHA256
4) SHA512
Opção: '''))

if op == 1:
    result = hashlib.md5(text.encode('utf-8'))
    print(f"O hash MD5 do texto \"{text}\" é: {result.hexdigest()}")
elif op == 2:
    result = hashlib.sha1(text.encode('utf-8'))
    print(f"O hash SHA1 do texto \"{text}\" é: {result.hexdigest()}")
elif op == 3:
    result = hashlib.sha256(text.encode('utf-8'))
    print(f"O hash SHA256 do texto \"{text}\" é: {result.hexdigest()}")
elif op == 2:
    result = hashlib.sha512(text.encode('utf-8'))
    print(f"O hash SHA512 do texto \"{text}\" é: {result.hexdigest()}")
else:
    print("Opção inválida")

