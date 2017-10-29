alpha = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_'

def decrypt(cipher, key):
    key *= len(cipher) // len(key) + 1
    for i, j in enumerate(cipher):
        print(alpha[(alpha.find(j) - alpha.find(key[i])) % 33], end='')
		
s = 'ХЫДЫЮЭНГЩЫЫЮНМРЩОФХЯВЭО'
key = 'НОС'
s = s.strip('\t\n')
decrypt(s, key)
print()
