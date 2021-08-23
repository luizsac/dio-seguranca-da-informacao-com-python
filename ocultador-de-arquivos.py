import ctypes

hide_attribute = 0x02

feedback = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", hide_attribute)

if feedback:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")
