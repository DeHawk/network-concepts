# Default character encoding test

str = "Hello World!"

print("String = ",str)

en_str = str.encode("ISO-8859-1")

print("byte sequence: ")
for byte in en_str:
    print(byte, hex(byte))

dec_str = en_str.decode("ISO-8859-1")

print("Decoded String = ", dec_str)
