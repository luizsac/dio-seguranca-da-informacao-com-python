import random, string

size = int(input("Insira o tamanho da senha: "))

chars = string.ascii_letters + string.digits + "!@#$%&*£¢-=+_"

rnd = random.SystemRandom()

print(("".join(rnd.choice(chars) for i in range(size))))
