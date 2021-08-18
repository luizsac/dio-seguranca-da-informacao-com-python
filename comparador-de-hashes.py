import hashlib

a_file = "a.txt"
b_file = "b.txt"

hash1 = hashlib.new("ripemd160")
hash1.update(open(a_file, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(b_file, "rb").read())

if hash1.digest() != hash2.digest():
    print(f"O arquivo {a_file} é diferente do arquivo {b_file}")
else:
    print(f"O arquivo {a_file} é igual ao arquivo {b_file}")

print(f"O hash do arquivo {a_file} é {hash1.hexdigest()}")
print(f"O hash do arquivo {b_file} é {hash2.hexdigest()}")
