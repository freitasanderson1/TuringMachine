import hashlib

def getHash(code):
    return hashlib.md5(code.encode()).hexdigest()

def CodeToHash(code, filename='t1.hashes'):
    with open(filename, 'a') as f:
      f.write(f'{getHash(code)}\n')

if __name__ == "__main__":
    CodeToHash(input('Insira um código:\n'))
    print("Hashes adicionados ao arquivo t1.hashes.")
