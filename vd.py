import argparse
import sys
alpha = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_'


def ParseArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='input_file', help="File with encrypted message", required=True)
    parser.add_argument('-k', action='store', dest='key', help="A key for decryption", required=True)
    return(parser.parse_args())


def decrypt(cipher, key):
    key *= len(cipher) // len(key) + 1
    for i, j in enumerate(cipher):
        print(alpha[(alpha.find(j) - alpha.find(key[i])) % 33], end='')


if __name__ == '__main__':
    args = ParseArgs(sys.argv)
    f = open(args.input_file, 'r')
    s = f.read()
    f.close()
    s = s.strip('\t\n')
    decrypt(s, args.key)
    print()